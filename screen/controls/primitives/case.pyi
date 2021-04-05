from typing import Callable

from enum import Enum


class Case(Enum):
    capital: Callable[[str], str]
    fold: Callable[[str], str]
    lower: Callable[[str], str]
    normal: Callable[[str], str]
    swap: Callable[[str], str]
    title: Callable[[str], str]
    upper: Callable[[str], str]
