# API contracts v1
PROPOSED until B freezes after compatibility verification across affected A/B/C producer/consumer paths. Owner and final decision: B; A/C supply lane compatibility evidence. Machine-readable response/error schema in `../contracts/`; change only through a B-authorized shared contract PR. UTF-8 JSON, HTTP(S), no authentication for bounded demo.

## GET /healthz
200 `{"status":"ok","version":"<git-sha>"}`; no call to model. 503 if boot config invalid (or service refuses start).

## POST /api/v1/analyze
Content-Type application/json. `source` enum `extension|web`; `consent` must be true; `text` nullable (max 6000 chars); `image` nullable object `{mime_type: "image/jpeg"|"image/png", data_base64: "..."}` (raw base64, no data URI; decoded max 2 MiB); `page_host` optional nullable string max 253 chars, only DNS hostname, no path/userinfo/port/query; at least nonblank text or image. Reject unknown fields. Client may resize to max 2048 px long edge / 4M pixels, preview final image. Request example:
```json
{"source":"web","consent":true,"text":"Bạn cần xác minh khoản phí ngay để nhận thưởng.","image":null,"page_host":null}
```

200 response fields (all required):
- `request_id`: opaque UUID; `risk_level`: LOW|MEDIUM|HIGH|UNKNOWN; `category`: IMPERSONATION|CREDENTIAL_THEFT|PAYMENT_SCAM|INVESTMENT_SCAM|JOB_SCAM|OTHER|NONE|UNDETERMINED.
- `summary`: ≤240 chars, Vietnamese; `signals`: ≤5 objects `{kind, evidence, explanation}`; kind enum from schema, evidence ≤180 chars and explanation ≤240. Evidence must be visible in input or labeled `context inference` with no invented quote. Never output full account/phone/OTP or link; mask sensitive identifiers.
- `actions`: 1–3 short Vietnamese steps ≤180 chars each, no URLs; `limitations`: 1–3 ≤180 chars; `analysis_mode`: AI|RULE_FALLBACK; `latency_ms`: integer >=0 server total. LOW = no strong evidence observed, never verified safe. UNKNOWN = insufficient material or AI unavailable (fallback). UNKNOWN implies category UNDETERMINED; LOW implies NONE; fallback always UNKNOWN. HIGH/MEDIUM require ≥1 signal and not NONE/UNDETERMINED. B enforces semantic validation in addition to JSON Schema; C follows same invariants. See `example-response.json`.

## Error envelope
```json
{"error":{"code":"INVALID_INPUT","message":"Dữ liệu không hợp lệ.","request_id":"00000000-0000-4000-8000-000000000001"}}
```
| HTTP | code | UI action |
|---|---|---|
| 400 | INVALID_INPUT / CONSENT_REQUIRED | Fix input/consent |
| 413 | PAYLOAD_TOO_LARGE | Crop/resize |
| 415 | UNSUPPORTED_MEDIA | Choose PNG/JPEG |
| 429 | RATE_LIMITED | Wait Retry-After seconds, manual retry |
| 503 | SERVICE_UNAVAILABLE | Retry manually; no safe claim |
| 500 | INTERNAL_ERROR | Generic error/request ID |

B overrides default FastAPI validation error to envelope; no echoed values. Provider timeout/refusal/invalid result normally returns 200 UNKNOWN RULE_FALLBACK if engine can complete safely; true infrastructure error 503; never synthetic AI success. HTTP 30s client timeout aborts UI; may not cancel provider, do not auto-retry. `Retry-After` integer seconds for 429. `Cache-Control: no-store`. Error messages localized VN.

## Cross-lane handoff
B first commits schemas & mock response fixture; A integrates using fixture, C uses `ModelAssessment` subset (same risk/category/summary/signals/actions/limitations, excluding request_id/latency/analysis_mode). B calls C engine interface described in ai-contract; only B wraps transport metadata; A maps enum labels, never recalculates risk. Run schema validation in CI on fixture, Pydantic output and TS runtime parser (or generated types + parser). Contract version changes only after B verifies every affected consumer and authorizes the coordinated migration. API key never sent to frontend. No hidden endpoints for user-controlled URLs.
