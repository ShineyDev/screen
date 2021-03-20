from typing import ClassVar, Optional

from screen.controls import Control
from screen.controls.primitives import Placement


class Popup(Control):
    default_horizontal_offset: ClassVar[int]
    default_placement: ClassVar[Placement]
    default_vertical_offset: ClassVar[int]

    def __init__(
        self,
        *,
        horizontal_offset: int,
        placement: Placement,
        vertical_offset: int,
        **kwargs,
    ) -> None: ...

    @property
    def horizontal_offset(self) -> int: ...
    @horizontal_offset.setter
    def horizontal_offset(self, value: Optional[int]) -> None: ...
    @property
    def placement(self) -> Placement: ...
    @placement.setter
    def placement(self, value: Optional[Placement]) -> None: ...
    @property
    def vertical_offset(self) -> int: ...
    @vertical_offset.setter
    def vertical_offset(self, value: Optional[int]) -> None: ...
