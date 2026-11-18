# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S1`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Đào Trường Vũ | 2A202603721 | Sản phẩm và kinh doanh (C) |             |
|   2 | Hồ Sỹ Tùng | 2A202603650 | Kỹ sư cổng (trace, chỉ số) (B) |             |
|   3 | Nguyễn Nho Trọng | 2A202603666 | Kỹ sư cổng (cổng code) (A) |             |
|   4 | Bùi Quang Hiếu | 2A202603639 | Vận hành và pháp lý (D) |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

Bàn có 4 người, lab có 3 vai, nên vai Kỹ sư cổng chia cho hai người (A, B). Tên thật của A–D điền ở bảng "Thành viên" phía trên.

| Người | Vai | Câu của đề | File chính | Công việc |
| ----- | --- | ---------- | ---------- | --------- |
| A | Kỹ sư cổng (cổng code) | 2.1, 2.6, 2.7 | `lab10/guards.py` | Chạy lệnh 2 và 4 trên bộ base; viết 2–3 cổng trong `pre_guard` / `write_gate`; thêm hai bước tránh rò rỉ dữ liệu. Vòng 2: sửa nhánh code theo thẻ sự cố (C7). |
| B | Kỹ sư cổng (trace, chỉ số) | 2.2, 2.8 | `lab10/monitors.py` | Dò `T-002@55` bằng lệnh 3 và điền bảng soát lỗi (B2); viết tính chất cùng hai ticket hiểm chạy bằng `--adhoc`. Vòng 2: thêm ít nhất một chỉ số theo dõi mới (C8), chạy `eval` và `grade`. |
| C | Sản phẩm và kinh doanh | 1.1–1.6, 2.3, 2.9 | `config/acceptance_criteria.json`, `config/operating_gates.json` (mục `business`) | Phiếu A: viết và ký tiêu chí (lệnh 1, chỉ ký một lần); bản đồ dữ liệu và drift; điền trần hoàn tiền, ngân sách chi phí, phạm vi pilot, ROI. Chốt quyết định v1 (B8) và v2 (C12). |
| D | Vận hành và pháp lý | 2.4, 2.10 | `config/operating_gates.json` (mục `operations`, `legal`), `submission/submission.json` | HAZOP vòng 1 và checklist 9 nhóm (mỗi dòng một người phụ trách có tên); điền người trực, hàng đợi, điều kiện dừng, dữ liệu cá nhân; viết runbook. Vòng 2: risk register (C10), cập nhật checklist và runbook (C11); gom bài bằng lệnh 7. |

**Làm chung cả bàn:** pre-mortem (2.5, B6), phân tích sự cố (3.1–3.4), quyết định Gate 1, demo.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## BuiQuangHieu-2A202603639

### Phần việc phụ trách

Vai D · Vận hành và pháp lý: câu 2.4 (HAZOP vòng 1, checklist 9 nhóm việc tại Phiếu B mục B4–B5); câu 2.10 (cổng `operations`, `legal` trong `config/operating_gates.json`, runbook 1–3 và giờ cao điểm tại B7.5–B7.6). Vòng 2: risk register C10, cập nhật checklist và runbook C11; tổng hợp `submission/submission.json` và chạy lệnh 7 sau khi cả bàn hoàn tất các mốc trước.

### Đóng góp cụ thể

- Đã đọc đề, rubric, hướng dẫn và dữ liệu vận hành để xác định các mốc phụ thuộc trước khi điền phần D.
- Đã điền tên, MSSV, vai và mục cá nhân trong `TEAM.md`.
- Có dùng trợ lý AI để đọc tài liệu, soát yêu cầu và hỗ trợ phần việc D; các ngưỡng và quyết định phải được bàn xác nhận theo dữ liệu trước khi ghi.
- Đã điền `operations` và `legal` trong `config/operating_gates.json` theo `data/world.json` và tiêu chí đã ký; viết runbook 1–3 và giờ cao điểm tại Phiếu B mục B7.5–B7.6. Có dùng trợ lý AI soạn và kiểm tra phần này; bàn cần xác nhận các ngưỡng vận hành trước khi chốt vòng 1.
- B4 đã được thành viên khác điền; đã điền B5 với chín PIC có tên trong dữ liệu `staff` hoặc tên thành viên đã biết, phân biệt trạng thái Xong/Chưa theo bằng chứng hiện có. Chờ mốc prepared và thẻ sự cố đã bốc, báo cáo sau sửa trước khi điền C10–C11, `submission/submission.json` và gom bài.

### Bằng chứng

- `TEAM.md` (bảng thành viên và mục cá nhân này); `config/operating_gates.json` (`operations`, `legal`); `templates/form-b-evaluation-gates.md` (B5, B7.5–B7.6). B5 trỏ tới các mã chạy base `R-base-before-20261118-152646-bde05c` và after `R-base-after-20261118-155059-1107eb` do nhóm ghi ở B0. Mã commit sẽ bổ sung sau khi nhóm chốt các mốc.

### Exit ticket

- Học được: cổng vận hành phải có người chịu trách nhiệm, ngưỡng đo và thao tác dừng rõ ràng, khớp config.
- Còn chưa chắc: hàng chờ, chi phí và mức rủi ro còn lại khi nhận đúng thẻ sự cố của bàn; cần kiểm bằng report ba mốc.

## DaoTruongVu-2A202603721

### Phần việc phụ trách

Vai C · Sản phẩm và kinh doanh: Phiếu A (câu 1.1–1.6, ký tiêu chí trong `config/acceptance_criteria.json`); Phiếu B mục B3 (câu 2.3, bản đồ dữ liệu và ví dụ drift), B6 (câu 2.5, lăng kính kinh doanh của pre-mortem), B7.4 (câu 2.9, mục `business` trong `config/operating_gates.json`); đồng thời PIC ký tiêu chí và quyết định v1 (B8). Vòng 2 (thẻ S1): đọc chi phí mỗi ticket, ROI và trần tiền, câu 3.2 (specification, C5) và quyết định v2 (C12).

### Đóng góp cụ thể

- Điền các ngưỡng bắt buộc, nên có, `business_ops`, `stop_condition` và bốn dòng `decision_rule` cho Bản tiêu chí. Cả bàn đồng ý các con số rồi mới ký; ba chỉ số an toàn đặt 0, chi phí tối đa 7.000đ/ticket thấp hơn làm tay 10.000đ. Chạy `lab10.criteria sign`, commit và push trước lần `eval` đầu tiên của bàn.
- Điền Phiếu A: mục tiêu hệ thống, mục tiêu nhìn từ chị Oanh và chị Hạnh, thước đo bước "ghi lỗi hãng" và telemetry production, câu 1.5 (chọn b), câu tiêu chí "Nếu … thì chúng tôi sẽ …", ranh giới đầu ra.
- Điền `business` trong `config/operating_gates.json`: trần hoàn 1.600.000đ/ngày (80% ngân sách Finance 2.000.000đ), ngân sách tiền máy 1.500đ/ticket, phạm vi pilot `all`, ROI tối thiểu 0,3; mỗi số có một câu lý do trong B7.4.
- Điền B3: bản đồ dữ liệu và ví dụ drift chính sách `REFUND-v3` sang `REFUND-v4` ngày 2026-12-01. Viết bản nháp pre-mortem B6 (sáu lý do, đủ bốn lăng kính, chọn ba cổng) để Kỹ sư cổng có căn cứ viết cổng.
- Có dùng trợ lý AI (Claude) để đọc đề, đọc dữ liệu `data/world.json`, soạn nháp các mục trên và kiểm tra hash, cú pháp JSON. Các ngưỡng và quyết định do bàn xác nhận trước khi ký và chốt; tôi chịu trách nhiệm cho nội dung đã nộp.
- Hỗ trợ nhóm tìm lỗi `integrity`: nguyên nhân là `core.autocrlf=true` trên Windows đổi LF thành CRLF làm lệch hash file bị khoá.

### Bằng chứng

- Commit: `dc4d954` (Sign acceptance criteria, ký lúc 2026-11-18T15:14:32), `ac605db` (Phiếu A), `903d7a3` (`business`, B3, B7.4), `8b6e1c8` (B6).
- File: `config/acceptance_criteria.json` và `.lock` (hash `881d7704…`, `lab10.criteria verify` báo `ok: true`); `config/operating_gates.json` mục `business`; `templates/form-a-criteria.md`; `templates/form-b-evaluation-gates.md` (B3, B6, B7.4).
- Mã lần chạy thẻ S1 làm căn cứ cho C5 (bản đo của tôi): base `R-S1-before-20261118-163939-6c547b`, prepared `R-S1-prepared-20261118-163940-6c547b`; các mã after và quyết định v2 xem Phiếu C của bàn.

### Exit ticket

- Học được: ngưỡng chấp nhận phải viết và ký trước khi xem số, và mỗi ngưỡng cần kèm một hành động nếu trượt; ở S1, lỗi gốc nằm ở dữ liệu (`delivered_date` trống làm tính trễ tới hôm nay) và ở trần lỗi/hãng/ngày, chứ không chỉ ở model.
- Còn chưa chắc: ngưỡng `pass_rate` 0,90, `pass_k` 0,85 và `roi_min` 0,3 được đặt khi chưa biết kết quả nên có thể quá cao hoặc quá thấp; và vì data là mock nên chưa biết con số thật trong pilot sẽ lệch bao nhiêu.

## HoSyTung-2A202603650

### Phần việc phụ trách

Vai B · Kỹ sư cổng (trace, chỉ số): câu 2.2 và 2.8; truy vết `T-002@55`, ghi nhận phân tích ở Phiếu B mục B2, xây dựng hai ticket hiểm để kiểm tra cổng bằng `--adhoc`, và đánh giá kết quả vòng 1 qua `eval`/`gate`. Vòng 2 theo phân công: bổ sung chỉ số theo dõi ở Phiếu C mục C8, rồi chạy `eval` và `grade` trên thẻ sự cố của nhóm.

### Đóng góp cụ thể

- Chạy trace `T-002` với seed `55`; đối chiếu lời khách khai trễ 5 ngày với tracking ghi nhận 2 ngày. Ghi nhận baseline đã hoàn sai 20.000đ, ghi lỗi hãng oan với 5 ngày và gửi nguyên văn ghi chú khách cho hãng.
- Điền phân tích nguyên nhân và biện pháp phòng ngừa của ca `T-002@55` vào Phiếu B mục B2.
- Đề xuất và chạy hai ticket hiểm bằng `--adhoc`: khách phóng đại số ngày trễ và khách yêu cầu bỏ qua chính sách/hoàn toàn bộ đơn. Cả hai được guard chuyển người duyệt trước khi phát sinh ghi sổ.
- Cung cấp kết quả `eval` baseline và các lần chạy sau cổng; đối chiếu bằng `gate`. Trên mốc `prepared`, 110/110 ticket đạt, hoàn sai 0đ, lỗi hãng oan 0, PII leak 0; chi phí 4.510đ/ticket, ROI 1,22 và queue stuck 0.
- Có dùng trợ lý AI để hỗ trợ phân tích trace và biên tập Phiếu B; các lệnh chạy và kết quả được thực hiện/kiểm tra trong repo của nhóm.

### Bằng chứng

- Phiếu B mục B2; trace `T-002@55`.
- Baseline: `R-base-before-20261118-152646-bde05c`.
- Sau cổng: `R-base-after-20261118-161334-5d7dab`; mốc chốt: `R-base-prepared-20261118-161830-5d7dab`.
- Gate sau cổng và prepared: cả hai đều xác nhận các ngưỡng đã ký đạt, không có ca mới hỏng so baseline.
- Commit phần CP3: `b3e902e`; merge nhóm: `8307617`.

### Exit ticket

- Học được: trace cần tách dữ liệu khách tự khai khỏi nguồn sự thật trong tracking; nhìn thấy một lần thực thi thành công chưa đủ, cần kiểm cả các tác dụng phụ như ghi lỗi hãng và payload gửi bên thứ ba.
- Còn chưa chắc: mức độ cổng giữ được an toàn trước thẻ sự cố chưa được xác nhận; cần chạy đúng thẻ của nhóm và bổ sung chỉ số theo dõi ở CP4.
