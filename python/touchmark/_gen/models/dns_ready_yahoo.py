from enum import StrEnum


class DnsReadyYahoo(StrEnum):
    FAIL = "fail"
    PASS = "pass"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
