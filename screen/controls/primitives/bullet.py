from screen.utils import decimal_to_latin, decimal_to_roman
from screen.utils.internal import Enum


class Bullet(Enum, __call__=lambda s, a: s.value(a)):
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

    decimal = str
    latin_lower = decimal_to_latin
    latin_upper = lambda s: decimal_to_latin(s).upper()
    none = lambda _: ""
    roman_lower = decimal_to_roman
    roman_upper = lambda s: decimal_to_roman(s).upper()


__all__ = [
    "Bullet",
]
