# ScamLens VN

ScamLens VN là dự án hackathon MoMo Tech Contest 2026 giúp người dùng đánh giá dấu hiệu lừa đảo trong văn bản và ảnh do họ chủ động chọn. Tên sản phẩm là tạm thời và không hàm ý liên kết chính thức với MoMo.

Repository hiện ở giai đoạn B00: chuẩn bị nền tảng, kiểm tra contract và CI. API, AI engine, Extension, web demo, Docker image và deployment **chưa được triển khai**.

## Nguồn chuẩn và cách bắt đầu

- Quy tắc cho coding agent: [`AGENTS.md`](AGENTS.md).
- Trạng thái đã kiểm chứng mới nhất: [`ai_artifacts/docs/current-state.md`](ai_artifacts/docs/current-state.md).
- Scope và kiến trúc: [`ai_artifacts/docs/product-brief.md`](ai_artifacts/docs/product-brief.md), [`ai_artifacts/docs/architecture-alignment.md`](ai_artifacts/docs/architecture-alignment.md).
- Wire contract và engine port: [`ai_artifacts/docs/api-contracts.md`](ai_artifacts/docs/api-contracts.md), [`ai_artifacts/docs/ai-contract.md`](ai_artifacts/docs/ai-contract.md).
- JSON Schema/fixtures canonical: [`ai_artifacts/contracts/`](ai_artifacts/contracts/).
- Task và acceptance criteria: [`ai_artifacts/plans/kanban.md`](ai_artifacts/plans/kanban.md); board GitHub là nguồn trạng thái khi truy cập được.

Các contract hiện vẫn là **PROPOSED** cho đến khi A/B/C cùng duyệt. Không xem việc validation pass là bằng chứng contract đã freeze.

## Contract checks cục bộ

Yêu cầu: Python 3.12 và `uv`.

```bash
UV_CACHE_DIR=/tmp/scamlens-uv-cache uv sync --locked --group test
UV_CACHE_DIR=/tmp/scamlens-uv-cache uv run --locked python -m scripts.check_contracts
UV_CACHE_DIR=/tmp/scamlens-uv-cache uv run --locked pytest
UV_CACHE_DIR=/tmp/scamlens-uv-cache uv run --locked python -m scripts.check_docs
```

Script kiểm tra tính hợp lệ của schema, fixtures, negative cases và khả năng tương thích của shared Python types với contract canonical. Không gọi provider và không cần credentials.

## Cấu hình

Sao chép `.env.example` thành `.env` ở máy local rồi thay placeholder bằng secret qua kênh được phê duyệt. Không commit `.env`, key hoặc dữ liệu scan. Các biến hiện chỉ là contract cấu hình; runtime sử dụng chúng thuộc B01/C01.

## Branch và review

- Nhánh tích hợp: `main`.
- Nhánh task: `feat/<Task-ID>` hoặc `fix/<Task-ID>`; ví dụ `feat/B00`.
- Mỗi task có một PR nhỏ, completion report theo template, CI thật và independent review.
- Tác giả không tự approve, merge hoặc deploy. Thay đổi shared contract cần A/B/C duyệt.

## CI hiện tại và lộ trình mở rộng

B00 chỉ chạy contract validation và contract unit tests, không cần paid inference hay production secret. Các task sau mở rộng CI trong chính PR của task đó:

| Task | Check bổ sung sau này |
|---|---|
| A01/A02 | Extension/web lint, unit tests và build |
| B01 | Backend tests, Docker build và local smoke |
| C01 | AI engine unit tests với fake provider injectable |
| B02 | Verification tích hợp thật theo contract |
| Release tasks | Packaging, checksum và deployment verification |

Không có automatic production deployment trong B00.
