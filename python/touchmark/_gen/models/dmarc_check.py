from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_status import CheckStatus

T = TypeVar("T", bound="DmarcCheck")


@_attrs_define
class DmarcCheck:
    """
    Attributes:
        status (CheckStatus):
        record (None | str):
        location (None | str):
        policy (None | str):
        warnings (list[str]):
        error (None | str):
    """

    status: CheckStatus
    record: None | str
    location: None | str
    policy: None | str
    warnings: list[str]
    error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        record: None | str
        record = self.record

        location: None | str
        location = self.location

        policy: None | str
        policy = self.policy

        warnings = self.warnings

        error: None | str
        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "record": record,
                "location": location,
                "policy": policy,
                "warnings": warnings,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = CheckStatus(d.pop("status"))

        def _parse_record(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        record = _parse_record(d.pop("record"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_policy(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        policy = _parse_policy(d.pop("policy"))

        warnings = cast(list[str], d.pop("warnings"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        dmarc_check = cls(
            status=status,
            record=record,
            location=location,
            policy=policy,
            warnings=warnings,
            error=error,
        )

        dmarc_check.additional_properties = d
        return dmarc_check

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
