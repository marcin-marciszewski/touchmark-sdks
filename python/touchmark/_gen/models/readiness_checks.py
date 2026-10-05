from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dkim_check import DkimCheck
    from ..models.dmarc_check import DmarcCheck
    from ..models.presence_check import PresenceCheck
    from ..models.spf_check import SpfCheck


T = TypeVar("T", bound="ReadinessChecks")


@_attrs_define
class ReadinessChecks:
    """
    Attributes:
        spf (SpfCheck):
        dkim (DkimCheck):
        dmarc (DmarcCheck):
        mx (PresenceCheck):
        mta_sts (PresenceCheck):
        tls_rpt (PresenceCheck):
        bimi (PresenceCheck):
    """

    spf: SpfCheck
    dkim: DkimCheck
    dmarc: DmarcCheck
    mx: PresenceCheck
    mta_sts: PresenceCheck
    tls_rpt: PresenceCheck
    bimi: PresenceCheck
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spf = self.spf.to_dict()

        dkim = self.dkim.to_dict()

        dmarc = self.dmarc.to_dict()

        mx = self.mx.to_dict()

        mta_sts = self.mta_sts.to_dict()

        tls_rpt = self.tls_rpt.to_dict()

        bimi = self.bimi.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spf": spf,
                "dkim": dkim,
                "dmarc": dmarc,
                "mx": mx,
                "mta_sts": mta_sts,
                "tls_rpt": tls_rpt,
                "bimi": bimi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dkim_check import DkimCheck  # noqa: PLC0415
        from ..models.dmarc_check import DmarcCheck  # noqa: PLC0415
        from ..models.presence_check import PresenceCheck  # noqa: PLC0415
        from ..models.spf_check import SpfCheck  # noqa: PLC0415

        d = dict(src_dict)
        spf = SpfCheck.from_dict(d.pop("spf"))

        dkim = DkimCheck.from_dict(d.pop("dkim"))

        dmarc = DmarcCheck.from_dict(d.pop("dmarc"))

        mx = PresenceCheck.from_dict(d.pop("mx"))

        mta_sts = PresenceCheck.from_dict(d.pop("mta_sts"))

        tls_rpt = PresenceCheck.from_dict(d.pop("tls_rpt"))

        bimi = PresenceCheck.from_dict(d.pop("bimi"))

        readiness_checks = cls(
            spf=spf,
            dkim=dkim,
            dmarc=dmarc,
            mx=mx,
            mta_sts=mta_sts,
            tls_rpt=tls_rpt,
            bimi=bimi,
        )

        readiness_checks.additional_properties = d
        return readiness_checks

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
