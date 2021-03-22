from enum import IntEnum


class Bullet(IntEnum):
    """
    Represents a dynamic bullet type.

    Attributes
    ----------
    decimal
        1, 2, 3, 4, 5, ...
    latin_lower
        a, b, c, d, e, ..., aa, ab, ac, ...
    latin_upper
        A, B, C, D, E, ..., AA, AB, AC, ...
    none
        No bullet. Identical to ``bullet=""``.
    roman_lower
        i, ii, iii, iv, v, ...
    roman_upper
        I, II, III, IV, V, ...
    """

    decimal = 1
    latin_lower = 2
    latin_upper = 3
    none = 4
    roman_lower = 5
    roman_upper = 6


__all__ = [
    "Bullet",
]
