# Release / QA / submission checklist
Owner B (integration); A guide/slides, C evaluation/video. All unchecked until real evidence. Dates ICT. P0 release candidate 02/12 18:00; submit 03/12 before 18:00; official hard cutoff 23:59:59.

## Gate G0 27/11
- [ ] B authorizes scope, lane names, request/response + AI port and fixture after compatibility verification across A/B/C lanes in one PR. Confirm registration and send clarification to BTC before 23:59:59 if needed.
- [ ] Provider model/SDK/key, quota, privacy terms and deployment account verified with synthetic test. Record model ID, initial budget and service owner.

## Gate G1 28/11
- [ ] Public health endpoint, Docker build/run from clean checkout, no API key in source/extension.
- [ ] Both clients can render schema fixture; mock banner only dev. Real text + image engine validates outputs. CI green on relevant lanes.

## Gate G2 29/11
- [ ] Chrome clean profile: install release ZIP via Load unpacked, capture synthetic tab, crop, consent, call actual public HTTPS and show valid AI response. Text fallback. Web upload/paste also actual same endpoint, no install required.
- [ ] Check build URL, CORS/permissions, no all_urls, no background capture. Consent reset after changes. No logs containing raw inputs, no storage, no API key in dist or Docker layer.

## Gate G3 30/11
- [ ] Regression tests: high, medium, low, unknown, no evidence, scam-warning benign, prompt injection in text/visual, corrupt image, MIME spoof, oversize, decompression bomb, empty, invalid consent, restricted tabs, active tab switch, rapid duplicate submit, provider refusal/malformed JSON/timeout, network failure, 429, invalid API response. Inspect real network for no upload before consent and crop-only payload. Check no rendered raw HTML/links. All critical pass; no misleading safe claim. Disable P1 if P0 not green.
- [ ] Web on another machine/network, fresh Chrome profile; accessibility focus/labels/keyboard, responsive, visible risk labels. Check timeout and recovery. Review provider data terms and record disclosure.

## Gate G4 01/12–02/12
- [ ] Holdout metrics logged with counts/model/prompt version; record failure cases and limitations; no tuning on same holdout. Verify release-mode real provider, no mock. Pin tested dependency versions. CI lint/tests/build and docker health scan; fix critical failures only.
- [ ] Record final commit/tag (`v0.1-contest`), container digest, extension ZIP checksum, exact public URL, UTC/ICT test time, actual test commands and results. Keep deployment stable; no silent model switch.
- [ ] Independent tester follows one-page PDF only, uses public web + optional extension. Test downloads and public URL without team login/local server. Verify provider and hosting budget/availability through 11/12.

## Submission bundle (to produce, not yet built)
| Deliverable | Owner | Acceptance |
|---|---|---|
| `guide.pdf` | A | ≤1 A4 page; public HTTPS demo URL, optional extension ZIP link, Chrome installation steps, demo sample, data consent, judge token/account if needed |
| `source.zip` | B | complete source incl extension, demo, backend, fixtures, lockfiles, Dockerfile/compose, `.env.example`, README, ai_artifacts; exclude .env, private keys, .git, node_modules, caches, raw scans |
| `slides.pdf` | A (C supplies metrics) | ≤10 pages; no revisions after submission; problem, scope, AI differentiator, user flow, architecture, actual evidence, impact, privacy/limits |
| `demo.mp4` | C | ≤3 min; actual running product; synthetic scenarios only; no API key or personal details |

README source required: exact local run/build/Docker commands, production URL, architecture/AI model/prompt version, external dependencies and versions/licenses, pre-existing assets and OSS libraries, AI coding tools used, datasets sources/rights (synthetic or licensed), personal/company data source/scope/legal basis if any; document no retained app scans, provider processing conditions, limitations. Record claims vs measured evidence. List all pre-existing assets truthfully; original project docs used for process inspiration, not copied code. Check official FAQ for additional requirements before freeze.

### Suggested 8-slide outline
1. Title + one sentence value; 2. Vietnam fintech scam problem & target; 3. User journey & pain point; 4. Live workflow (capture / evidence / action); 5. AI pipeline + privacy; 6. Actual evaluation (baseline vs AI, sample size/limitations); 7. Competition/differentiation & scale/cost; 8. Deployment/roadmap/limits and link.

### 165-second demo script (15s buffer)
0–20s problem and target; 20–65s real Chrome capture fictional risky advertisement/message, preview/crop/consent; 65–100s explain risk evidence and safe next steps; 100–125s benign or ambiguous example, show non-guarantee; 125–150s web demo same API and evaluation actual result; 150–165s privacy and potential impact. No simulated model success or jump cut implying instant response.

## 03/12 handoff and operations
- [ ] A/B/C verify PDF page counts, video duration/format, ZIP contents/reproducibility and all links. Team leader submits on official site before 18:00; save platform receipt/timestamp and final file hashes outside public repo. If resubmitting before cutoff, latest valid submission is the one judged; verify all files again.
- [ ] B monitors cheap /healthz until 11/12; check error/usage counts and budget, no input logs. Keep exact revision and credentials active. Incident: identify issue, restore same revision if permitted; do not change submitted behavior after deadline; consult BTC if unclear. A backup contact can access platform account via approved team process, not shared plaintext secrets.
