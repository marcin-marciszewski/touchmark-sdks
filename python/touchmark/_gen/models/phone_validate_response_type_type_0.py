from enum import StrEnum


class PhoneValidateResponseTypeType0(StrEnum):
    FIXED_LINE = "fixed_line"
    FIXED_LINE_OR_MOBILE = "fixed_line_or_mobile"
    MOBILE = "mobile"
    PAGER = "pager"
    PERSONAL_NUMBER = "personal_number"
    PREMIUM_RATE = "premium_rate"
    SHARED_COST = "shared_cost"
    TOLL_FREE = "toll_free"
    UAN = "uan"
    UNKNOWN = "unknown"
    VOICEMAIL = "voicemail"
    VOIP = "voip"

    def __str__(self) -> str:
        return str(self.value)
