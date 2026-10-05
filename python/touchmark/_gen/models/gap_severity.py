from enum import StrEnum


class GapSeverity(StrEnum):
    BLOCKER = "blocker"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
