from enum import Enum


class DealType(str, Enum):
    REGULAR = "regular"


class DealStatus(str, Enum):
    CREATED = "Created"
    DENY_PERFORMER = "DenyPerformer"
    IN_PROCESS = "InProcess"
    CLOSE = "Close"
    ARB_CLOSE_CUSTOMER = "ArbCloseCustomer"
    ARB_CLOSE_PERFORMER = "ArbClosePerfomer"


class Currency(str, Enum):
    DOLLAR = "dollar"
