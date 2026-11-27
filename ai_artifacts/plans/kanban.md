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


---

# Kanban chi tiết — ScamLens VN

**Version 0.2 (proposed) | 27/11–03/12/2026 ICT | 21 P0 cards | 90 giờ focus tổng cộng**

Bản mở rộng của kế hoạch v0.1; giữ nguyên ID, owner, priority, thời lượng, ngày, dependency và trạng thái seed. Checklist là hướng dẫn triển khai đề xuất, chưa phải công việc đã làm. Tất cả checkbox bắt đầu chưa tick. Nếu contract/board khác card, báo B và thống nhất trước khi sửa. Các đường dẫn `docs/`, `contracts/`, `skeletons/` trong Required reading tương đối từ `ai_artifacts/`; các đường dẫn chỉnh sửa code tính từ root repo.

## Cách sử dụng
- Bản Kanban gốc `plans/kanban.md` là overview lịch và dependency; phần card dưới đây bổ sung chi tiết, không tạo board thứ hai. Nếu dùng bản ZIP v0.2, overview và card đã được ghép vào cùng `plans/kanban.md`. CSV là seed/export để import hoặc copy vào issue; live board giữ trạng thái thật. Không đánh dấu Done trực tiếp ở nhiều nơi.
- Mỗi card có Implementation checklist, Testing checklist và Deliverable/handoff. Đây là subtasks, không tách 21 card thành hàng trăm issues. Checklists không thay thế acceptance criteria gốc.
- Estimate là giờ tập trung của owner; checklist không tăng ngân sách giờ một cách ngầm định. Nếu hết timebox, báo Blocked hoặc cắt polish/P1; không bỏ safety/real AI/public demo. Review/integration buffer ngoài estimate.
- Ready khi dependency đã merge hoặc có frozen fixture được duyệt; ghi rõ dependency PR. A02 có thể chạy fixture song song B02 nhưng G2 bắt buộc cả hai tích hợp AI thật. B05/A05/C05 phối hợp cùng revision, không đợi đến cuối ngày mới chốt.
- WIP 1 card/member, Review/Test tối đa 2 card/team; reviewer ghi actual evidence và không sửa lane khác. Daily sync 09:00, gate 19:00 (G0/G4/G5 theo mốc riêng trong overview); cập nhật `sprints/daily-log.md`.

## Definition of Done chung
- [ ] Đọc Agent_Prompt, contract và file ownership; chỉ sửa phạm vi được giao, báo mọi cross-lane change.
- [ ] Acceptance criteria gốc và checklist card có evidence; ghi command + kết quả thật (pass/fail/not run) và lý do nếu chưa chạy.
- [ ] Lint/test/build liên quan đã chạy; synthetic data; không secret/PII, không log raw input; không mock giả làm thật.
- [ ] PR nhỏ `feat/<ID>` được reviewer duyệt/merge; cập nhật doc liên quan nếu có thay đổi đã duyệt.
- [ ] Link PR/commit, artifacts, blockers, next handoff trong issue và daily log. Không Done nếu P0 acceptance chưa đạt.

## Task assignment prompt

```text
Bạn là Member [A|B|C], thực hiện task [ID].
Đọc ai_artifacts/prompts/Agent_Prompt.md, plans/kanban.md và card [ID].
Đọc các contract và skeleton được liệt kê trong card; kiểm tra repo trước khi sửa.
Chỉ chỉnh sửa allowed paths; không đổi API/schema/dependency chung nếu chưa được duyệt.
Thực hiện checklist, chạy test liên quan; không tạo mock thành công giả hoặc đưa secrets/PII vào code/log.
Báo blocker, owner và interface nếu cần đổi lane. Dừng khi hoàn thành AC hoặc bị blocked.
Trả về: task ID, files, commands + actual results, evidence, PR, known limitations, handoff.
```

## Card index

| ID | Owner | Ngày | Giờ | Task | Dependency |
|---|---|---|---:|---|---|
| [A00](#a00) | A | 27/11 | 2 | Chốt UX/scope và đề | - |
| [B00](#b00) | B | 27/11 | 3 | Contract freeze + repo/infra spike | - |
| [C00](#c00) | C | 27/11 | 3 | Model/provider spike | - |
| [A01](#a01) | A | 28/11 | 5 | Extension capture + preview | A00;B00 |
| [B01](#b01) | B | 28/11 | 5 | FastAPI + Docker + public health | B00 |
| [C01](#c01) | C | 28/11 | 5 | Vision engine + schema | B00;C00 |
| [A02](#a02) | A | 29/11 | 5 | Extension result + web demo | A01;B00 |
| [B02](#b02) | B | 29/11 | 5 | Real analyze integration | B01;C01 |
| [C02](#c02) | C | 29/11 | 5 | Fallback & dev fixture set | C01 |
| [A03](#a03) | A | 30/11 | 5 | External UI E2E and polish | A02;B02 |
| [B03](#b03) | B | 30/11 | 5 | Security + integration gate | B02 |
| [C03](#c03) | C | 30/11 | 5 | Adversarial QA + holdout lock | C02;B02 |
| [A04](#a04) | A | 01/12 | 5 | Demo UX & slide/guide drafts | A03;B03 |
| [B04](#b04) | B | 01/12 | 5 | Release hardening + README | B03;A03;C03 |
| [C04](#c04) | C | 01/12 | 5 | Holdout evaluation + claims | C03 |
| [A05](#a05) | A | 02/12 | 5 | Finalize guide/slides + UI freeze | A04;C04;B04 |
| [B05](#b05) | B | 02/12 | 5 | Freeze release and source ZIP | B04;C04;A04 |
| [C05](#c05) | C | 02/12 | 5 | Record final demo MP4 | C04;B04;A04 |
| [A06](#a06) | A | 03/12 | 2 | Independent guide test | A05;B05 |
| [B06](#b06) | B | 03/12 | 3 | Final submission & runbook | A05;B05;C05;A06;C06 |
| [C06](#c06) | C | 03/12 | 2 | Final AI/video verification | C05;B05 |


## Member A — Frontend & Product UX (29h)

<a id="a00"></a>

### A00 — Chốt UX/scope và đề

**Owner:** A | **Priority:** P0 | **Ngày:** 27/11/2026 ICT | **Estimate:** 2h | **Dependency:** - | **Seed:** Ready

**Mục tiêu / mô tả:** Chốt trải nghiệm, mục tiêu MVP và luồng minh họa để A/B/C không hiểu khác nhau về sản phẩm.

**Required reading:** docs/product-brief.md; docs/ui-workflow.md; docs/release-checklist.md.

**File ownership:** docs/product-brief.md, docs/ui-workflow.md (phần UX), ghi chú thiết kế của A.

**Implementation checklist:**
- [ ] Đối chiếu đề/FAQ, ghi câu hỏi chưa rõ về extension Load unpacked, public web, giới hạn model để B gửi BTC nếu cần.
- [ ] Chốt một journey: mở tab HTTP(S) → chụp viewport → xem/cắt ảnh → consent → phân tích → kết quả → reset; thêm luồng paste text và web upload.
- [ ] Phác wireframe 5 trạng thái idle/review/analyzing/result/error, nội dung tiếng Việt, 4 risk labels, no-safe-guarantee.
- [ ] Chọn 3 tình huống mẫu giả lập (đáng nghi, bình thường, mơ hồ); thống nhất với C, không dùng thông tin người thật.
- [ ] Xác nhận P0/P1/out of scope với B/C và ghi các quyết định còn chờ vào daily-log.

**Acceptance criteria (gốc):** Product scope, wireframe states; xác nhận flow/FAQ với B/C

**Testing checklist:**
- [ ] Walkthrough cả hai client với B/C; kiểm tra mỗi trạng thái có hành động kế tiếp và thông báo lỗi.
- [ ] Review wording consent, UNKNOWN/LOW; kiểm tra mock không được trình bày như AI thật.

**Expected deliverables & handoff:** Wireframe hoặc mô tả trạng thái đã duyệt; danh sách câu hỏi BTC; 3 mô tả fixture; scope sign-off. B00 nhận flow và ràng buộc; C00 nhận tình huống.

**Reviewer:** B (C góp ý tình huống/AI)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="a01"></a>

### A01 — Extension capture + preview

**Owner:** A | **Priority:** P0 | **Ngày:** 28/11/2026 ICT | **Estimate:** 5h | **Dependency:** A00;B00 | **Seed:** Backlog

**Mục tiêu / mô tả:** Xây Extension MV3 chạy được trên Chrome, thu đúng dữ liệu mà người dùng chủ động chọn, chưa phụ thuộc API thật.

**Required reading:** docs/ui-workflow.md; docs/architecture-alignment.md (capture); contracts/request.schema.json.

**File ownership:** extension/**; extension lockfile và test của A.

**Implementation checklist:**
- [ ] Khởi tạo WXT + React + TypeScript; manifest MV3, activeTab, host permission API chính xác (localhost chỉ dev), không all_urls/tabs/scripting/background capture.
- [ ] Tạo popup hoặc review tab theo contract; captureVisibleTab chỉ khi người dùng bấm, kiểm tra tab/window trước và sau; chỉ HTTP(S), loại restricted/incognito.
- [ ] Hiển thị ảnh preview trong memory; crop bằng Canvas; export PNG/JPEG ≤2 MiB, max 2048px mỗi chiều/4M pixel; hiển thị đúng ảnh sau crop.
- [ ] Tạo textarea ≤6000 ký tự, clear/reset và paste fallback; page_host optional chỉ hostname và phải được duyệt, không path/query.
- [ ] Consent mặc định false; mọi thay đổi ảnh/text/host reset consent; không upload trước xác nhận; bỏ preview khi đóng popup.
- [ ] Tạo payload đúng request schema (raw base64, không data URI); mock fixture có banner dev, không tự gọi mạng.

**Acceptance criteria (gốc):** MV3 action, activeTab, HTTP(S) capture/crop/consent, paste fallback; không gửi ngầm

**Testing checklist:**
- [ ] Build và Load unpacked fresh Chrome; thử tab HTTP(S), chrome://, tab switch, ảnh crop, đóng popup, text-only, blank, ảnh vượt giới hạn.
- [ ] DevTools Network: không request trước consent; payload crop-only; kiểm tra manifest dist không có quyền dư.

**Expected deliverables & handoff:** Extension dev build, ảnh/video ngắn capture→preview→consent, manifest và test evidence; A02 nhận ScanForm và payload builder.

**Reviewer:** B

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="a02"></a>

### A02 — Extension result + web demo

**Owner:** A | **Priority:** P0 | **Ngày:** 29/11/2026 ICT | **Estimate:** 5h | **Dependency:** A01;B00 | **Seed:** Backlog

**Mục tiêu / mô tả:** Hoàn thiện Result UI và web demo dùng cùng wire contract với Extension; tách state xử lý mạng khỏi component hiển thị.

**Required reading:** docs/ui-workflow.md; docs/api-contracts.md; contracts/example-response.json; contracts/error.schema.json.

**File ownership:** extension/**, demo/** và test/lockfile tương ứng.

**Implementation checklist:**
- [ ] Tạo apiClient.analyze(payload, signal) với base URL build-time VITE_API_BASE_URL cho extension, relative path cho web; runtime validate response/error, timeout 30s, không auto-retry.
- [ ] Xây state machine idle/review/analyzing/result/error; disable submit trong analyzing, abort về review, bỏ late response theo request sequence.
- [ ] Render RiskBadge, EvidenceList, ActionList, Limitations; phân biệt AI/RULE_FALLBACK, LOW/UNKNOWN, không tính lại risk ở client.
- [ ] Web /: upload PNG/JPEG hoặc paste, preview/crop nếu cần, 3 synthetic sample lựa chọn, consent như extension; không tự gửi sample khi chọn.
- [ ] Map 400/413/415/429/503/500 sang VN, 429 đọc Retry-After; lỗi network/timeout/invalid JSON có manual retry, không hiện lỗi upstream.
- [ ] Build cả hai client; dùng fixture trước, phối hợp B02 để chuyển API public thật trước G2 (29/11 tối).

**Acceptance criteria (gốc):** Same adapter; web upload/paste/fixture, both render all enums/errors, consent

**Testing checklist:**
- [ ] Test fixture đủ bốn risk level, fallback, zero/long signals hợp lệ, malicious HTML hiển thị text inert; click đúp, timeout, cancel, stale response, 429.
- [ ] Thử text và screenshot từ Extension và web tới public endpoint sau khi B02 ready; lưu request ID không kèm dữ liệu thật.

**Expected deliverables & handoff:** Web dist, extension dist, test report, screenshot các state; B02 nhận build/artifact paths và API integration status.

**Reviewer:** B

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="a03"></a>

### A03 — External UI E2E and polish

**Owner:** A | **Priority:** P0 | **Ngày:** 30/11/2026 ICT | **Estimate:** 5h | **Dependency:** A02;B02 | **Seed:** Backlog

**Mục tiêu / mô tả:** Kiểm thử end-to-end trên môi trường ngoài máy dev và sửa lỗi UI P0, không mở thêm tính năng.

**Required reading:** docs/ui-workflow.md; docs/release-checklist.md G2/G3; docs/api-contracts.md.

**File ownership:** extension/**, demo/**, UI tests của A; không sửa backend.

**Implementation checklist:**
- [ ] Cài ZIP release từ public URL trên Chrome profile sạch; đối chiếu permissions và backend origin, thử capture synthetic page.
- [ ] Kiểm tra web trên máy/network khác, text-only, upload PNG/JPEG, sample, consent, reset; chạy cả screenshot flow.
- [ ] Dùng DevTools xác minh consent trước network, crop-only, no-store, không raw HTML/link clickable, không API key trong bundle.
- [ ] Kiểm tra lỗi tab restricted/tab switch, invalid input, unsupported image, timeout, 429 và offline; thử quay lại review/reset.
- [ ] Kiểm tra keyboard Tab/Enter, visible focus, label, aria-live; viewport web 320px+, popup 360–400px scroll; nội dung Việt dài không tràn.
- [ ] Ghi bugs P0 theo request ID/commit, tái hiện bằng fixture; báo B/C lỗi cross-lane thay vì sửa hộ.

**Acceptance criteria (gốc):** Fresh Chrome, public web, capture consent network check, states keyboard/mobile web

**Testing checklist:**
- [ ] Chạy test/lint/build theo script thực tế; lặp smoke sau fix; kiểm tra no false-safe UI với LOW/UNKNOWN.
- [ ] Đối chiếu cả hai client gọi AI thật, lỗi fallback không mang badge AI.

**Expected deliverables & handoff:** Bảng pass/fail + screenshots synthetic, danh sách blocker và PR fixes; B03/B04 nhận kết quả external smoke; A04 nhận UI đã ổn định.

**Reviewer:** B

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="a04"></a>

### A04 — Demo UX & slide/guide drafts

**Owner:** A | **Priority:** P0 | **Ngày:** 01/12/2026 ICT | **Estimate:** 5h | **Dependency:** A03;B03 | **Seed:** Backlog

**Mục tiêu / mô tả:** Chuẩn bị câu chuyện sản phẩm và tài liệu ban giám khảo trong khi giữ UI ổn định.

**Required reading:** docs/product-brief.md; docs/release-checklist.md; kết quả A03/B03.

**File ownership:** submission/guide, submission/slides và UI P0 trong extension/**, demo/**.

**Implementation checklist:**
- [ ] Chọn demo journey với C: risky capture → evidence/action, benign hoặc ambiguous → caution, public web cùng API.
- [ ] Viết guide draft 1 trang A4: link HTTPS, 3 bước thử web, tải ZIP/Load unpacked tùy chọn, consent, giới hạn, hỗ trợ nếu cần.
- [ ] Lập slide outline khoảng 8 trang: problem, target, workflow, AI, architecture, evaluation, differentiation/impact, deployment/limits.
- [ ] Xin B public URL ổn định, C model/prompt version và bảng số liệu dự kiến; chỉ để placeholder ghi rõ chưa đo trước C04.
- [ ] Kiểm tra text UI demo, sửa lỗi P0 đã ghi nhận; không thêm animations, dashboard hay history.

**Acceptance criteria (gốc):** Guide URL/steps, 8 slide outline, fixture flows; fix P0 UI only

**Testing checklist:**
- [ ] Đọc thử guide với thành viên không làm frontend; xác minh hướng dẫn không cần API key/local server.
- [ ] Review slide claims: không khẳng định an toàn tuyệt đối, không đưa số liệu giả hay logo hàm ý MoMo chứng thực.

**Expected deliverables & handoff:** Guide draft, slide outline, demo flow có timestamp gợi ý, URL đã xác nhận; B04/C05 nhận luồng demo và asset; A05 chờ C04 metrics.

**Reviewer:** B (C duyệt AI claims)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="a05"></a>

### A05 — Finalize guide/slides + UI freeze

**Owner:** A | **Priority:** P0 | **Ngày:** 02/12/2026 ICT | **Estimate:** 5h | **Dependency:** A04;C04;B04 | **Seed:** Backlog

**Mục tiêu / mô tả:** Xuất guide và slide PDF cuối cùng theo đúng giới hạn nộp, đồng bộ với release candidate và kết quả đánh giá thật.

**Required reading:** docs/release-checklist.md; A04 draft; C04 evaluation; B04 release info.

**File ownership:** submission/guide.pdf, submission/slides.pdf và nguồn thiết kế của A.

**Implementation checklist:**
- [ ] Điền đúng public URL, link download extension, bước sử dụng và privacy disclosure; loại mọi placeholder.
- [ ] Điền số liệu C04 với raw counts, holdout n, model/prompt version, baseline, limitations; không suy rộng giảm thiệt hại.
- [ ] Chốt nội dung 8 slide (tối đa 10 trang) và guide tối đa 1 A4; link đọc được và click được nếu công cụ xuất hỗ trợ.
- [ ] Kiểm tra fonts tiếng Việt, khoảng trắng, bố cục, contrast; ghi version theo commit/release B05.
- [ ] Gửi B/C review các claims và URL; freeze UI, chỉ critical fix qua B và re-test.

**Acceptance criteria (gốc):** A4 1 page, slide PDF ≤10 pages with actual metrics, reviewed public URL

**Testing checklist:**
- [ ] Mở PDF bằng trình đọc khác, kiểm tra page count, kích thước A4 guide, chữ không bị cắt, URL hoạt động.
- [ ] Đối chiếu metrics với evaluation report và phiên bản release; không dùng screenshot chứa PII.

**Expected deliverables & handoff:** 2 PDF final + sign-off + version; B06 nhận file/hashes để nộp; A06 dùng guide thực tế để kiểm tra độc lập.

**Reviewer:** B (C duyệt số liệu)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="a06"></a>

### A06 — Independent guide test

**Owner:** A | **Priority:** P0 | **Ngày:** 03/12/2026 ICT | **Estimate:** 2h | **Dependency:** A05;B05 | **Seed:** Backlog

**Mục tiêu / mô tả:** Xác minh giám khảo có thể tự dùng sản phẩm chỉ dựa trên tài liệu đã nộp dự kiến.

**Required reading:** submission/guide.pdf; submission/slides.pdf; docs/release-checklist.md G5; B05 release record.

**File ownership:** báo cáo QA của A; tài liệu chỉ nếu phát hiện lỗi trước nộp và B điều phối.

**Implementation checklist:**
- [ ] Dùng trình duyệt/máy khác, không đăng nhập tài khoản nhóm và không chạy server local; làm theo guide từng bước.
- [ ] Mở public web, chọn fixture, consent, gửi scan; tải và Load unpacked ZIP theo đúng hướng dẫn tùy chọn.
- [ ] Thử capture synthetic tab và paste text; xác nhận đúng risk/evidence/limitations và AI thật.
- [ ] Kiểm tra lại số trang PDF, link, tên file, checksum so với bản B05; ghi lỗi nếu có.

**Acceptance criteria (gốc):** Guide-only fresh machine test, confirm PDF pages/links, sign off

**Testing checklist:**
- [ ] Người kiểm thử không được dùng hướng dẫn miệng; ghi thời gian ICT, browser, commit, pass/fail và request ID đã ẩn dữ liệu.
- [ ] Nếu không truy cập được hoặc không dùng được, đánh dấu Blocked và báo B06 ngay; không sign-off giả.

**Expected deliverables & handoff:** Independent guide-test report và sign-off (hoặc blocker) cho B06.

**Reviewer:** B

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---


## Member B — Backend & DevOps (31h)

<a id="b00"></a>

### B00 — Contract freeze + repo/infra spike

**Owner:** B | **Priority:** P0 | **Ngày:** 27/11/2026 ICT | **Estimate:** 3h | **Dependency:** - | **Seed:** Ready

**Mục tiêu / mô tả:** Freeze ranh giới giữa ba lane, chuẩn bị repo và dịch vụ deploy để cả nhóm triển khai song song ngay hôm nay.

**Required reading:** docs/architecture-alignment.md; docs/api-contracts.md; docs/ai-contract.md; contracts/; skeletons/README.md.

**File ownership:** contracts, backend/app/contracts.py nếu khởi tạo, root config/README, .github/workflows/**; A/C duyệt schema.

**Implementation checklist:**
- [ ] Khởi tạo Git repo, main, .gitignore (.env, node_modules, caches, scans), PR template, CI skeleton; mời A/C và phân branch feat/<ID>.
- [ ] Review JSON Schema và fixtures: source/consent/text/image/page_host; risk/category/mode; error envelope; semantic invariants trong API doc.
- [ ] Chốt AnalysisInput, ModelAssessment, EngineResult, async assess port; B sở hữu transport metadata, C sở hữu inference; A render-only.
- [ ] Kiểm thử schema với example request/response/error; thống nhất dùng ai_artifacts/contracts làm nguồn canonical, không tạo bản copy lệch.
- [ ] Xác minh account cloud/billing, quyền deploy, ngân sách/secret store và phương án dự phòng; phối hợp C00 provider key/quota; không chia sẻ secret qua Git.
- [ ] Chốt owner, review và timestamp freeze với cả 3; xác nhận FAQ/deadline và gửi câu hỏi BTC nếu cần trước hạn.

**Acceptance criteria (gốc):** Schema/fixture và port được 3 người duyệt; repo CI skeleton, public account/billing

**Testing checklist:**
- [ ] Schema/examples hợp lệ, repo access A/B/C, CI skeleton chạy hoặc ghi blocker; xác nhận provider/cloud với bằng chứng không lộ key.
- [ ] A/C đọc và đồng ý field names, limits, error semantics, port trước khi merge.

**Expected deliverables & handoff:** PR contract freeze G0, commit SHA, infra decision, `.env.example` placeholders nếu có; A01/C01/B01 nhận frozen interface.

**Reviewer:** C (A đồng duyệt contract)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="b01"></a>

### B01 — FastAPI + Docker + public health

**Owner:** B | **Priority:** P0 | **Ngày:** 28/11/2026 ICT | **Estimate:** 5h | **Dependency:** B00 | **Seed:** Backlog

**Mục tiêu / mô tả:** Tạo FastAPI service một container, validation API cơ bản và endpoint health public để không trì hoãn deployment.

**Required reading:** docs/architecture-alignment.md; docs/api-contracts.md; contracts/; skeletons/README.md.

**File ownership:** backend/app/main.py, contracts.py, routes/**, security/**, tests/api/**, Dockerfile, requirements*, compose.yaml, .env.example, CI.

**Implementation checklist:**
- [ ] Tạo FastAPI/Pydantic v2 models đúng schema, GET /healthz trả status/version không gọi model, POST /api/v1/analyze với explicit dev fixture stub.
- [ ] Tạo error handler VN đúng envelope và no-store; reject thiếu consent, blank text/image, extra fields; full image checks B02.
- [ ] Cấu hình Uvicorn 0.0.0.0:$PORT, một worker, non-root Docker, pin dependencies, compose; .env.example chỉ placeholders.
- [ ] Mount điểm phục vụ web dist và extension ZIP theo contract; chưa có dist thì ghi rõ dependency, không tạo demo fake; hỗ trợ CI build khi dist sẵn.
- [ ] Deploy public HTTPS health trên Cloud Run hoặc nền tảng đã duyệt; secret server-side; kiểm tra access anonymous bounded demo, release không chấp nhận mock mode.
- [ ] Thêm pytest/httpx smoke + schema fixture validation; thông báo URL ổn định A/C, ghi lệnh build/run thật.

**Acceptance criteria (gốc):** Docker clean build, GET health public HTTPS, validation/fixture local, CI smoke

**Testing checklist:**
- [ ] Clean checkout docker compose up --build; curl /healthz local và public HTTPS; test invalid request/error/no-store.
- [ ] Kiểm tra image/layer/config không chứa secret; prod mock config phải bị từ chối; verify dev mock có banner phía client.

**Expected deliverables & handoff:** Dockerfile/compose, public health URL, CI log và API fixture test; B02 nhận routes/models, A02 nhận API origin.

**Reviewer:** C

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="b02"></a>

### B02 — Real analyze integration

**Owner:** B | **Priority:** P0 | **Ngày:** 29/11/2026 ICT | **Estimate:** 5h | **Dependency:** B01;C01 | **Seed:** Backlog

**Mục tiêu / mô tả:** Kết nối AI engine thật và bảo đảm đường truyền input/output an toàn cho cả Extension và Web.

**Required reading:** docs/api-contracts.md; docs/ai-contract.md; docs/architecture-alignment.md; C01 handoff.

**File ownership:** backend/app/routes/**, app/security/**, app/main.py, app/contracts.py nếu cần không đổi contract, tests/api/**, deploy/CI.

**Implementation checklist:**
- [ ] Nối POST /api/v1/analyze vào async assess(AnalysisInput) từ C; wrap assessment + request_id + latency_ms + analysis_mode; validate semantic output.
- [ ] Capping actual HTTP body 3 MiB kể cả chunked; raw base64 strict, decoded ≤2 MiB; text ≤6000, DNS hostname-only, consent true, không echo raw input.
- [ ] Dùng Pillow kiểm tra MIME thực, kích thước ≤2048 mỗi chiều/4M pixels, corrupt/animated/bomb; re-encode loại metadata trong memory, không temp file.
- [ ] Giới hạn tổng request ≤25s, AI timeout theo env (20s mặc định), cancel/timeout mapping theo contract; fallback UNKNOWN nếu engine trả an toàn, infra 503.
- [ ] Cấu hình CORS chỉ nếu cần (verified extension origins, no wildcard credentials); web same-origin; không backend fetch page_host/URL.
- [ ] Build và deploy revision thật; gắn public web dist và extension dev/release ZIP với host đúng; phối hợp A02/C02 run live smoke trước 29/11 tối.

**Acceptance criteria (gốc):** Wire provider, body/image validation, timeout, no-store; deploy real end-to-end

**Testing checklist:**
- [ ] Test valid text/image/mixed, semantic invalid response, invalid base64/MIME, limits, consent, 503/timeout/no-store; kiểm tra no API key/raw input logs.
- [ ] G2: Extension screenshot+paste và web upload+paste thực sự nhận response mode AI từ public endpoint; lưu request ID, commit, revision, test output.

**Expected deliverables & handoff:** Public real endpoint, Docker revision, integration evidence và danh sách lỗi; A03/B03/C03 nhận URL, schema/port version, test details.

**Reviewer:** C

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="b03"></a>

### B03 — Security + integration gate

**Owner:** B | **Priority:** P0 | **Ngày:** 30/11/2026 ICT | **Estimate:** 5h | **Dependency:** B02 | **Seed:** Backlog

**Mục tiêu / mô tả:** Hoàn thiện guardrails, kiểm thử tích hợp và bảo mật trước khi cho phép release/hardening.

**Required reading:** docs/architecture-alignment.md (security); docs/api-contracts.md; docs/release-checklist.md G3; B02/A03 evidence.

**File ownership:** backend/app/security/**, main.py/routes nếu cần, tests/api/**, CI/deploy.

**Implementation checklist:**
- [ ] Thêm rate limiter 5/min/IP, 30/day/IP, max 2 concurrent/instance theo config; trusted proxy IP hoặc global cap nếu không xác minh được; 429 Retry-After integer.
- [ ] Thêm configurable total quota/cap và kiểm tra billing alert; single instance/worker, giới hạn per-process reset ghi rõ; không giả định CORS là auth.
- [ ] Chặn logging body/base64/text/PII, error echo, tracebacks public; log request ID/status/elapsed/model ID, no-store cả lỗi.
- [ ] Test prod fail closed khi thiếu key/config hoặc mock; timeout/refusal/malformed provider theo C port, không fallback LOW/AI fake.
- [ ] Chạy regression invalid/oversized/chunked, decompression bomb, MIME spoof, unknown fields, consent, invalid host; không có outbound fetch theo user input.
- [ ] Chốt G3 với A/C; lỗi P0 có owner/deadline, hoãn P1 nếu chưa xanh.

**Acceptance criteria (gốc):** Rate/concurrency, no logs, invalid/oversize, 429/timeouts, production rejects mock; all P0 smoke

**Testing checklist:**
- [ ] pytest với concurrent requests, rate window, 429 retry-after, cap; inspect synthetic sentinel không xuất hiện trong log/error; provider failure không lộ exception.
- [ ] Smoke external web/extension và verify release path; run test/lint/build/CI theo script thật, ghi pass/fail.

**Expected deliverables & handoff:** Security regression report, rate config, privacy evidence, G3 decision; B04 nhận P0 issues và triển khai giới hạn production.

**Reviewer:** C

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="b04"></a>

### B04 — Release hardening + README

**Owner:** B | **Priority:** P0 | **Ngày:** 01/12/2026 ICT | **Estimate:** 5h | **Dependency:** B03;A03;C03 | **Seed:** Backlog

**Mục tiêu / mô tả:** Đưa sản phẩm lên bản release candidate có thể dựng lại và dùng độc lập; chuẩn bị README khai báo đầy đủ.

**Required reading:** docs/release-checklist.md; docs/architecture-alignment.md; A03/C03 reports.

**File ownership:** Dockerfile, compose, backend infra, CI, root README, .env.example, download route; A chịu trách nhiệm UI dist.

**Implementation checklist:**
- [ ] Pin versions/lockfiles, xác minh fresh build từ clean checkout; build web dist trong Docker hoặc copy verified dist đúng commit.
- [ ] Giữ public URL ổn định, yêu cầu A build extension với exact host permission; serve `/downloads/extension.zip` chứa unpacked dist, không private signing key.
- [ ] Cấu hình public invoker/HTTPS, single instance, timeout, concurrency, secret và quota đến 11/12; kiểm tra health cheap.
- [ ] Viết root README commands thật, architecture/model/prompt version, external service/licences, source/data provenance, AI tools, privacy/limits; A/C gửi declaration.
- [ ] Chạy CI lint/test/build + Docker smoke, external network smoke cả client; xử lý P0 blocker, không thêm service.

**Acceptance criteria (gốc):** Clean build/CI, download extension with final API host, actual external smoke and README declarations

**Testing checklist:**
- [ ] Fresh checkout Docker build/run + test, tải ZIP từ public URL và Load unpacked; verify dist API origin, no debug/mock/key in release.
- [ ] Kiểm tra health/public analyze, log/config an toàn và chi phí/quota; ghi version/revision và lỗi còn tồn tại.

**Expected deliverables & handoff:** Release candidate revision, URL/download, root README và QA evidence; A05/C05 nhận đúng release candidate; B05 chuẩn bị tag/ZIP.

**Reviewer:** C

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="b05"></a>

### B05 — Freeze release and source ZIP

**Owner:** B | **Priority:** P0 | **Ngày:** 02/12/2026 ICT | **Estimate:** 5h | **Dependency:** B04;C04;A04 | **Seed:** Backlog

**Mục tiêu / mô tả:** Freeze release 02/12 trước 18:00 ICT, tạo source ZIP đầy đủ và tái lập được; phối hợp C05 ghi hình đúng bản.

**Required reading:** docs/release-checklist.md G4; B04 release record; C04 evaluation; A04 docs.

**File ownership:** submission/source.zip, release manifest, root README, deployment metadata; không tự sửa code lane khác.

**Implementation checklist:**
- [ ] Xác nhận G4 với A/C: metrics thật, P0 tests, public URL, UI và AI release candidate; chốt commit/tag v0.1-contest và image digest.
- [ ] Đảm bảo C05 quay đúng revision, A05 dùng đúng URL/metrics; critical fix cần review, rebuild/re-test và quay lại phần bị ảnh hưởng trước freeze.
- [ ] Đóng gói toàn bộ extension/demo/backend/evaluation/contracts/ai_artifacts + lockfiles, Dockerfile, compose, .env.example, README; không .env/keys/.git/node_modules/cache/raw scans.
- [ ] Unzip vào thư mục sạch, kiểm tra cấu trúc và run/build theo README; kiểm tra secret scan và dependencies/licenses declarations.
- [ ] Tính SHA256 source ZIP và extension ZIP, lưu release manifest (commit/tag/digest/public URL/model/prompt version/test times), đảm bảo hosting/quota tới 11/12.

**Acceptance criteria (gốc):** Tagged tested commit + image digest, ZIP checksum, README, clean unzip/run; retain hosting

**Testing checklist:**
- [ ] Test archive integrity, kiểm tra nội dung ZIP và clean smoke; đối chiếu public revision đúng image digest, extension ZIP đúng checksum.
- [ ] Record CI/test thật, không đánh dấu pass nếu chưa chạy; xác nhận C05 video/A05 PDFs sẽ dùng cùng release.

**Expected deliverables & handoff:** source.zip + release manifest + verification log + sign-off; A06/C06 nhận revision/hash; B06 nhận source ZIP và runbook.

**Reviewer:** C

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="b06"></a>

### B06 — Final submission & runbook

**Owner:** B | **Priority:** P0 | **Ngày:** 03/12/2026 ICT | **Estimate:** 3h | **Dependency:** A05;B05;C05;A06;C06 | **Seed:** Backlog

**Mục tiêu / mô tả:** Điều phối nộp bài đúng hạn và duy trì release đã nộp hoạt động theo thể lệ.

**Required reading:** docs/release-checklist.md G5; B05 release manifest; A05/A06/C05/C06 sign-offs.

**File ownership:** submission manifest, receipt, runbook và nhật ký; không đổi bản nộp sau hạn.

**Implementation checklist:**
- [ ] Thu guide.pdf, source.zip, slides.pdf, demo.mp4 đúng version; verify file names, hashes, page count, video duration/format và links.
- [ ] Đối chiếu FAQ/thể lệ và cổng nộp; đăng ký leader thực hiện submit chính thức, B điều phối. Mục tiêu nội bộ trước 18:00 ICT ngày 03/12, hard cutoff 23:59:59.
- [ ] Kiểm tra lần cuối từ máy khác, health + live text/image, public ZIP; mọi blocker P0 phải giải quyết và re-test trước submit.
- [ ] Lưu receipt/timestamp, hashes của 4 file ngoài repo public; nếu nộp lại trước cutoff thì kiểm tra lại toàn bộ bundle và lưu receipt mới.
- [ ] Bàn giao runbook đến 11/12: owner/backup contact, health/error/usage/budget, secret validity, restore same revision nếu được phép; hỏi BTC nếu chưa rõ.

**Acceptance criteria (gốc):** Leader submits all files before 18:00 ICT; capture receipt, hashes, maintain to 11/12

**Testing checklist:**
- [ ] Đối chiếu A06/C06 sign-off, receipt chính thức và đúng 4 file; kiểm tra link không cần tài khoản nhóm.
- [ ] Thử health monitor và xác minh credential/quota/hosting; không ghi thông tin đăng nhập trong runbook public.

**Expected deliverables & handoff:** Receipt + file hashes + deployed revision + operations handoff; nhóm trưởng xác nhận đã nộp, B chịu trách nhiệm duy trì.

**Reviewer:** C (A đồng xác nhận)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---


## Member C — AI Engineer (30h)

<a id="c00"></a>

### C00 — Model/provider spike

**Owner:** C | **Priority:** P0 | **Ngày:** 27/11/2026 ICT | **Estimate:** 3h | **Dependency:** - | **Seed:** Ready

**Mục tiêu / mô tả:** Kiểm chứng model vision thực tế trước khi chọn provider; tránh cam kết model chưa có key/quota.

**Required reading:** docs/ai-contract.md; research/stack-and-market.md; docs/product-brief.md; contracts/model-assessment.schema.json.

**File ownership:** ghi chú model spike của C trong evaluation/ hoặc research; không sửa shared contract.

**Implementation checklist:**
- [ ] Dùng SDK/model vision được account hỗ trợ, kiểm tra key hợp lệ, quota, billing, data use/retention và terms; secret chỉ qua env.
- [ ] Chuẩn bị 3 text + 3 screenshot synthetic có risky/benign/ambiguous; không dùng dữ liệu thật hoặc link lừa đảo hoạt động.
- [ ] Gọi thử multimodal và structured output, validate JSON với schema/semantic rules; đo elapsed và ghi lỗi/truncation.
- [ ] So sánh ít nhất tính khả dụng, chất lượng VN, độ trễ và chi phí dự kiến giữa lựa chọn khả thi; pin model ID/SDK version đã test, đề xuất fallback provider nếu lỗi.
- [ ] Ghi provider privacy disclosure, budget/quota đến 11/12 và risk; gửi B config names, requirements đề xuất, A/C xác nhận G0.

**Acceptance criteria (gốc):** 3 text + 3 ảnh synthetic; pin model ID, quota/privacy/latency, structured JSON

**Testing checklist:**
- [ ] 6 synthetic calls, ghi actual pass/fail, latency, mode, model ID; không ghi key/ảnh thật; kiểm tra text/image-only.
- [ ] Nếu không có model usable, đánh dấu Blocked và báo B00 ngay, không fake success; switch chỉ sau team duyệt.

**Expected deliverables & handoff:** Spike report, verified model ID, SDK/version, quota/terms decision; B00/B01 nhận dependency/env, C01 nhận provider configuration.

**Reviewer:** A (B duyệt infra/quota)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="c01"></a>

### C01 — Vision engine + schema

**Owner:** C | **Priority:** P0 | **Ngày:** 28/11/2026 ICT | **Estimate:** 5h | **Dependency:** B00;C00 | **Seed:** Backlog

**Mục tiêu / mô tả:** Xây AI engine độc lập với HTTP, dùng multimodal model thật và trả ModelAssessment đúng port đã freeze.

**Required reading:** docs/ai-contract.md; docs/api-contracts.md; contracts/model-assessment.schema.json; B00 port.

**File ownership:** backend/app/engine/**, backend/tests/engine/**; B sở hữu contracts.py và dependency lock.

**Implementation checklist:**
- [ ] Tạo provider adapter injectable, async assess(input: AnalysisInput) -> EngineResult; đọc AI_PROVIDER/AI_MODEL/GEMINI_API_KEY/AI_TIMEOUT_SECONDS từ env, không hardcode key.
- [ ] Chuẩn hóa Unicode NFC; truyền ảnh/text/hostname như untrusted data, tách system prompt; không tools/function calls/browsing, không fetch URL.
- [ ] Dùng canonical prompt v1 và schema ModelAssessment; cấu hình output budget và variability thấp nếu hỗ trợ; pin prompt version và model ID.
- [ ] Parse strict Pydantic + semantic check: HIGH/MEDIUM evidence, LOW NONE, UNKNOWN UNDETERMINED; mask PII; phân biệt evidence từ text/ảnh/suy luận.
- [ ] Implement provider timeout/refusal/invalid-output handling tối thiểu để không crash; C02 hoàn thiện fallback; không đưa request_id/latency vào engine.

**Acceptance criteria (gốc):** Text/image inference; prompt injection isolation, valid assessment and unit mock

**Testing checklist:**
- [ ] Unit test fake adapter cho text/image/mixed, schema invalid, prompt injection, thiếu evidence, unsupported output; thực hiện real text+image smoke.
- [ ] Kiểm tra không log input/raw response/key, không tools/URL; báo B dependency/port mismatch, không sửa shared files.

**Expected deliverables & handoff:** Engine module, prompt v1, unit test và real smoke evidence; B02 nhận import path, config, model ID, expected errors; C02 nhận adapter.

**Reviewer:** A

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="c02"></a>

### C02 — Fallback & dev fixture set

**Owner:** C | **Priority:** P0 | **Ngày:** 29/11/2026 ICT | **Estimate:** 5h | **Dependency:** C01 | **Seed:** Backlog

**Mục tiêu / mô tả:** Xử lý AI failure trung thực và chuẩn bị dev dataset/baseline để cải thiện prompt trước holdout.

**Required reading:** docs/ai-contract.md (pipeline/rubric/evaluation); C01 handoff; contracts/response.schema.json.

**File ownership:** backend/app/engine/**, backend/tests/engine/**, evaluation/**.

**Implementation checklist:**
- [ ] Xây fallback RULE_FALLBACK luôn UNKNOWN/UNDETERMINED, lý do cụ thể, safe static actions, optional grounded lexical cues; không LOW/AI giả.
- [ ] Mask evidence và action output: không full OTP/tài khoản/điện thoại/link; không lời khuyên theo số/link từ scam; downgrade UNKNOWN khi evidence không đủ.
- [ ] Tạo lexical baseline cố định dựa request patterns/ngữ cảnh phủ định (không dùng keyword đơn lẻ); cùng quy tắc flagged HIGH/MEDIUM hoặc binary flag rõ ràng.
- [ ] Tạo 12 dev fixture trong tổng 30, ID/label/modality/expected risk range; synthetic screenshot từ HTML local, `.example`/`.invalid`.
- [ ] Chạy dev test thật, ghi model/prompt version/latency/schema results, cải thiện prompt trên dev only; phối hợp B02 G2 real analyze.

**Acceptance criteria (gốc):** UNKNOWN fallback, safe actions, 12 dev fixtures + lexical baseline; record real test

**Testing checklist:**
- [ ] Test timeout, refusal, malformed JSON, empty/unreadable, fabricated evidence, unsafe action, benign OTP warning; all fallback result đúng schema và mode.
- [ ] Test baseline với risky/benign/ambiguous, verify không gửi PII; record real scan request ID không lộ input.

**Expected deliverables & handoff:** Fallback policy/tests, 12 dev fixtures + labels, baseline runner, dev metrics; C03 nhận bộ dev và prompt version, B03 nhận failure semantics.

**Reviewer:** A

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="c03"></a>

### C03 — Adversarial QA + holdout lock

**Owner:** C | **Priority:** P0 | **Ngày:** 30/11/2026 ICT | **Estimate:** 5h | **Dependency:** C02;B02 | **Seed:** Backlog

**Mục tiêu / mô tả:** Kiểm thử đối kháng, hoàn thành và khóa bộ 30 fixture trước khi đánh giá holdout chính thức.

**Required reading:** docs/ai-contract.md (evaluation); docs/release-checklist.md G3; C02 dev results; B02 live integration.

**File ownership:** evaluation/**, backend/app/engine/** và engine tests (dev-only tuning trước freeze).

**Implementation checklist:**
- [ ] Hoàn thành ≥30 synthetic cases: 15 risky, 10 benign, 5 ambiguous; ≥12 image-only, ≥10 text-only, còn lại mixed; phân bố theo nhóm scam trong AI contract.
- [ ] Chia dev 12 và holdout 18 (9 risky/6 benign/3 unknown), không trùng case/near duplicate; hai người label độc lập, resolve khác biệt trước khi run.
- [ ] Tạo adversarial set riêng: ignore instructions trong text/ảnh, fabricated OTP, malicious HTML, blurry, unsafe action, malformed output, refusal, timeout; phối hợp B test media/limit.
- [ ] Kiểm tra evidence grounded, no identity/fraud proof claim, no safe guarantee, no leak, no tool execution; UI nhận đúng fallback/mode với A.
- [ ] Chỉ sửa prompt/policy dựa dev/adversarial; freeze model/prompt/baseline/fixture IDs và hash trước holdout; chưa chạy holdout.

**Acceptance criteria (gốc):** 30 labeled cases stratified dev/holdout; independent labels, adversarial failures, prompt freeze

**Testing checklist:**
- [ ] Run engine unit/adversarial, live synthetic smoke; verify labels/distribution và holdout chưa truy cập để tuning; G3 no critical safety issues.
- [ ] Log failures bằng fixture ID/expected/predicted/mode/elapsed; báo A/B cross-lane bugs, không giả mạo kết quả.

**Expected deliverables & handoff:** 30 labeled fixtures + split manifest/hash, adversarial report, frozen model/prompt/baseline; C04 nhận holdout locked, B04 nhận safety sign-off.

**Reviewer:** A (B duyệt integration)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="c04"></a>

### C04 — Holdout evaluation + claims

**Owner:** C | **Priority:** P0 | **Ngày:** 01/12/2026 ICT | **Estimate:** 5h | **Dependency:** C03 | **Seed:** Backlog

**Mục tiêu / mô tả:** Đo AI so với rule baseline trên cùng holdout, cung cấp bằng chứng thật cho slide, video và release.

**Required reading:** docs/ai-contract.md evaluation protocol; C03 frozen manifest; B04 candidate info.

**File ownership:** evaluation/runner, results, report; không sửa prompt/model trên holdout.

**Implementation checklist:**
- [ ] Chạy baseline và AI trên cùng 18 holdout (9 risky/6 benign/3 unknown), dùng version đã freeze; ghi fixture ID, expected/predicted, mode, elapsed, schema status.
- [ ] Flag HIGH/MEDIUM; risky UNKNOWN tính không flagged trong recall, benign UNKNOWN báo riêng không gọi safe; ambiguous riêng; ghi TP/FP/TN/FN theo quy ước.
- [ ] Tính precision/recall/F1 nếu denominator >0, benign FPR, UNKNOWN rate/coverage, median/p95 nearest rank, schema-valid rate; raw counts và n.
- [ ] Đối chiếu mục tiêu recall ≥80%, FPR ≤25%, valid 100%, p95 ≤15s warm low-load; ghi unmet và case thất bại; không che giấu.
- [ ] Nếu cần sửa critical issue, báo nhóm và dùng dev set; holdout mới nếu retune, không báo lại số trên holdout cũ như independent test.

**Acceptance criteria (gốc):** AI vs baseline same holdout, counts/precision/recall/FP/unknown/latency; limitations evidence

**Testing checklist:**
- [ ] Kiểm tra metrics bằng phép tính từ CSV, match sample count và model/prompt versions; kiểm tra fallback vs AI không gộp sai.
- [ ] Review với A/B: claim chỉ trong phạm vi synthetic holdout, không khẳng định hiệu quả thực địa hoặc giảm thiệt hại.

**Expected deliverables & handoff:** Evaluation report + raw sanitized results + baseline comparison table + limitations; A05/C05 dùng số liệu chính xác, B05 nhận G4 evidence.

**Reviewer:** A

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="c05"></a>

### C05 — Record final demo MP4

**Owner:** C | **Priority:** P0 | **Ngày:** 02/12/2026 ICT | **Estimate:** 5h | **Dependency:** C04;B04;A04 | **Seed:** Backlog

**Mục tiêu / mô tả:** Quay video demo sản phẩm chạy thật, thể hiện rõ giá trị AI, giữ thời lượng tối đa 3 phút.

**Required reading:** docs/release-checklist.md demo script; C04 report; A04 demo flow; B04 release candidate.

**File ownership:** submission/demo.mp4 và nguồn quay/dựng của C.

**Implementation checklist:**
- [ ] Xác nhận revision/model với B05 trước ghi hình; dùng synthetic page/screenshot và dữ liệu mẫu, không quay key, account, email thật hay tab cá nhân.
- [ ] Storyboard ~165s: problem → Chrome capture/crop/consent → real result evidence/actions → benign/ambiguous → web demo cùng API → actual metrics/limitations.
- [ ] Quay thực tế latency và response; không mock, không jump cut khiến người xem hiểu sai độ trễ; nếu request fail, xử lý trung thực hoặc quay lại.
- [ ] Hiển thị phân biệt AI vs fallback, LOW không xác nhận an toàn, user quyết định; giải thích AI hiểu ngữ cảnh hơn lexical baseline theo số C04.
- [ ] Xuất MP4 ≤180s, kiểm tra audio/subtitle tiếng Việt đọc được, không nội dung cá nhân; phối hợp A/B review trước freeze.

**Acceptance criteria (gốc):** ≤3 min running real release candidate; no personal data; actual results/limitations

**Testing checklist:**
- [ ] Phát file từ đầu đến cuối, kiểm tra duration/codec/quality, không PII, link/demo revision khớp release manifest.
- [ ] Nếu release thay đổi critical trước freeze, quay lại phần bị ảnh hưởng và đối chiếu metrics, không dùng clip cũ sai version.

**Expected deliverables & handoff:** demo.mp4 final + duration + revision + sign-off; C06 verify video, B06 nhận video final.

**Reviewer:** A (B duyệt revision)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

<a id="c06"></a>

### C06 — Final AI/video verification

**Owner:** C | **Priority:** P0 | **Ngày:** 03/12/2026 ICT | **Estimate:** 2h | **Dependency:** C05;B05 | **Seed:** Backlog

**Mục tiêu / mô tả:** Kiểm tra AI và video lần cuối trên release đã freeze; xác nhận provider đủ khả dụng tới 11/12.

**Required reading:** docs/release-checklist.md G5; B05 release manifest; C05 MP4; C04 evaluation.

**File ownership:** AI verification report; chỉ sửa sản phẩm trước nộp nếu critical fix được B điều phối.

**Implementation checklist:**
- [ ] Chạy một text-only và một image-only synthetic case qua public endpoint từ môi trường ngoài; response AI hợp lệ, evidence/actions/limitations đúng contract.
- [ ] Xác minh model/prompt version, key validity, quota/budget cùng B; không xoay model âm thầm, không test bằng dữ liệu thật.
- [ ] Mở MP4 final, xác minh ≤3 phút, file playable, revision đúng, actual claims/metrics đúng C04, không PII/mock.
- [ ] Đối chiếu video hash với manifest B06; ghi ICT timestamp, request ID, mode, latency, test evidence và blocker.

**Acceptance criteria (gốc):** Validate MP4 duration, live AI text/image, model/quota until 11/12, sign off

**Testing checklist:**
- [ ] Check real public responses, schema, no safe guarantee; kiểm tra video duration và checksum bằng công cụ sẵn có, không tự nhận pass nếu chưa chạy.
- [ ] Nếu provider unavailable, đánh dấu Blocked, báo B06 ngay; không dùng fallback làm bằng chứng AI thật.

**Expected deliverables & handoff:** Final AI/video verification và sign-off hoặc blocker, provider availability handoff đến 11/12; B06 nhận xác nhận trước submit.

**Reviewer:** A (B xác minh quota)

**Evidence:** PR/commit: TBD · commands/results: TBD · artifacts: TBD · blockers: TBD

---

## P1 — Optional, chỉ pull sau G3 được duyệt

Các ID dưới đây đã có trong overview; không nằm trong 21 P0, chưa ước lượng hay xếp lịch. Không dùng buffer nộp bài cho P1.

| ID | Owner | Hướng dẫn / nghiệm thu tối thiểu |
|---|---|---|
| P1-01 | B/C | Kiểm tra điều khoản URL reputation; chỉ tra domain đã được duyệt, không truy cập URL tùy ý. Kết quả reputation chỉ là tín hiệu bổ sung, không chứng nhận an toàn. Contract change cần A/B/C duyệt. |
| P1-02 | A | QR decode cục bộ từ ảnh đã duyệt; hiển thị dạng text inert, không mở link hay xác thực thanh toán. Test QR lỗi/không có QR và quyền tối thiểu. |
| P1-03 | A | Cải thiện crop keyboard/drag/resize; test payload chỉ gồm ảnh sau crop; không thay đổi consent. |
| P1-04 | C | Thêm synthetic evaluation scenarios độc lập; phân biệt tập bổ sung và holdout gốc; không dùng test để tune rồi báo như holdout mới. |
