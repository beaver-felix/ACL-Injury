# Infrastructure preflight — B00

Observed 27/11/2026 ICT on local Arch Linux workspace. This is readiness evidence, not account approval or deployment evidence. Secret values were neither read nor displayed.

| Area | Status | Observed evidence / limitation | Human next action |
|---|---|---|---|
| Python 3.12 | VERIFIED locally | `python3.12` 3.12.13; default `python` is 3.14.10 | Keep CI/runtime pinned to 3.12 |
| FastAPI / Pydantic v2 | PARTIAL | Pydantic v2 is declared for shared contract types; FastAPI/runtime belongs to B01 | B01 pins and tests runtime dependencies |
| Git / GitHub CLI | PARTIAL | Git 2.56.1; gh 2.106.0; remote configured | Re-authenticate `gh` privately and verify collaborators, board and Actions |
| GitHub Actions | UNVERIFIED externally | Local workflow added for contract checks; no remote run exists | Push/PR only after approval, then inspect run at exact head SHA |
| Docker / Compose | VERIFIED locally | CLI/daemon 29.10.1 and Compose 5.8.0 available; default context responds | B01 adds Dockerfile/Compose and clean build smoke |
| Cloud Run account/project | UNVERIFIED | No account, project, IAM or API evidence inspected | Human confirms project, region, deploy/IAM permission and public-invoker policy |
| Cloud billing/budget | UNVERIFIED | No billing/budget evidence | Human confirms billing account, contest budget, alerts and owner |
| Secret storage | UNVERIFIED | No Secret Manager/project evidence | Human selects secret store and grants least-privilege runtime access; never paste key in chat |
| Gemini vision provider | UNVERIFIED | No key/model call/quota/privacy evidence; C00 owns spike | C verifies supported vision model ID, SDK, terms, retention, quota and six synthetic calls |
| Provider budget/quota through 11/12 | UNVERIFIED | No provider console evidence | Human/C records non-secret quota and budget evidence |
| Alternative deployment | UNAPPROVED | Architecture permits an explicitly approved TLS-capable Docker platform if Cloud Run fails | Team approves only after Cloud Run blocker is evidenced |

No cloud resource, billing setting, secret, provider call, GitHub setting or deployment was created during B00 local work.
