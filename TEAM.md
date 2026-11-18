# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 |           |      |     |             |
|   3 |           |      |     |             |
|   4 |           |      |     |             |

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
