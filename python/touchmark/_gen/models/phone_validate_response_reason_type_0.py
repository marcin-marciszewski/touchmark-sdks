from enum import StrEnum


class PhoneValidateResponseReasonType0(StrEnum):
    INVALID_COUNTRY_CODE = "invalid_country_code"
    INVALID_LENGTH = "invalid_length"
    NOT_A_NUMBER = "not_a_number"
    NOT_IN_PLAN = "not_in_plan"
    NO_COUNTRY_CODE = "no_country_code"
    TOO_LONG = "too_long"
    TOO_SHORT = "too_short"

    def __str__(self) -> str:
        return str(self.value)
