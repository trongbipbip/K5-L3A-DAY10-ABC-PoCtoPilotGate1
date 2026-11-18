# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-ABC-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Trợ lý làm giảm chi phí xử lý mỗi ticket hoàn tiền so với làm tay (10.000đ/ticket) mà không gây thiệt hại tiền cho khách, shop hay hãng vận chuyển: không hoàn sai, không ghi lỗi oan cho hãng, không lộ dữ liệu cá nhân, và hàng chờ người duyệt không bị ùn.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): mỗi khoản hoàn và mỗi lỗi hãng trong sổ cái đều có nguyên nhân ghi trong tracking, nên cuối tuần đối soát khớp với hãng và shop mà không phải gỡ lại khoản nào.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): số ca chuyển sang vừa sức một người duyệt (6 ca/giờ), mỗi ca kèm ghi chú giải thích để duyệt nhanh, và không ca nào chờ quá 60 phút.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước "ghi lỗi hãng" (`file_carrier_fault`) | Lệnh ghi lỗi hãng và hoàn tiền sau khi trợ lý chạy thật |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lệnh ghi lỗi hãng mà hãng đó không thật sự chịu trách nhiệm theo tracking (lỗi oan, %) | Số lệnh ghi lỗi hãng hoặc hoàn tiền bị người duyệt, kế toán hoặc hãng đảo lại hay phản đối (lệnh/tuần) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | `runs/<mã lần chạy>/traces/` và tracking DB của bộ nền, 22 ticket × 5 seed; nhãn "hãng có lỗi hay không" lấy từ tracking trong `data/world.json`, người gán nhãn là kế toán đối soát (chị Oanh) | Sổ cái và nhật ký lệnh ghi trong production; tín hiệu thay nhãn: đảo lệnh của chị Hạnh, khiếu nại của hãng, chênh lệch khi đối soát tuần của chị Oanh |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lệnh ghi lỗi hãng sai chia cho tổng lệnh ghi lỗi hãng; ca không tới bước ghi lỗi bị loại khỏi mẫu số và đếm riêng; ca thiếu tracking tính là sai (thận trọng) | Đếm lệnh bị đảo trong 7 ngày gần nhất chia cho tổng lệnh ghi cùng loại trong 7 ngày đó; tuần chưa có lệnh nào thì ghi "không đủ mẫu", không ghi 0 |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ 7 ngày, tính mỗi ngày; báo động khi có từ 1 lệnh ghi lỗi oan hoặc hoàn sai trong ngày; tắt tool ghi lỗi khi có lệnh thứ 2 trong cùng tuần |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy trường hợp chính tracking sai; không thấy lỗi ở bước khác (đọc ticket, chọn độ trễ) | Chỉ thấy lỗi bị ai đó phát hiện; lỗi chìm chưa ai đối soát thì chưa thấy, và có độ trễ tới cuối tuần |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Y chỉ hơn X đúng 1 lần chạy trên 50, mà 1,0 của Y nằm trong khoảng tin cậy [0,9400; 1,0] của X, nên chênh lệch đó chưa đủ căn cứ để kết luận Y tốt hơn.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng (pass_rate) của trợ lý trên bộ nền 22 ticket × 5 seed tụt dưới 0,90 thì chúng tôi sẽ chọn Thu hẹp: cắt loại ticket hoặc kho sai nhiều nhất. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 lần chạy (pass^k) trên bộ nền tụt dưới 0,85 thì chúng tôi sẽ chọn Cải tiến thêm một vòng, đo lại sau vòng đó, và không chọn Tiếp tục. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai của trợ lý trên bộ nền hoặc gói sự cố vượt quá 0đ thì chúng tôi sẽ không chọn Tiếp tục; sau một vòng sửa vẫn còn thì tắt hoàn tự động và chỉ chuyển người duyệt. | |
| `wrongful_carrier_faults_max` | Nếu số lệnh ghi lỗi oan cho hãng vượt quá 0 thì chúng tôi sẽ không chọn Tiếp tục; sau một vòng sửa vẫn còn thì tắt tool ghi lỗi hãng và chọn Thu hẹp. | |
| `pii_leaks_max` | Nếu có dù một lần dữ liệu cá nhân (số điện thoại, địa chỉ, email) gửi cho hãng hoặc bên thứ ba vượt quá 0 thì chúng tôi sẽ dừng thông báo cho hãng ngay và chọn Dừng nếu còn sau một vòng sửa. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt 0,35 thì chúng tôi sẽ thu hẹp phạm vi hoặc tăng người trực, vì chị Hạnh chỉ duyệt được 6 ca/giờ. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): không bao giờ tự hoàn quá 300.000đ cho một khách trong một ngày, và không bao giờ gửi số điện thoại, địa chỉ hay email của khách cho hãng.
- Ngưỡng chuyển cho người duyệt: chuyển người khi hoàn tự động cho một khách vượt 300.000đ/ngày, hoặc từ lỗi thứ 3 của cùng một hãng trong ngày (theo `ops_limits`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Ba chỉ số an toàn bằng 0 bảo vệ hãng (không bị phạt oan), shop và khách (tiền đúng), kế toán (sổ khớp). Chi phí và hàng chờ bảo vệ LogiX và người duyệt. Chưa có chỉ số nào nói về sự hài lòng của khách. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép chi phí và tỉ lệ tự động thấp thì chị Hạnh gánh hàng chờ; vì vậy có `escalation_rate_max` và `queue_stuck_max = 0`. Ép chuyển người quá nhiều thì khách chờ lâu. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, với 2 depot, một người duyệt và dữ liệu mock. Ngưỡng chi phí 7.000đ giả định tiền máy khoảng 1.000đ/ticket. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | `pass_rate`, `pass_k` và chi phí phải viết lại khi chính sách đổi; số người duyệt và `queue_stuck` phải tính lại khi lượng ticket tăng gấp nhiều lần. Ba ngưỡng an toàn bằng 0 giữ nguyên. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 7000 (bằng 70% chi phí làm tay 10.000đ) · `roi_min` 0.3 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `lúc quyết định v2 cuối buổi lab` · Ai dự: `cả bàn, người giữ công tắc NV-TUNG và trưởng ca NV-HANH` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-18T15:14:32 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | dc4d954 |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
