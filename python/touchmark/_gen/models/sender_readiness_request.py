from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SenderReadinessRequest")


@_attrs_define
class SenderReadinessRequest:
    """
    Attributes:
        domain (str):
        dkim_selectors (list[str] | Unset):
    """

    domain: str
    dkim_selectors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        dkim_selectors: list[str] | Unset = UNSET
        if not isinstance(self.dkim_selectors, Unset):
            dkim_selectors = self.dkim_selectors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )
        if dkim_selectors is not UNSET:
            field_dict["dkim_selectors"] = dkim_selectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        dkim_selectors = cast(list[str], d.pop("dkim_selectors", UNSET))

        sender_readiness_request = cls(
            domain=domain,
            dkim_selectors=dkim_selectors,
        )

        sender_readiness_request.additional_properties = d
        return sender_readiness_request

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
