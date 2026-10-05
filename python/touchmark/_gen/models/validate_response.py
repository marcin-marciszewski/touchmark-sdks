from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_response_result import ValidateResponseResult

if TYPE_CHECKING:
    from ..models.checks import Checks
    from ..models.validate_response_datasets import ValidateResponseDatasets


T = TypeVar("T", bound="ValidateResponse")


@_attrs_define
class ValidateResponse:
    """
    Attributes:
        email (str):
        normalized (None | str):
        result (ValidateResponseResult):
        reasons (list[str]):
        did_you_mean (None | str):
        checks (Checks):
        datasets (ValidateResponseDatasets):
        credits_charged (int):
        request_id (str):
    """

    email: str
    normalized: None | str
    result: ValidateResponseResult
    reasons: list[str]
    did_you_mean: None | str
    checks: Checks
    datasets: ValidateResponseDatasets
    credits_charged: int
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        normalized: None | str
        normalized = self.normalized

        result = self.result.value

        reasons = self.reasons

        did_you_mean: None | str
        did_you_mean = self.did_you_mean

        checks = self.checks.to_dict()

        datasets = self.datasets.to_dict()

        credits_charged = self.credits_charged

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "normalized": normalized,
                "result": result,
                "reasons": reasons,
                "did_you_mean": did_you_mean,
                "checks": checks,
                "datasets": datasets,
                "credits_charged": credits_charged,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checks import Checks  # noqa: PLC0415
        from ..models.validate_response_datasets import (
            ValidateResponseDatasets,  # noqa: PLC0415
        )

        d = dict(src_dict)
        email = d.pop("email")

        def _parse_normalized(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        normalized = _parse_normalized(d.pop("normalized"))

        result = ValidateResponseResult(d.pop("result"))

        reasons = cast(list[str], d.pop("reasons"))

        def _parse_did_you_mean(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        did_you_mean = _parse_did_you_mean(d.pop("did_you_mean"))

        checks = Checks.from_dict(d.pop("checks"))

        datasets = ValidateResponseDatasets.from_dict(d.pop("datasets"))

        credits_charged = d.pop("credits_charged")

        request_id = d.pop("request_id")

        validate_response = cls(
            email=email,
            normalized=normalized,
            result=result,
            reasons=reasons,
            did_you_mean=did_you_mean,
            checks=checks,
            datasets=datasets,
            credits_charged=credits_charged,
            request_id=request_id,
        )

        validate_response.additional_properties = d
        return validate_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
