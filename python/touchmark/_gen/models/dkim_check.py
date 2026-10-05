from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_status import CheckStatus

T = TypeVar("T", bound="DkimCheck")


@_attrs_define
class DkimCheck:
    """
    Attributes:
        status (CheckStatus):
        selectors_found (list[str]):
        selectors_tried (list[str]):
    """

    status: CheckStatus
    selectors_found: list[str]
    selectors_tried: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        selectors_found = self.selectors_found

        selectors_tried = self.selectors_tried

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "selectors_found": selectors_found,
                "selectors_tried": selectors_tried,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = CheckStatus(d.pop("status"))

        selectors_found = cast(list[str], d.pop("selectors_found"))

        selectors_tried = cast(list[str], d.pop("selectors_tried"))

        dkim_check = cls(
            status=status,
            selectors_found=selectors_found,
            selectors_tried=selectors_tried,
        )

        dkim_check.additional_properties = d
        return dkim_check

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
