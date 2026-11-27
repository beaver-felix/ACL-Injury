# Product brief / scope contract
Status: PROPOSED • Owner A • 27/11/2026

## 1. Đề thi làm core
Nguồn chính thức: https://techday.momo.vn/topic.html ; https://techday.momo.vn/assets/docs/the-le-cuoc-thi.pdf (Điều 9–13, 14, 18). HTML người dùng gửi chỉ có section topicPage rỗng và JS ngoài; nội dung đề lấy từ kết quả lập chỉ mục trang chính thức, thể lệ từ PDF text. Kiểm tra lại FAQ và bản đề đầy đủ trước freeze. Chủ đề Imagine the Future Workspace, Human Centered / AI Powered; chọn Chống lừa đảo, bổ trợ An ninh mạng. Người dùng tự chọn; AI phải cốt lõi; giám khảo phải dùng trực tuyến không phụ thuộc máy local.

| Ràng buộc chính thức | Cách đáp ứng / evidence |
|---|---|
| AI cốt lõi | Phân tích ngữ cảnh Việt, hình ảnh + văn bản + bằng chứng và lời khuyên; demo thật với AI, so sánh với rule-only |
| Dùng trực tuyến | Public HTTPS web demo dùng cùng API; ZIP extension tải từ trang hướng dẫn, Chrome Load unpacked; không cần API key từ giám khảo |
| Hướng dẫn PDF ≤1 trang A4 | URL, 3 bước thử web, cách tải extension tùy chọn, giới hạn quyền riêng tư |
| Source ZIP + README | Toàn bộ source + lockfiles + Dockerfile + hướng dẫn + khai báo tài sản có sẵn, OSS, AI, dữ liệu |
| Slide PDF ≤10 trang | Problem, target, UX, architecture, AI, evaluation, impact, privacy/limits; freeze khi nộp |
| Video MP4 ≤3 phút | Quay luồng thật, cả scam và benign, không dùng mock giả làm thật |
| Deadline 03/12 23:59:59 ICT | Submit nội bộ 18:00; trưởng nhóm giữ xác nhận nền tảng |
| Duy trì đến hết TechDay 11/12 | Pin image/revision, quota/billing đủ, health monitoring; không chỉnh sửa bài nộp sau hạn |
| Quyền dữ liệu/tài sản | Chỉ fixture tự tạo; liệt kê provenance/licence; không nộp sản phẩm làm trước 20/11 |

Hạn gửi câu hỏi làm rõ: 27/11 23:59:59 ICT, techday@mservice.com.vn; chỉ FAQ chính thức có giá trị như phần đề. Hỏi ngay về Load unpacked + web demo, giới hạn tài nguyên/model (nếu có). Không giả định BTC tài trợ API. Kiểm tra đã đăng ký trước hạn cùng ngày.

## 2. Problem & user
Người dùng Việt Nam mua sắm, đọc quảng cáo, email/chat trên Chrome desktop gặp yêu cầu chuyển tiền/OTP, mạo danh ngân hàng, ví điện tử, tuyển dụng, đầu tư, đơn hàng. Bộ lọc URL không đủ cho lời dụ dỗ trong ảnh/tin nhắn hoặc website hợp lệ bị lợi dụng. Giải pháp: giúp người dùng tạm dừng trước hành động tài chính, hiểu lý do và tự xác minh qua kênh chính thức.

JTBD: Khi nghi ngờ một nội dung, tôi muốn kiểm tra ngay tại trang đang xem, nhận bằng chứng cụ thể và bước tiếp theo bằng tiếng Việt, không phải tự suy đoán hay gửi cả lịch sử trình duyệt.

## 3. MVP acceptance (P0)
- P0-1 Extension MV3: người dùng bấm icon, chụp viewport HTTP(S), xem trước, cắt vùng hoặc bỏ ảnh để nhập text, đồng ý gửi; không quét ngầm. Có text paste fallback.
- P0-2 Web demo public: paste text hoặc chọn ảnh PNG/JPEG, preview, consent, phân tích qua cùng API; có 3 fixture mẫu tự tạo, chạy AI thật.
- P0-3 AI vision/text hiểu ngữ cảnh Việt: nhận diện mạo danh, thúc giục, yêu cầu bí mật/chuyển tiền, quảng cáo lợi nhuận; phân loại LOW/MEDIUM/HIGH/UNKNOWN, giải thích bằng bằng chứng quan sát, hướng dẫn cụ thể. Không kết luận một người là kẻ lừa đảo hay cam kết an toàn.
- P0-4 Backend một Docker container, public HTTPS, schema validation, provider key server-only, bounded input, no-store, timeout, rate limit, error states; fallback trung thực UNKNOWN nếu AI lỗi.
- P0-5 QA: ít nhất 30 fixture (15 nghi scam, 10 benign, 5 mơ hồ/ảnh khó) + security/error tests. Public smoke từ máy khác. Báo số thật.
- P0-6 Bộ bài nộp đầy đủ và release có thể truy cập tới 11/12.

P1 (chỉ sau gate 30/11): URL reputation theo domain (không truy cập URL tùy ý), crop nâng cao, optional QR decode local chỉ để hiển thị không mở link; nếu P0 crop chưa xong thì ưu tiên crop cơ bản. Không đưa P1 vào lời hứa demo trước khi chạy thật.

Out of scope: mobile, realtime monitoring, auto-block, đọc tất cả tab/chat, ngân hàng thật, đăng nhập/hồ sơ cá nhân, database lưu ảnh, browser store approval, training model từ đầu, multi-agent/RAG/vector DB, QR payment verification, click/transfer tự động.

## 4. Điểm khác biệt cần chứng minh
Không tuyên bố đầu tiên trên thế giới: thị trường đã có AI screenshot scan. Điểm nhấn là in-context capture ít thao tác + ngữ cảnh social engineering Việt + evidence-to-action (người dùng hiểu tại sao nên dừng), privacy by design. Public demo chạy cùng engine. Đánh giá AI vs lexical baseline trên cùng holdout; ghi rõ mẫu nhỏ/synthetic, không suy rộng.

## 5. Mapping tiêu chí chính thức
- Sáng tạo: bằng chứng ảnh/ngôn ngữ + phản ứng trước chuyển tiền; competitor table.
- Chất lượng: live demo, lỗi/ảnh không đọc được, UI tiếng Việt, không safe guarantee, latency/test evidence, public smoke.
- Tiềm năng tác động: bối cảnh người dùng fintech, kiến trúc stateless, chi phí mỗi scan và mở rộng; chưa đo mức giảm thiệt hại thực tế.
