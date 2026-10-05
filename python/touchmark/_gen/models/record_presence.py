from enum import StrEnum


class RecordPresence(StrEnum):
    ABSENT = "absent"
    PRESENT = "present"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
