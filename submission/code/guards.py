"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
import re

from . import helpers as H  # noqa: F401
from .tools import Verdict


_CLAIMED_DELAY = re.compile(
    r"(?:trễ|tre|chậm|muộn|late|delay(?:ed)?)\D{0,24}?"
    r"(\d{1,3})\s*(?:ngày|ngay|days?|hôm)",
    re.I,
)


def _claimed_delay_days(text):
    match = _CLAIMED_DELAY.search(text or "")
    return int(match.group(1)) if match else None


def pre_guard(ctx):
    policies = ctx.tools.lookup_policies()
    policy = H.effective_policy(policies, ctx.as_of)

    if policy is None:
        return Verdict.escalate("Không tìm thấy chính sách hoàn tiền đang hiệu lực")

    order_id = ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    claimed_days = _claimed_delay_days(ctx.ticket.get("text", ""))
    if order is not None and claimed_days is not None:
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        if parcel is not None:
            tracked_days = H.db_delay_days(parcel, ctx.as_of)
            if claimed_days != tracked_days:
                matched = _CLAIMED_DELAY.search(ctx.ticket.get("text", ""))
                neutral_text = re.sub(
                    r"\d{1,3}\s*(?:ngày|ngay|days?|hôm)",
                    "",
                    matched.group(0),
                    flags=re.I,
                )
                ctx.log(
                    "ticket_tracking_mismatch",
                    claimed_delay_days=claimed_days,
                    tracking_delay_days=tracked_days,
                )
                return Verdict.rewrite(
                    "Loại số ngày tự khai để agent dùng tracking có thẩm quyền",
                    ctx.ticket["text"].replace(matched.group(0), neutral_text, 1),
                )

    # Ghim phiên bản theo ngày hiệu lực, thay vì tin cờ index_active.
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")

    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("Không xác minh được đơn và chủ đơn trước khi hoàn tiền")

        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if policy is None:
            return Verdict.escalate("Không tìm thấy chính sách hiệu lực để xác minh tiền hoàn")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        if parcel is None:
            return Verdict.escalate("Không xác minh được kiện hàng trước khi hoàn tiền")
        if parcel.get("status") == "DELIVERED" and not parcel.get("delivered_date"):
            return Verdict.escalate(
                "Tracking ghi đã giao nhưng thiếu ngày giao; chuyển người duyệt"
            )
        delay_days = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause") or ("CARRIER" if delay_days > 0 else None)
        expected = H.entitlement_vnd(policy, order, delay_days, cause)
        proposed = int(action.get("amount_vnd", 0))

        if proposed != expected:
            ctx.log(
                "refund_mismatch",
                order_id=order["order_id"],
                proposed_vnd=proposed,
                expected_vnd=expected,
                tracking_delay_days=delay_days,
            )
            return Verdict.escalate(
                "Số tiền đề xuất không khớp tracking và chính sách; chuyển người duyệt"
            )

    elif tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None:
            return Verdict.deny("Không ghi lỗi hãng khi không tìm thấy đơn")

        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        if policy is None or parcel is None:
            return Verdict.deny("Thiếu dữ liệu để xác minh lỗi hãng")

        if parcel.get("status") == "DELIVERED" and not parcel.get("delivered_date"):
            return Verdict.deny(
                "Tracking ghi đã giao nhưng thiếu ngày giao; không ghi lỗi hãng tự động"
            )

        delay_days = H.db_delay_days(parcel, ctx.as_of)
        recorded_cause = parcel.get("delay_cause")
        supported = (
            recorded_cause in policy["fault_causes"]
            and H.carrier_at_fault(policy, parcel, delay_days)
        )
        if not supported:
            ctx.log(
                "carrier_fault_denied",
                order_id=order["order_id"],
                parcel_id=parcel["parcel_id"],
                tracking_delay_days=delay_days,
                recorded_cause=recorded_cause,
            )
            return Verdict.deny("Tracking không đủ căn cứ để ghi lỗi cho hãng")

        max_strikes = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        existing_strikes = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
        if max_strikes is not None and existing_strikes >= max_strikes:
            ctx.log(
                "carrier_fault_cap_reached",
                carrier_id=parcel["carrier_id"],
                existing_strikes=existing_strikes,
                cap=max_strikes,
            )
            return Verdict.deny(
                "Đã đạt trần lỗi tự động của hãng trong ngày; chuyển người duyệt"
            )

        # Agent có thể chọn kiện đầu tiên nhưng gắn số ngày trễ của kiện khác.
        # Chuẩn hóa lệnh theo kiện trễ nhất và dữ liệu tracking có thẩm quyền.
        corrected = {
            "parcel_id": parcel["parcel_id"],
            "carrier_id": parcel["carrier_id"],
            "driver_id": parcel.get("driver_id"),
            "delay_days": delay_days,
        }
        if any(action.get(key) != value for key, value in corrected.items()):
            ctx.log(
                "carrier_fault_corrected",
                order_id=order["order_id"],
                parcel_id=parcel["parcel_id"],
                tracking_delay_days=delay_days,
            )
            return Verdict.modify(
                "Đã sửa thông tin lỗi hãng theo kiện và tracking có thẩm quyền",
                **corrected,
            )

    elif tool == "notify_carrier":
        payload = action.get("payload") or {}
        blocked = set(
            ((ctx.gates or {}).get("legal") or {}).get(
                "pii_fields_blocked_to_third_party"
            ) or []
        )
        # Không gửi nguyên văn ticket hoặc thông tin liên hệ người nhận cho hãng.
        blocked.update({"customer_note", "recipient_contact", "phone", "name"})
        safe_payload = {key: value for key, value in payload.items() if key not in blocked}

        if safe_payload != payload:
            ctx.log(
                "carrier_payload_sanitized",
                removed_fields=sorted(set(payload) - set(safe_payload)),
            )
            return Verdict.modify(
                "Đã loại nội dung ticket và trường dữ liệu cá nhân khỏi thông báo hãng",
                payload=safe_payload,
            )

    return Verdict.allow()
