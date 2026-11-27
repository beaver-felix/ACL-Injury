# Kanban delivery plan — 3 members
27/11–03/12/2026 ICT • 5 core build days (28/11–02/12), 27/11 half-day kickoff, 03/12 submission buffer. Dates are target windows, not strict Scrum sprints. Estimate focus hours, not clock time; 5h/member/day + 1–2h review/integration/buffer. Actual availability unknown; adjust at kickoff. All planned tasks are P0. Board initially seeded from CSV; no real work completed.

## Ownership and cadence
A — Extension & Web UX; guide/slides. B — API, Docker/deployment, integration, submission coordination. C — AI engine, security-aware assessment/evaluation, demo video. Team leader identity not supplied; B coordinates submission but registered leader submits. A reviews C outputs/UX, C reviews B security/AI integration, B reviews A API/permissions. Each member supplies dependencies/license/AI tools declaration. 

Board columns: Backlog → Ready → In progress → Review/Test → Done; Blocked flag with owner + exact dependency (counts as WIP; if truly blocked park in Backlog and pull highest ready). WIP: max 1 implementation card/member, max 2 cards team in Review/Test; unblock reviews before pulling new work. Ready = dependencies merged or explicitly approved frozen fixture, AC + ownership clear. Done = AC proven, tests run or honestly reported, PR reviewed/merged, docs updated, real evidence linked. Mock permitted during lane work, not final P0 gate. No task marked done based solely on AI's assertion. Daily 09:00 10-min sync; 19:00 gate/handoff; 27/11 18:00 contract freeze; 03/12 final submit by 18:00. Short-lived feat/A01 etc from main; B merges shared contract first, then lane PRs; reviewers not allowed to silently edit other lanes. All times proposed ICT.

## Cards by lane
Each date is in 2026; dependencies denote start/finish prerequisites, except frozen fixture allows parallel A/C work. Read actual board for status after import. Hours exclude review/buffer.

### Member A

| ID | Date | h | Depends | Deliverable | Acceptance criteria |
|---|---|---:|---|---|---|
| A00 | 27/11 | 2 | - | Chốt UX/scope và đề | Product scope, wireframe states; xác nhận flow/FAQ với B/C |
| A01 | 28/11 | 5 | A00;B00 | Extension capture + preview | MV3 action, activeTab, HTTP(S) capture/crop/consent, paste fallback; không gửi ngầm |
| A02 | 29/11 | 5 | A01;B00 | Extension result + web demo | Same adapter; web upload/paste/fixture, both render all enums/errors, consent |
| A03 | 30/11 | 5 | A02;B02 | External UI E2E and polish | Fresh Chrome, public web, capture consent network check, states keyboard/mobile web |
| A04 | 01/12 | 5 | A03;B03 | Demo UX & slide/guide drafts | Guide URL/steps, 8 slide outline, fixture flows; fix P0 UI only |
| A05 | 02/12 | 5 | A04;C04;B04 | Finalize guide/slides + UI freeze | A4 1 page, slide PDF ≤10 pages with actual metrics, reviewed public URL |
| A06 | 03/12 | 2 | A05;B05 | Independent guide test | Guide-only fresh machine test, confirm PDF pages/links, sign off |

### Member B

| ID | Date | h | Depends | Deliverable | Acceptance criteria |
|---|---|---:|---|---|---|
| B00 | 27/11 | 3 | - | Contract freeze + repo/infra spike | Schema/fixture và port được 3 người duyệt; repo CI skeleton, public account/billing |
| B01 | 28/11 | 5 | B00 | FastAPI + Docker + public health | Docker clean build, GET health public HTTPS, validation/fixture local, CI smoke |
| B02 | 29/11 | 5 | B01;C01 | Real analyze integration | Wire provider, body/image validation, timeout, no-store; deploy real end-to-end |
| B03 | 30/11 | 5 | B02 | Security + integration gate | Rate/concurrency, no logs, invalid/oversize, 429/timeouts, production rejects mock; all P0 smoke |
| B04 | 01/12 | 5 | B03;A03;C03 | Release hardening + README | Clean build/CI, download extension with final API host, actual external smoke and README declarations |
| B05 | 02/12 | 5 | B04;C04;A04 | Freeze release and source ZIP | Tagged tested commit + image digest, ZIP checksum, README, clean unzip/run; retain hosting |
| B06 | 03/12 | 3 | A05;B05;C05;A06;C06 | Final submission & runbook | Leader submits all files before 18:00 ICT; capture receipt, hashes, maintain to 11/12 |

### Member C

| ID | Date | h | Depends | Deliverable | Acceptance criteria |
|---|---|---:|---|---|---|
| C00 | 27/11 | 3 | - | Model/provider spike | 3 text + 3 ảnh synthetic; pin model ID, quota/privacy/latency, structured JSON |
| C01 | 28/11 | 5 | B00;C00 | Vision engine + schema | Text/image inference; prompt injection isolation, valid assessment and unit mock |
| C02 | 29/11 | 5 | C01 | Fallback & dev fixture set | UNKNOWN fallback, safe actions, 12 dev fixtures + lexical baseline; record real test |
| C03 | 30/11 | 5 | C02;B02 | Adversarial QA + holdout lock | 30 labeled cases stratified dev/holdout; independent labels, adversarial failures, prompt freeze |
| C04 | 01/12 | 5 | C03 | Holdout evaluation + claims | AI vs baseline same holdout, counts/precision/recall/FP/unknown/latency; limitations evidence |
| C05 | 02/12 | 5 | C04;B04;A04 | Record final demo MP4 | ≤3 min running real release candidate; no personal data; actual results/limitations |
| C06 | 03/12 | 2 | C05;B05 | Final AI/video verification | Validate MP4 duration, live AI text/image, model/quota until 11/12, sign off |

## Integration checkpoints
| Gate | When | Hard stop / decision |
|---|---|---|
| G0 | 27/11 18:00 | Freeze API+AI port, provider/key and deployment verified; if not, escalate that evening |
| G1 | 28/11 evening | public health, frontend fixture + real engine works separately |
| G2 | 29/11 evening | live public screenshot/text scan from both clients; no further feature breadth until pass |
| G3 | 30/11 evening | safety/error/privacy tests green, holdout locked; cut P1 if any P0 blocker |
| G4 | 01/12 evaluation, 02/12 18:00 freeze | evidence, build, URL, bundle, exact revision; only critical fix before re-test |
| G5 | 03/12 18:00 | clean external verification and receipt (actual official cutoff 23:59:59) |

Critical path: B00 → B01 + C01 → B02 → B03 → B04 → B05 → B06. A01/A02 run using frozen fixture while backend builds; C02/03 overlap integration. C04 feeds slides/video. No P1 until G3 accepted. If 29/11 live slice blocked, cut crop sophistication and optional metadata, use simple paste+upload and basic crop; retain real screenshot AI and public web (P0), reduce visual polish. If provider unavailable, switch approved provider by 28/11 or report blocker; UNKNOWN fallback is not acceptable as sole demo. If slide/video at risk freeze features sooner. No fake results.

Optional backlog (not scheduled, no promised hours): P1-01 URL reputation (B/C, terms check); P1-02 local QR decode inert display (A); P1-03 optional crop polish (A); P1-04 more evaluation scenarios (C). Pull only if every P0 gate on track and owners agree; defer by default.
