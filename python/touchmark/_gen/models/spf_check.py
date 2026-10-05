from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_status import CheckStatus

T = TypeVar("T", bound="SpfCheck")


@_attrs_define
class SpfCheck:
    """
    Attributes:
        status (CheckStatus):
        record (None | str):
        dns_lookups (int | None):
        warnings (list[str]):
        error (None | str):
    """

    status: CheckStatus
    record: None | str
    dns_lookups: int | None
    warnings: list[str]
    error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        record: None | str
        record = self.record

        dns_lookups: int | None
        dns_lookups = self.dns_lookups

        warnings = self.warnings

        error: None | str
        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "record": record,
                "dns_lookups": dns_lookups,
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

        def _parse_dns_lookups(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        dns_lookups = _parse_dns_lookups(d.pop("dns_lookups"))

        warnings = cast(list[str], d.pop("warnings"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        spf_check = cls(
            status=status,
            record=record,
            dns_lookups=dns_lookups,
            warnings=warnings,
            error=error,
        )

        spf_check.additional_properties = d
        return spf_check

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
