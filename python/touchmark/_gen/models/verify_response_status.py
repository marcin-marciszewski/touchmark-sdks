from enum import StrEnum


class VerifyResponseStatus(StrEnum):
    DONE = "done"
    QUEUED = "queued"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
