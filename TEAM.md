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
