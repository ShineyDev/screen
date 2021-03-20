from typing import Any, Callable, ClassVar, Iterator, NamedTuple, Optional, Type, Union

from screen.controls.primitives import HorizontalAlignment
from screen.controls.primitives import Thickness
from screen.controls.primitives import VerticalAlignment
from screen.drawing import Color


class property(NamedTuple):
    type: Type[Any]
    default: Optional[Any]
    optional: bool
    remeasure: Union[bool, Callable[[Any, Any], bool]]


class Control:
    default_background: ClassVar[Optional[Color]]
    default_foreground: ClassVar[Optional[Color]]
    default_height: ClassVar[Optional[int]]
    default_horizontal_alignment: ClassVar[HorizontalAlignment]
    default_is_resizable: ClassVar[bool]
    default_layer: ClassVar[int]
    default_margin: ClassVar[Thickness]
    default_max_height: ClassVar[Optional[int]]
    default_max_width: ClassVar[Optional[int]]
    default_min_height: ClassVar[Optional[int]]
    default_min_width: ClassVar[Optional[int]]
    default_padding: ClassVar[Thickness]
    default_vertical_alignment: ClassVar[VerticalAlignment]
    default_width: ClassVar[Optional[int]]

    def __init__(
        self,
        *,
        background: Color=...,
        foreground: Color=...,
        height: int=...,
        horizontal_alignment: HorizontalAlignment=...,
        is_resizable: bool=...,
        layer: int=...,
        margin: Thickness=...,
        max_height: int=...,
        max_width: int=...,
        min_height: int=...,
        min_width: int=...,
        padding: Thickness=...,
        vertical_alignment: VerticalAlignment=...,
        width: int=...,
    ) -> None: ...

    @property
    def background(self) -> Optional[Color]: ...
    @background.setter
    def background(self, value: Optional[Color]) -> None: ...
    @property
    def foreground(self) -> Optional[Color]: ...
    @foreground.setter
    def foreground(self, value: Optional[Color]) -> None: ...
    @property
    def height(self) -> Optional[int]: ...
    @height.setter
    def height(self, value: Optional[int]) -> None: ...
    @property
    def horizontal_alignment(self) -> HorizontalAlignment: ...
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: Optional[HorizontalAlignment]) -> None: ...
    @property
    def is_resizable(self) -> bool: ...
    @is_resizable.setter
    def is_resizable(self, value: Optional[bool]) -> None: ...
    @property
    def layer(self) -> int: ...
    @layer.setter
    def layer(self, value: Optional[int]) -> None: ...
    @property
    def margin(self) -> Thickness: ...
    @margin.setter
    def margin(self, value: Optional[Thickness]) -> None: ...
    @property
    def max_height(self) -> int: ...
    @max_height.setter
    def max_height(self, value: Optional[int]) -> None: ...
    @property
    def max_width(self) -> int: ...
    @max_width.setter
    def max_width(self, value: Optional[int]) -> None: ...
    @property
    def min_height(self) -> int: ...
    @min_height.setter
    def min_height(self, value: Optional[int]) -> None: ...
    @property
    def min_width(self) -> int: ...
    @min_width.setter
    def min_width(self, value: Optional[int]) -> None: ...
    @property
    def padding(self) -> Thickness: ...
    @padding.setter
    def padding(self, value: Optional[Thickness]) -> None: ...
    @property
    def vertical_alignment(self) -> VerticalAlignment: ...
    @vertical_alignment.setter
    def vertical_alignment(self, value: Optional[VerticalAlignment]) -> None: ...
    @property
    def width(self) -> Optional[int]: ...
    @width.setter
    def width(self, value: Optional[int]) -> None: ...

    def measure(self, h: int, w: int, **kwargs) -> tuple[int, int]: ...
    def measure_core(self, h: int, w: int, **kwargs) -> tuple[int, int]: ...
    def render(self, h: int, w: int, **kwargs) -> Iterator[str]: ...
