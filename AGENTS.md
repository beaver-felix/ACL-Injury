# Repository agent contract

Mỗi session phải có đúng một Member ID (`A`, `B` hoặc `C`), một Task ID và một mode. Dừng sau task được giao; không tự mở rộng sang card kế tiếp.

## Mandatory read order

1. `AGENTS.md`.
2. `ai_artifacts/prompts/Agent_Prompt.md`.
3. `ai_artifacts/docs/current-state.md`.
4. `ai_artifacts/docs/integration-workflow.md`.
5. Card được giao trong `ai_artifacts/plans/kanban.md` và trạng thái board live nếu truy cập được.
6. Ownership map trong `ai_artifacts/skeletons/README.md`, dependency evidence và technical contracts liên quan.

Trước khi làm: đọc baseline repository thật, kiểm tra dependency/commit/PR và nêu blocker. Không suy diễn capability từ kế hoạch.

## Execution modes

- `IMPLEMENTATION`: chỉ thay đổi code/docs thuộc task và ownership được giao.
- `REVIEW`: read-only; trả findings, evidence và verdict đề xuất, không sửa/approve/merge.
- `CONTEXT MAINTENANCE`: chỉ cập nhật context/docs từ thay đổi đã merge và được kiểm chứng.

## Mandatory rules

- Tôn trọng file ownership; không sửa lane khác nếu chưa có authorization rõ ràng từ Member B.
- Không âm thầm đổi shared contract. Báo drift; contract change cần B quyết định sau khi verify compatibility với mọi producer/consumer bị ảnh hưởng và cập nhật đồng bộ canonical docs/schema/fixtures/tests.
- Chỉ dùng synthetic data; không đưa secret, PII, raw scan hoặc live scam URL vào code, log, prompt hay artifact.
- Chạy check liên quan và báo lệnh/kết quả thật bằng PASS, FAIL, NOT RUN hoặc BLOCKED.
- GitHub Issues/Projects là trạng thái live; PR là execution evidence; `current-state.md` là verified baseline; không tạo tracker trùng lặp.
- Kết thúc bằng Task Completion Report theo `.github/pull_request_template.md`, gồm limitation và downstream handoff.
- AI agent không tự approve, merge, deploy hoặc thay đổi GitHub/cloud settings; chỉ push khi human cho phép rõ ràng. Member B là reviewer và integration decision-maker. PR do B implement phải có review session AI read-only tách biệt và evidence checks; không gọi đó là independent human approval.
