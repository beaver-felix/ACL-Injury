"""Shared Python types for the canonical contracts in ai_artifacts/contracts.

The JSON Schema files remain the machine-readable source of truth. These types
encode the frozen candidate engine boundary; they do not implement HTTP routes
or the AI engine.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Annotated, Literal, TypeAlias

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

RiskLevel: TypeAlias = Literal["LOW", "MEDIUM", "HIGH", "UNKNOWN"]
Category: TypeAlias = Literal[
    "IMPERSONATION",
    "CREDENTIAL_THEFT",
    "PAYMENT_SCAM",
    "INVESTMENT_SCAM",
    "JOB_SCAM",
    "OTHER",
    "NONE",
    "UNDETERMINED",
]
SignalKind: TypeAlias = Literal[
    "IMPERSONATION",
    "URGENCY",
    "CREDENTIAL_REQUEST",
    "PAYMENT_REQUEST",
    "UNREALISTIC_REWARD",
    "SECRECY",
    "SUSPICIOUS_LINK",
    "CONTEXT_INFERENCE",
    "OTHER",
]
AnalysisMode: TypeAlias = Literal["AI", "RULE_FALLBACK"]
MimeType: TypeAlias = Literal["image/jpeg", "image/png"]

Summary = Annotated[str, StringConstraints(min_length=1, max_length=240)]
Evidence = Annotated[str, StringConstraints(min_length=1, max_length=180)]
Explanation = Annotated[str, StringConstraints(min_length=1, max_length=240)]
ShortItem = Annotated[str, StringConstraints(min_length=1, max_length=180)]


class ContractModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class Signal(ContractModel):
    kind: SignalKind
    evidence: Evidence
    explanation: Explanation


class ModelAssessment(ContractModel):
    """The six content fields returned by Member C."""

    risk_level: RiskLevel
    category: Category
    summary: Summary
    signals: Annotated[list[Signal], Field(max_length=5)]
    actions: Annotated[list[ShortItem], Field(min_length=1, max_length=3)]
    limitations: Annotated[list[ShortItem], Field(min_length=1, max_length=3)]

    @model_validator(mode="after")
    def enforce_semantic_relationships(self) -> ModelAssessment:
        if self.risk_level == "UNKNOWN" and self.category != "UNDETERMINED":
            raise ValueError("UNKNOWN requires category UNDETERMINED")
        if self.risk_level == "LOW" and self.category != "NONE":
            raise ValueError("LOW requires category NONE")
        if self.risk_level in {"HIGH", "MEDIUM"}:
            if not self.signals:
                raise ValueError("HIGH/MEDIUM require at least one signal")
            if self.category in {"NONE", "UNDETERMINED"}:
                raise ValueError("HIGH/MEDIUM require a risk category")
        return self


class AnalysisInput(ContractModel):
    """Validated content passed from Member B transport to Member C."""

    text: Annotated[str, StringConstraints(max_length=6000)] | None = None
    image_bytes: Annotated[bytes, Field(max_length=2 * 1024 * 1024)] | None = None
    mime_type: MimeType | None = None
    page_host: Annotated[str, StringConstraints(max_length=253)] | None = None

    @model_validator(mode="after")
    def enforce_content_boundary(self) -> AnalysisInput:
        if not (self.text and self.text.strip()) and self.image_bytes is None:
            raise ValueError("nonblank text or image_bytes is required")
        if (self.image_bytes is None) != (self.mime_type is None):
            raise ValueError("image_bytes and mime_type must be supplied together")
        return self


class EngineResult(ContractModel):
    """Engine output before Member B adds request_id and latency_ms."""

    assessment: ModelAssessment
    analysis_mode: AnalysisMode

    @model_validator(mode="after")
    def enforce_fallback_behavior(self) -> EngineResult:
        if self.analysis_mode == "RULE_FALLBACK" and self.assessment.risk_level != "UNKNOWN":
            raise ValueError("RULE_FALLBACK must return UNKNOWN")
        return self


# Member C supplies an async callable with this signature; no implementation lives here.
AssessPort: TypeAlias = Callable[[AnalysisInput], Awaitable[EngineResult]]
