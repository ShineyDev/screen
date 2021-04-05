from typing import Callable

from enum import Enum


class Bullet(Enum):
    decimal: Callable[[int], str]
    latin_lower: Callable[[int], str]
    latin_upper: Callable[[int], str]
    none: Callable[[int], str]
    roman_lower: Callable[[int], str]
    roman_upper: Callable[[int], str]
