#!/usr/bin/env python3
"""Validate canonical JSON Schemas, fixtures, negative cases and runtime types."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from jsonschema import FormatChecker
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validator_for

from backend.app.contracts import AnalysisInput, EngineResult, ModelAssessment

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "ai_artifacts" / "contracts"


def load_json(name: str) -> dict[str, Any]:
    with (CONTRACTS / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def validator(name: str):
    schema = load_json(name)
    validator_class = validator_for(schema)
    validator_class.check_schema(schema)
    return validator_class(schema, format_checker=FormatChecker())


def expect_invalid(schema_validator: Any, instance: dict[str, Any], label: str) -> None:
    try:
        schema_validator.validate(instance)
    except ValidationError:
        print(f"PASS negative: {label}")
        return
    raise AssertionError(f"negative case unexpectedly valid: {label}")


def main() -> None:
    assessment_schema = load_json("model-assessment.schema.json")
    response_schema = load_json("response.schema.json")
    request_validator = validator("request.schema.json")
    response_validator = validator("response.schema.json")
    error_validator = validator("error.schema.json")
    assessment_validator = validator("model-assessment.schema.json")
    print("PASS schemas: 4 Draft 2020-12 schemas are valid")

    request = load_json("example-request.json")
    response = load_json("example-response.json")
    error = load_json("example-error.json")
    request_validator.validate(request)
    response_validator.validate(response)
    error_validator.validate(error)

    assessment_fields = {
        "risk_level",
        "category",
        "summary",
        "signals",
        "actions",
        "limitations",
    }
    assessment_payload = {key: response[key] for key in assessment_fields}
    assessment_validator.validate(assessment_payload)
    assert {
        key: response_schema["properties"][key] for key in assessment_fields
    } == assessment_schema["properties"]
    assert response_schema["allOf"][:3] == assessment_schema["allOf"]
    print("PASS fixtures: request, response, error and extracted assessment")

    runtime_assessment = ModelAssessment.model_validate(assessment_payload)
    EngineResult(assessment=runtime_assessment, analysis_mode=response["analysis_mode"])
    AnalysisInput(
        text=request["text"],
        image_bytes=None,
        mime_type=None,
        page_host=request["page_host"],
    )
    assert set(ModelAssessment.model_fields) == assessment_fields
    assert set(AnalysisInput.model_fields) == {
        "text",
        "image_bytes",
        "mime_type",
        "page_host",
    }
    assert set(EngineResult.model_fields) == {"assessment", "analysis_mode"}
    print("PASS runtime: shared type fields and canonical fixture are compatible")

    invalid_request = copy.deepcopy(request)
    invalid_request["consent"] = False
    expect_invalid(request_validator, invalid_request, "consent must be true")
    invalid_request = copy.deepcopy(request)
    invalid_request["text"] = "   "
    expect_invalid(request_validator, invalid_request, "blank text without image")
    invalid_request = copy.deepcopy(request)
    invalid_request["unexpected"] = True
    expect_invalid(request_validator, invalid_request, "request extra field")
    invalid_request = copy.deepcopy(request)
    invalid_request["text"] = "x" * 6001
    expect_invalid(request_validator, invalid_request, "text limit")
    invalid_request = copy.deepcopy(request)
    invalid_request["image"] = {
        "mime_type": "image/gif",
        "data_base64": "AAAA",
    }
    expect_invalid(request_validator, invalid_request, "image MIME enum")
    invalid_request = copy.deepcopy(request)
    invalid_request["image"] = {
        "mime_type": "image/png",
        "data_base64": "A" * 2_796_205,
    }
    expect_invalid(request_validator, invalid_request, "encoded image limit")

    fallback_response = copy.deepcopy(response)
    fallback_response.update(
        risk_level="UNKNOWN",
        category="UNDETERMINED",
        signals=[],
        analysis_mode="RULE_FALLBACK",
    )
    response_validator.validate(fallback_response)
    print("PASS semantics: UNKNOWN RULE_FALLBACK response is valid")

    invalid_response = copy.deepcopy(response)
    invalid_response["risk_level"] = "UNKNOWN"
    expect_invalid(response_validator, invalid_response, "UNKNOWN category relationship")
    invalid_response = copy.deepcopy(response)
    invalid_response["analysis_mode"] = "RULE_FALLBACK"
    expect_invalid(response_validator, invalid_response, "fallback must be UNKNOWN")
    invalid_response = copy.deepcopy(response)
    invalid_response["risk_level"] = "MEDIUM"
    invalid_response["signals"] = []
    expect_invalid(response_validator, invalid_response, "MEDIUM requires signals")
    invalid_response = copy.deepcopy(response)
    invalid_response["latency_ms"] = -1
    expect_invalid(response_validator, invalid_response, "negative latency")
    invalid_response = copy.deepcopy(response)
    invalid_response["risk_level"] = "LOW"
    expect_invalid(response_validator, invalid_response, "LOW category relationship")
    invalid_response = copy.deepcopy(response)
    invalid_response["summary"] = "x" * 241
    expect_invalid(response_validator, invalid_response, "summary limit")

    invalid_error = copy.deepcopy(error)
    invalid_error["error"]["code"] = "UPSTREAM_TRACE"
    expect_invalid(error_validator, invalid_error, "unknown error code")
    invalid_error = copy.deepcopy(error)
    invalid_error["error"]["request_id"] = "not-a-uuid"
    expect_invalid(error_validator, invalid_error, "request_id format")

    print("PASS summary: 4 schemas, 5 valid payload views, runtime compatibility, 14 negatives")


if __name__ == "__main__":
    main()
