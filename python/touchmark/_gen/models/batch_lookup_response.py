from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_lookup import IpLookup


T = TypeVar("T", bound="BatchLookupResponse")


@_attrs_define
class BatchLookupResponse:
    """
    Attributes:
        results (list[IpLookup]):
        credits_charged (int):
        request_id (str):
    """

    results: list[IpLookup]
    credits_charged: int
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        credits_charged = self.credits_charged

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "credits_charged": credits_charged,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_lookup import IpLookup  # noqa: PLC0415

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = IpLookup.from_dict(results_item_data)

            results.append(results_item)

        credits_charged = d.pop("credits_charged")

        request_id = d.pop("request_id")

        batch_lookup_response = cls(
            results=results,
            credits_charged=credits_charged,
            request_id=request_id,
        )

        batch_lookup_response.additional_properties = d
        return batch_lookup_response

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
