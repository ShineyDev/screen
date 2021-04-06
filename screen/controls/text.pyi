from typing import ClassVar, Optional

from screen.controls import Control
from screen.controls.primitives import Boundary, Case, HorizontalAlignment, VerticalAlignment


class Text(Control):
    default_case: ClassVar[Case]
    default_horizontal_text_alignment: ClassVar[HorizontalAlignment]
    default_trim_boundary: ClassVar[Boundary]
    default_vertical_text_alignment: ClassVar[VerticalAlignment]
    default_wrap_boundary: ClassVar[Boundary]

    def __init__(
        self,
        *,
        content: str,
        case: Case=...,
        horizontal_text_alignment: HorizontalAlignment=...,
        trim_boundary: Boundary=...,
        vertical_text_alignment: VerticalAlignment=...,
        wrap_boundary: Boundary=...,
        **kwargs,
    ) -> None: ...

    @property
    def case(self) -> Case: ...
    @case.setter
    def case(self, value: Optional[Case]) -> None: ...
    @property
    def content(self) -> str: ...
    @content.setter
    def content(self, value: str) -> None: ...
    @property
    def horizontal_text_alignment(self) -> HorizontalAlignment: ...
    @horizontal_text_alignment.setter
    def horizontal_text_alignment(self, value: Optional[HorizontalAlignment]) -> None: ...
    @property
    def trim_boundary(self) -> Boundary: ...
    @trim_boundary.setter
    def trim_boundary(self, value: Optional[Boundary]) -> None: ...
    @property
    def vertical_text_alignment(self) -> VerticalAlignment: ...
    @vertical_text_alignment.setter
    def vertical_text_alignment(self, value: Optional[VerticalAlignment]) -> None: ...
    @property
    def wrap_boundary(self) -> Boundary: ...
    @wrap_boundary.setter
    def wrap_boundary(self, value: Optional[Boundary]) -> None: ...
