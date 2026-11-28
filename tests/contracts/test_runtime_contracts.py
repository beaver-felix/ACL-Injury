from __future__ import annotations

import pytest
from pydantic import ValidationError

from backend.app.contracts import AnalysisInput, EngineResult, ModelAssessment


def assessment(**updates: object) -> ModelAssessment:
    payload: dict[str, object] = {
        "risk_level": "UNKNOWN",
        "category": "UNDETERMINED",
        "summary": "Chưa đủ thông tin để đánh giá.",
        "signals": [],
        "actions": ["Xác minh qua kênh chính thức tự tìm."],
        "limitations": ["Nội dung cung cấp chưa đủ."],
    }
    payload.update(updates)
    return ModelAssessment.model_validate(payload)


def test_analysis_input_accepts_text_or_image() -> None:
    assert AnalysisInput(text="Nội dung synthetic").text == "Nội dung synthetic"
    assert AnalysisInput(image_bytes=b"synthetic", mime_type="image/png").mime_type == "image/png"


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"text": "   "},
        {"image_bytes": b"orphan"},
        {"text": "ok", "mime_type": "image/png"},
    ],
)
def test_analysis_input_rejects_incomplete_content(payload: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        AnalysisInput.model_validate(payload)


@pytest.mark.parametrize(
    "updates",
    [
        {"risk_level": "UNKNOWN", "category": "NONE"},
        {"risk_level": "LOW", "category": "UNDETERMINED"},
        {"risk_level": "MEDIUM", "category": "PAYMENT_SCAM", "signals": []},
        {"risk_level": "HIGH", "category": "NONE", "signals": [{"kind": "URGENCY", "evidence": "ngay", "explanation": "Ép thời gian."}]},
    ],
)
def test_assessment_rejects_invalid_relationships(updates: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        assessment(**updates)


def test_engine_fallback_is_unknown_only() -> None:
    EngineResult(assessment=assessment(), analysis_mode="RULE_FALLBACK")
    low = assessment(risk_level="LOW", category="NONE")
    with pytest.raises(ValidationError):
        EngineResult(assessment=low, analysis_mode="RULE_FALLBACK")


def test_transport_metadata_is_not_owned_by_engine_models() -> None:
    assert set(ModelAssessment.model_fields) == {
        "risk_level",
        "category",
        "summary",
        "signals",
        "actions",
        "limitations",
    }
    assert set(EngineResult.model_fields) == {"assessment", "analysis_mode"}
