from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dns_ready import DnsReady
    from ..models.gap import Gap
    from ..models.readiness_checks import ReadinessChecks


T = TypeVar("T", bound="SenderReadinessResponse")


@_attrs_define
class SenderReadinessResponse:
    """
    Attributes:
        domain (str):
        dns_ready (DnsReady):
        checks (ReadinessChecks):
        gaps (list[Gap]):
        not_checked (list[str]):
        credits_charged (int):
        request_id (str):
    """

    domain: str
    dns_ready: DnsReady
    checks: ReadinessChecks
    gaps: list[Gap]
    not_checked: list[str]
    credits_charged: int
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        dns_ready = self.dns_ready.to_dict()

        checks = self.checks.to_dict()

        gaps = []
        for gaps_item_data in self.gaps:
            gaps_item = gaps_item_data.to_dict()
            gaps.append(gaps_item)

        not_checked = self.not_checked

        credits_charged = self.credits_charged

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "dns_ready": dns_ready,
                "checks": checks,
                "gaps": gaps,
                "not_checked": not_checked,
                "credits_charged": credits_charged,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_ready import DnsReady  # noqa: PLC0415
        from ..models.gap import Gap  # noqa: PLC0415
        from ..models.readiness_checks import ReadinessChecks  # noqa: PLC0415

        d = dict(src_dict)
        domain = d.pop("domain")

        dns_ready = DnsReady.from_dict(d.pop("dns_ready"))

        checks = ReadinessChecks.from_dict(d.pop("checks"))

        gaps = []
        _gaps = d.pop("gaps")
        for gaps_item_data in _gaps:
            gaps_item = Gap.from_dict(gaps_item_data)

            gaps.append(gaps_item)

        not_checked = cast(list[str], d.pop("not_checked"))

        credits_charged = d.pop("credits_charged")

        request_id = d.pop("request_id")

        sender_readiness_response = cls(
            domain=domain,
            dns_ready=dns_ready,
            checks=checks,
            gaps=gaps,
            not_checked=not_checked,
            credits_charged=credits_charged,
            request_id=request_id,
        )

        sender_readiness_response.additional_properties = d
        return sender_readiness_response

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
