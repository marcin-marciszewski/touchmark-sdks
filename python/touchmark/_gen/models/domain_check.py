from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainCheck")


@_attrs_define
class DomainCheck:
    """
    Attributes:
        mx_found (bool):
        implicit_mx (bool):
        null_mx (bool):
        mx_vendor (None | str):
        mx_hosts (list[str]):
    """

    mx_found: bool
    implicit_mx: bool
    null_mx: bool
    mx_vendor: None | str
    mx_hosts: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mx_found = self.mx_found

        implicit_mx = self.implicit_mx

        null_mx = self.null_mx

        mx_vendor: None | str
        mx_vendor = self.mx_vendor

        mx_hosts = self.mx_hosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mx_found": mx_found,
                "implicit_mx": implicit_mx,
                "null_mx": null_mx,
                "mx_vendor": mx_vendor,
                "mx_hosts": mx_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mx_found = d.pop("mx_found")

        implicit_mx = d.pop("implicit_mx")

        null_mx = d.pop("null_mx")

        def _parse_mx_vendor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mx_vendor = _parse_mx_vendor(d.pop("mx_vendor"))

        mx_hosts = cast(list[str], d.pop("mx_hosts"))

        domain_check = cls(
            mx_found=mx_found,
            implicit_mx=implicit_mx,
            null_mx=null_mx,
            mx_vendor=mx_vendor,
            mx_hosts=mx_hosts,
        )

        domain_check.additional_properties = d
        return domain_check

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
