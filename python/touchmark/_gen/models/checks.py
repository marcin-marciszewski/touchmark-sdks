from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain_check import DomainCheck
    from ..models.mailbox_check import MailboxCheck


T = TypeVar("T", bound="Checks")


@_attrs_define
class Checks:
    """
    Attributes:
        syntax (bool):
        domain (DomainCheck | None):
        disposable (bool):
        free_provider (bool):
        role_account (bool):
        mailbox (MailboxCheck):
    """

    syntax: bool
    domain: DomainCheck | None
    disposable: bool
    free_provider: bool
    role_account: bool
    mailbox: MailboxCheck
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_check import DomainCheck  # noqa: PLC0415

        syntax = self.syntax

        domain: dict[str, Any] | None
        if isinstance(self.domain, DomainCheck):
            domain = self.domain.to_dict()
        else:
            domain = self.domain

        disposable = self.disposable

        free_provider = self.free_provider

        role_account = self.role_account

        mailbox = self.mailbox.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syntax": syntax,
                "domain": domain,
                "disposable": disposable,
                "free_provider": free_provider,
                "role_account": role_account,
                "mailbox": mailbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_check import DomainCheck  # noqa: PLC0415
        from ..models.mailbox_check import MailboxCheck  # noqa: PLC0415

        d = dict(src_dict)
        syntax = d.pop("syntax")

        def _parse_domain(data: object) -> DomainCheck | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                domain_type_0 = DomainCheck.from_dict(data)

                return domain_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainCheck | None, data)

        domain = _parse_domain(d.pop("domain"))

        disposable = d.pop("disposable")

        free_provider = d.pop("free_provider")

        role_account = d.pop("role_account")

        mailbox = MailboxCheck.from_dict(d.pop("mailbox"))

        checks = cls(
            syntax=syntax,
            domain=domain,
            disposable=disposable,
            free_provider=free_provider,
            role_account=role_account,
            mailbox=mailbox,
        )

        checks.additional_properties = d
        return checks

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
