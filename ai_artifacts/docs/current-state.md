# Current State — ScamLens VN
Owner: B | Mục đích: context ngắn cho task tiếp theo. Chỉ ghi sự thật đã kiểm tra; thay nội dung cũ khi baseline thay đổi. Lịch sử nằm trong PR, decision-log, daily-log. Không sao chép toàn bộ Kanban.

Last verified (ICT): 2026-11-28
Integration branch: `main` tại `ad0a6b21fd4843c76a370fe58d0afca9c2eb649d`; working branch `feat/B00`
Verified code SHA: `ad0a6b21fd4843c76a370fe58d0afca9c2eb649d` là baseline; B00 candidate chưa merge
Context updated by: Member B implementation agent, task B00 candidate branch
Contract: API/AI v1 proposed trong bundle Kanban v0.2; local schema/runtime checks pass nhưng chưa có A/C approval hoặc freeze evidence
Repository: `beaver-felix/ACL-Injury` PUBLIC, default branch `main`; GitHub Projects chưa cấu hình theo quyết định của B
Latest gate / verdict / evidence: G0 NOT VERIFIED; mốc 27/11 18:00 đã qua, thiếu approval và account/provider evidence

## Capability baseline
| Surface | State (unverified/fixture/real verified/blocked) | Evidence / PR / SHA | Consumer caveat |
|---|---|---|---|
| Contract schemas/fixtures/shared types | fixture (candidate branch) | B00 checks: validator 4 schemas/5 valid payload views/14 negatives; pytest 11 pass | Chưa CI/peer approval/merge; canonical status vẫn proposed |
| Extension capture/crop/consent | unverified | — | A |
| Extension result + web demo | unverified | — | A |
| FastAPI /healthz, analyze | unverified | — | A/C |
| Engine assess(AnalysisInput) | unverified | — | B |
| Fallback UNKNOWN & safety | unverified | — | A/B |
| Public HTTPS + Docker | unverified | — | A/C |
| Evaluation / holdout | unverified | — | A/B/C |

## Verified interfaces and how to run
- Canonical wire: `api-contracts.md`, `../contracts/`; engine port: `ai-contract.md`; UI: `ui-workflow.md`. Do not duplicate schemas here.
- Actual new/changed canonical interface since last baseline: none. B00 adds compatible Python types only; no JSON Schema was changed.
- Local contract setup/check commands: root `README.md`; executed with Python 3.12 and locked uv environment.
- Public base URL / deployment revision / image digest / tested extension build: TBD.
- Provider/model ID, prompt version, dataset version (no keys): TBD.

## Latest integrated verification
| Command/check | PASS / FAIL / NOT RUN | Tested SHA / revision and link | Limitation |
|---|---|---|---|
| `uv run --locked python -m scripts.check_contracts` | PASS | B00 candidate on baseline `ad0a6b2` | Not a remote CI run or approval |
| `uv run --locked pytest` | PASS (11 tests) | B00 candidate on baseline `ad0a6b2` | Contract runtime tests only |
| `uv run --locked python -m scripts.check_docs` | PASS (8 local links, 21 task IDs) | B00 candidate on baseline `ad0a6b2` | Does not validate external URLs |
| `yamllint .github/workflows/ci.yml` | PASS | B00 candidate on baseline `ad0a6b2` | Generic YAML only; GitHub Actions semantic run NOT RUN |
| GitHub Actions run | NOT RUN | — | Remote result is not recorded in this candidate baseline; inspect the B00 PR |
| Targeted smoke | NOT RUN (no repo evidence) | — | — |
| Real public inference | NOT RUN (no repo evidence) | — | — |

## Active blockers and handoff (only current)
| Affected task | Exact missing input or blocker | Owner / next action | Entry criterion / evidence |
|---|---|---|---|
| B00 / G0 | Contract/schema/port chưa được A và C approve độc lập | A/C review current B00 head; B records evidence | PR approval trên exact head; A/B/C freeze decision |
| B00 / G0 | Cloud project/IAM, billing/budget, secret store chưa được xác minh | Human B verifies consoles without sharing secrets | Non-secret account/project/permission/budget evidence |
| B00 / G0 | Gemini model/key/quota/privacy/retention chưa được C00 xác minh | C completes C00 synthetic provider spike | Model ID/SDK, 6-call results, quota/terms evidence |
| B00 remote evidence | Chưa có independent review hoặc merge evidence trên exact head | A/C review B00 PR; B kiểm tra CI và post-merge | Approval và CI trên cùng head SHA |
| A01/B01/C01 | B00 chưa merge/freeze; A01 còn A00, C01 còn C00 | Owners wait for dependencies | Approved B00 merge SHA plus each lane dependency |

## Constraints & approved deviations
- P0 scope per product brief and backlog; no automatic browsing/sending scans, no raw input retention, no fake AI success; UNKNOWN fallback never LOW.
- Approved deviations: none recorded; see `decision-log.md`.
- Known limitations/mock boundaries: TBD from actual evidence (do not infer implemented from planned contract).
- Next ready work: independent B00 review và external readiness verification. Không dispatch A01/B01/C01 chỉ dựa trên thay đổi local này.
