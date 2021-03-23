from enum import IntEnum


class Case(IntEnum):
    """
    Represents a character case.

    Attributes
    ----------
    capital
        :meth:`str.capitalize`
    fold
        :meth:`str.casefold`
    lower
        :meth:`str.lower`
    normal
        Text is displayed as-is.
    swap
        :meth:`str.swapcase`
    title
        :meth:`str.title`
    upper
        :meth:`str.upper`
    """

    capital = 1
    fold = 2
    lower = 3
    normal = 4
    swap = 5
    title = 6
    upper = 7


__all__ = [
    "Case",
]
