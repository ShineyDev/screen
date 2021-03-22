from enum import IntEnum


class Boundary(IntEnum):
    """
    Represents a text boundary.

    Attributes
    ----------
    character
        The character boundary.
    word
        The word boundary.
    """

    character = 1
    word = 2


__all__ = [
    "Boundary",
]
