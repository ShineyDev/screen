from typing import ClassVar, Type, TypeVar

from enum import IntEnum


C = TypeVar("C", bound=Color)


class ColorInterpolationMethod(IntEnum):
    hsl: int
    hsv: int
    rgb: int

class Color:
    black: ClassVar[Color]
    blue: ClassVar[Color]
    bright_black: ClassVar[Color]
    bright_blue: ClassVar[Color]
    bright_cyan: ClassVar[Color]
    bright_green: ClassVar[Color]
    bright_magenta: ClassVar[Color]
    bright_red: ClassVar[Color]
    bright_yellow: ClassVar[Color]
    bright_white: ClassVar[Color]
    cyan: ClassVar[Color]
    green: ClassVar[Color]
    magenta: ClassVar[Color]
    red: ClassVar[Color]
    transparent: ClassVar[Color]
    yellow: ClassVar[Color]
    white: ClassVar[Color]

    value: int

    def __init__(self, value: int) -> None: ...

    @classmethod
    def from_ahsl(cls: Type[C], a: float, h: int, s: float, l: float) -> C: ...
    @classmethod
    def from_ahsv(cls: Type[C], a: float, h: int, s: float, v: float) -> C: ...
    @classmethod
    def from_argb(cls: Type[C], a: float, r: int, g: int, b: int) -> C: ...
    @classmethod
    def from_hsl(cls: Type[C], h: int, s: float, l: float) -> C: ...
    @classmethod
    def from_hsv(cls: Type[C], h: int, s: float, v: float) -> C: ...
    @classmethod
    def from_rgb(cls: Type[C], r: int, g: int, b: int) -> C: ...
    @classmethod
    def from_random(cls: Type[C]) -> C:...
    @classmethod
    def from_random_ahsl(cls: Type[C], a: float=..., h: int=..., s: float=..., l: float=...) -> C: ...
    @classmethod
    def from_random_ahsv(cls: Type[C], a: float=..., h: int=..., s: float=..., v: float=...) -> C: ...
    @classmethod
    def from_random_argb(cls: Type[C], a: float=..., r: int=..., g: int=..., b: int=...) -> C: ...
    @classmethod
    def from_random_hsl(cls: Type[C], h: int=..., s: float=..., l: float=...) -> C: ...
    @classmethod
    def from_random_hsv(cls: Type[C], h: int, s: float=..., v: float=...) -> C: ...
    @classmethod
    def from_random_rgb(cls: Type[C], r: int=..., g: int=..., b: int=...) -> C: ...

    @property
    def a(self) -> float: ...
    @property
    def r(self) -> int: ...
    @property
    def g(self) -> int: ...
    @property
    def b(self) -> int: ...

    @classmethod
    def distance(cls: Type[C], c1: Color, c2: Color) -> float: ...
    @classmethod
    def interpolate(cls: Type[C], c1: Color, c2: Color, p: float, *, method: ColorInterpolationMethod=...) -> C: ...
