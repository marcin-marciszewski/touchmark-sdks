from enum import StrEnum


class IpLookupScope(StrEnum):
    GLOBAL = "global"
    LINK_LOCAL = "link_local"
    LOOPBACK = "loopback"
    MULTICAST = "multicast"
    PRIVATE = "private"
    RESERVED = "reserved"
    SHARED = "shared"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)
