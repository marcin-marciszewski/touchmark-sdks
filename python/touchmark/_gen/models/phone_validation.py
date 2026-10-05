from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phone_validation_reason_type_0 import PhoneValidationReasonType0
from ..models.phone_validation_type_type_0 import PhoneValidationTypeType0

if TYPE_CHECKING:
    from ..models.phone_country import PhoneCountry
    from ..models.phone_validation_datasets import PhoneValidationDatasets


T = TypeVar("T", bound="PhoneValidation")


@_attrs_define
class PhoneValidation:
    """
    Attributes:
        valid (bool): The number fits its country's numbering plan. This does not mean it is assigned, in service or
            reachable.
        reason (None | PhoneValidationReasonType0): Why the number is not valid.
        e164 (None | str):
        international (None | str):
        national (None | str):
        extension (None | str):
        country (None | PhoneCountry):
        calling_code (int | None):
        type_ (None | PhoneValidationTypeType0): Line type from the numbering plan. Plans that do not separate mobile
            ranges, such as the North American plan, answer fixed_line_or_mobile.
        original_carrier (None | str): The network the number range was first allocated to. Numbers move between
            networks, so this is not necessarily the current one.
        region (None | str): The area of a landline range, such as a city. It describes the number range, never where a
            person is.
        time_zones (list[str]):
        datasets (PhoneValidationDatasets): The version of the numbering-plan data used.
    """

    valid: bool
    reason: None | PhoneValidationReasonType0
    e164: None | str
    international: None | str
    national: None | str
    extension: None | str
    country: None | PhoneCountry
    calling_code: int | None
    type_: None | PhoneValidationTypeType0
    original_carrier: None | str
    region: None | str
    time_zones: list[str]
    datasets: PhoneValidationDatasets
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.phone_country import PhoneCountry  # noqa: PLC0415

        valid = self.valid

        reason: None | str
        if isinstance(self.reason, PhoneValidationReasonType0):
            reason = self.reason.value
        else:
            reason = self.reason

        e164: None | str
        e164 = self.e164

        international: None | str
        international = self.international

        national: None | str
        national = self.national

        extension: None | str
        extension = self.extension

        country: dict[str, Any] | None
        if isinstance(self.country, PhoneCountry):
            country = self.country.to_dict()
        else:
            country = self.country

        calling_code: int | None
        calling_code = self.calling_code

        type_: None | str
        if isinstance(self.type_, PhoneValidationTypeType0):
            type_ = self.type_.value
        else:
            type_ = self.type_

        original_carrier: None | str
        original_carrier = self.original_carrier

        region: None | str
        region = self.region

        time_zones = self.time_zones

        datasets = self.datasets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
                "reason": reason,
                "e164": e164,
                "international": international,
                "national": national,
                "extension": extension,
                "country": country,
                "calling_code": calling_code,
                "type": type_,
                "original_carrier": original_carrier,
                "region": region,
                "time_zones": time_zones,
                "datasets": datasets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_country import PhoneCountry  # noqa: PLC0415
        from ..models.phone_validation_datasets import (
            PhoneValidationDatasets,  # noqa: PLC0415
        )

        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_reason(data: object) -> None | PhoneValidationReasonType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0 = PhoneValidationReasonType0(data)

                return reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PhoneValidationReasonType0, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_e164(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        e164 = _parse_e164(d.pop("e164"))

        def _parse_international(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        international = _parse_international(d.pop("international"))

        def _parse_national(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        national = _parse_national(d.pop("national"))

        def _parse_extension(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        extension = _parse_extension(d.pop("extension"))

        def _parse_country(data: object) -> None | PhoneCountry:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_type_0 = PhoneCountry.from_dict(data)

                return country_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PhoneCountry, data)

        country = _parse_country(d.pop("country"))

        def _parse_calling_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        calling_code = _parse_calling_code(d.pop("calling_code"))

        def _parse_type_(data: object) -> None | PhoneValidationTypeType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = PhoneValidationTypeType0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PhoneValidationTypeType0, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_original_carrier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_carrier = _parse_original_carrier(d.pop("original_carrier"))

        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))

        time_zones = cast(list[str], d.pop("time_zones"))

        datasets = PhoneValidationDatasets.from_dict(d.pop("datasets"))

        phone_validation = cls(
            valid=valid,
            reason=reason,
            e164=e164,
            international=international,
            national=national,
            extension=extension,
            country=country,
            calling_code=calling_code,
            type_=type_,
            original_carrier=original_carrier,
            region=region,
            time_zones=time_zones,
            datasets=datasets,
        )

        phone_validation.additional_properties = d
        return phone_validation

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
