# UI, component & workflow contract
Owner A • Vietnamese-first • proposed

## Canonical screens
| Surface | State | Components | Expected action |
|---|---|---|---|
| Extension popup | idle | CaptureButton, TextInput, PrivacyNotice | Capture current viewport or paste |
| Extension popup | review | PreviewCrop, ConsentCheck, SubmitButton | Crop/clear; confirm preview before transmission |
| Web / | idle/review | UploadField, TextInput, sample chooser, same result layout | Upload/paste/sample; confirm |
| Both | analyzing | LoadingState | disable submit, no duplicate calls; cancel view or wait |
| Both | result | RiskBadge, EvidenceList, ActionList, Limitations | read, reset, try another |
| Both | error | ErrorState | edit or retry manually; 429 countdown |

State machine: `idle -> review -> analyzing -> result|error`; capture/validation failure -> error; review -> idle on clear; any result/error -> review/idle; client abort -> review; late response discarded using local request sequence. Closing popup discards preview; no upload before consent. Each change of text/image/host resets consent. Capture grant may expire on navigation; instruct user to reopen extension. Don't capture current review tab. If screenshot unavailable, paste text fallback always visible. Spinner is indeterminate and announced; never fabricated progress. Unknown is displayed as result, not LOW/error. Backend errors mapped per api-contracts. Preserve preview only in memory while same UI remains open; no history. If user leaves, discard.

## Component contracts
- `ScanForm`: source, text, image, pageHost, consent, onSubmit; owns temporary inputs. `PreviewCrop`: image, onCrop, onClear; canvas exports cropped JPEG/PNG, review sent image, accessible reset. `RiskBadge`: riskLevel only. `ResultCard`: `AnalyzeResponse`; shows summary + evidence + next steps + limitations; render all plain text, no clickable URLs. `ErrorState`: error code, retryAfter, onRetry; no raw upstream exception. `apiClient.analyze(payload, signal)` single adapter, 30s timeout, runtime response validation. Keep UI business rules display-only.
- Labels: HIGH “Nguy cơ cao”; MEDIUM “Có dấu hiệu đáng nghi”; LOW “Chưa thấy dấu hiệu rõ ràng”; UNKNOWN “Chưa đủ thông tin”. Show explicit badge “AI phân tích” or “AI chưa khả dụng — đánh giá hạn chế” based on mode. No safe/checkmark guarantee. Each result says “Không thay thế xác minh qua kênh chính thức”. Evidence visible, mask sensitive data. Risk status always icon + text + color, not color only.
- Style: neutral white/ink, indigo primary, amber caution, red high, gray unknown, teal neutral-low. 8px spacing, 8px controls, 12px cards, system sans supports Vietnamese. Extension popup width ~360–400px, vertical scroll max viewport, keyboard focus and visible labels; web responsive 320px+. No official MoMo logo or implied affiliation. Clear consent text: “Ảnh/văn bản bạn chọn sẽ được gửi đến máy chủ và dịch vụ AI để phân tích. Hãy che thông tin nhạy cảm trước khi gửi.” Explain app no retention, provider policies separate. No default checked consent.

## Acceptance
Capture and preview real tab, crop removes off-area content in network payload; text scan from both clients; no network before consent; result/high/medium/low/unknown; error for unsupported tab/image, timeout, 429, invalid response; close/reopen clean; keyboard access, labels, focus, no overflow; inspect DevTools payload and logs using synthetic data. Demo page links extension ZIP and installation instructions; sample buttons fill input only, not auto-submit.
