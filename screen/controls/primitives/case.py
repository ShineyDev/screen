from screen.utils.internal import Enum


class Case(Enum, __call__=lambda s, a: s.value(a)):
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

    capital = str.capitalize
    fold = str.casefold
    lower = str.lower
    normal = lambda s: s
    swap = str.swapcase
    title = str.title
    upper = str.upper


__all__ = [
    "Case",
]
