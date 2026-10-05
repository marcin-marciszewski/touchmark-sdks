from enum import StrEnum


class MailboxCheckStatus(StrEnum):
    CATCH_ALL = "catch_all"
    EXISTS = "exists"
    NOT_CHECKED = "not_checked"
    NOT_EXISTS = "not_exists"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
