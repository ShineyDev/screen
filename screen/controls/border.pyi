from typing import ClassVar, Optional

from screen.controls import Control, Text
from screen.controls.primitives import Thickness


class Border(Control):
    default_header: ClassVar[Optional[Text]]
    default_thickness: ClassVar[Thickness]

    def __init__(
        self,
        *,
        child: Control,
        header: Text=...,
        thickness: Thickness=...,
        **kwargs,
    ) -> None: ...

    @property
    def child(self) -> Control: ...
    @child.setter
    def child(self, value: Control) -> None: ...
    @property
    def header(self) -> Optional[Text]: ...
    @header.setter
    def header(self, value: Optional[Text]) -> None: ...
    @property
    def thickness(self) -> Thickness: ...
    @thickness.setter
    def thickness(self, value: Optional[Thickness]) -> None: ...
