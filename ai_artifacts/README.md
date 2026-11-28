# ScamLens VN — AI artifacts

Bộ contract khởi tạo cho MoMo Tech Contest 2026 • v0.1 PROPOSED • 27/11/2026 (ICT UTC+7). Tên sản phẩm tạm, không phải sản phẩm chính thức của MoMo. Tất cả task chưa thực hiện.

## Start here
1. Mỗi coding session bắt đầu từ root `AGENTS.md`, sau đó theo read order trong file đó; đọc `docs/current-state.md` trước card và contract liên quan.
2. Cả nhóm đọc `docs/product-brief.md`, `prompts/Agent_Prompt.md`, `plans/kanban.md`.
3. Gán tên thật cho A/B/C; chốt contract v1 (A/B/C cùng duyệt) trước 18:00 ICT ngày 27/11.
4. Đọc `docs/architecture-alignment.md`, `docs/api-contracts.md`, `docs/ai-contract.md`, `docs/ui-workflow.md` và `skeletons/README.md` theo lane.
5. Chuyển các card ở `plans/kanban.csv` vào GitHub Projects (hoặc Trello/Notion). CSV chỉ là dữ liệu import/seed; board là nguồn trạng thái sau khi import. Không duy trì hai board.
6. Mỗi tối cập nhật `sprints/daily-log.md` bằng kết quả thật; ngày 02/12 freeze bản dự thi; 03/12 nộp trước 18:00.

## Artifact map (single source of truth)
| Path | Nội dung | Chủ trì |
|---|---|---|
| docs/product-brief.md | Đề thi, scope, giá trị và tiêu chí | A |
| docs/architecture-alignment.md | Hệ thống, security, deployment | B |
| docs/api-contracts.md + contracts/ | Wire protocol + schema + fixture | B, A/C duyệt |
| docs/ai-contract.md | AI provider port, rules, prompt, đánh giá | C |
| docs/ui-workflow.md | UI states, component contract | A |
| docs/release-checklist.md | QA, demo, submission, runbook | B phối hợp A/C |
| docs/infrastructure-preflight.md | Readiness evidence và human actions cho B00 | B |
| plans/kanban.md + kanban.csv | Owner, card, phụ thuộc, AC | B điều phối, mỗi owner cập nhật board |
| prompts/Agent_Prompt.md | Quy tắc làm việc với AI | Cả nhóm |
| docs/current-state.md | Baseline hệ thống mới nhất đã kiểm chứng | B |
| docs/integration-workflow.md + docs/decision-log.md | Quy trình integration và quyết định cross-lane | B |
| skeletons/README.md | File ownership map, không phải runtime code | B |
| sprints/daily-log.md | Daily review/handoff | Cả nhóm |
| research/stack-and-market.md | Stack, competitor, nguồn tham khảo | C |
| research/reference-audit.md | Đối chiếu dự án mẫu, giới hạn nguồn | Cả nhóm |

Bộ này không phải mã nguồn sản phẩm hoặc kết quả test. Các ngưỡng hiệu năng là mục tiêu, không phải số liệu thực nghiệm. Không đưa dữ liệu thật/API key vào Git, prompt AI hoặc demo.
