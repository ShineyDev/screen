from typing import Type, TypeVar

from enum import IntEnum


C = TypeVar("C", bound=Color)


class ColorInterpolationMethod(IntEnum):
    hsl: int
    hsv: int
    rgb: int

class Color:
    value: int

    def __init__(self, value: int) -> None: ...

    @classmethod
    def from_argb(cls: Type[C], a: float, r: int, g: int, b: int) -> C: ...
    @classmethod
    def from_hsl(cls: Type[C], h: int, s: float, l: float) -> C: ...
    @classmethod
    def from_hsv(cls: Type[C], h: int, s: float, v: float) -> C: ...
    @classmethod
    def from_rgb(cls: Type[C], r: int, g: int, b: int) -> C: ...

    @property
    def a(self) -> float: ...
    @property
    def r(self) -> int: ...
    @property
    def g(self) -> int: ...
    @property
    def b(self) -> int: ...

    @staticmethod
    def interpolate(c1: Color, c2: Color, p: float, *, method: ColorInterpolationMethod=...) -> Color: ...
