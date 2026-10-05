from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lookup_response_scope import LookupResponseScope
from ..models.lookup_response_version import LookupResponseVersion

if TYPE_CHECKING:
    from ..models.asn import Asn
    from ..models.country import Country
    from ..models.lookup_response_datasets import LookupResponseDatasets
    from ..models.network import Network


T = TypeVar("T", bound="LookupResponse")


@_attrs_define
class LookupResponse:
    """
    Attributes:
        ip (str): The address in normalised form.
        version (LookupResponseVersion):
        scope (LookupResponseScope): Anything but global skips every dataset: the other fields are null.
        country (Country | None): Geolocation estimate at country level (DB-IP).
        continent (None | str): Two-letter continent code.
        asn (Asn | None):
        network (Network | None):
        tor_exit (bool | None): Null for IPv6: the Tor exit list holds IPv4 addresses only.
        datasets (LookupResponseDatasets): The version of each dataset read; null for one not loaded yet.
        credits_charged (int):
        request_id (str):
    """

    ip: str
    version: LookupResponseVersion
    scope: LookupResponseScope
    country: Country | None
    continent: None | str
    asn: Asn | None
    network: Network | None
    tor_exit: bool | None
    datasets: LookupResponseDatasets
    credits_charged: int
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asn import Asn  # noqa: PLC0415
        from ..models.country import Country  # noqa: PLC0415
        from ..models.network import Network  # noqa: PLC0415

        ip = self.ip

        version = self.version.value

        scope = self.scope.value

        country: dict[str, Any] | None
        if isinstance(self.country, Country):
            country = self.country.to_dict()
        else:
            country = self.country

        continent: None | str
        continent = self.continent

        asn: dict[str, Any] | None
        if isinstance(self.asn, Asn):
            asn = self.asn.to_dict()
        else:
            asn = self.asn

        network: dict[str, Any] | None
        if isinstance(self.network, Network):
            network = self.network.to_dict()
        else:
            network = self.network

        tor_exit: bool | None
        tor_exit = self.tor_exit

        datasets = self.datasets.to_dict()

        credits_charged = self.credits_charged

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
                "version": version,
                "scope": scope,
                "country": country,
                "continent": continent,
                "asn": asn,
                "network": network,
                "tor_exit": tor_exit,
                "datasets": datasets,
                "credits_charged": credits_charged,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asn import Asn  # noqa: PLC0415
        from ..models.country import Country  # noqa: PLC0415
        from ..models.lookup_response_datasets import (
            LookupResponseDatasets,  # noqa: PLC0415
        )
        from ..models.network import Network  # noqa: PLC0415

        d = dict(src_dict)
        ip = d.pop("ip")

        version = LookupResponseVersion(d.pop("version"))

        scope = LookupResponseScope(d.pop("scope"))

        def _parse_country(data: object) -> Country | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_type_0 = Country.from_dict(data)

                return country_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Country | None, data)

        country = _parse_country(d.pop("country"))

        def _parse_continent(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        continent = _parse_continent(d.pop("continent"))

        def _parse_asn(data: object) -> Asn | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asn_type_0 = Asn.from_dict(data)

                return asn_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Asn | None, data)

        asn = _parse_asn(d.pop("asn"))

        def _parse_network(data: object) -> Network | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                network_type_0 = Network.from_dict(data)

                return network_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Network | None, data)

        network = _parse_network(d.pop("network"))

        def _parse_tor_exit(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        tor_exit = _parse_tor_exit(d.pop("tor_exit"))

        datasets = LookupResponseDatasets.from_dict(d.pop("datasets"))

        credits_charged = d.pop("credits_charged")

        request_id = d.pop("request_id")

        lookup_response = cls(
            ip=ip,
            version=version,
            scope=scope,
            country=country,
            continent=continent,
            asn=asn,
            network=network,
            tor_exit=tor_exit,
            datasets=datasets,
            credits_charged=credits_charged,
            request_id=request_id,
        )

        lookup_response.additional_properties = d
        return lookup_response

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
