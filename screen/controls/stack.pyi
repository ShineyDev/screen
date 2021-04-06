from typing import ClassVar, List, Optional, Union

from screen.controls import Control
from screen.controls.primitives import Bullet, Orientation


class Stack(Control):
    default_bullet: ClassVar[Union[Bullet, str]]
    default_orientation: ClassVar[Orientation]
    default_spacing: ClassVar[int]

    def __init__(
        self,
        *,
        children: List[Control],
        bullet: Union[Bullet, str]=...,
        orientation: Orientation=...,
        spacing: int=...,
        **kwargs,
    ) -> None: ...

    @property
    def bullet(self) -> Union[Bullet, str]: ...
    @bullet.setter
    def bullet(self, value: Optional[Union[Bullet, str]]) -> None: ...
    @property
    def children(self) -> List[Control]: ...
    @children.setter
    def children(self, value: List[Control]) -> None: ...
    @property
    def orientation(self) -> Orientation: ...
    @orientation.setter
    def orientation(self, value: Optional[Orientation]) -> None: ...
    @property
    def spacing(self) -> int: ...
    @spacing.setter
    def spacing(self, value: Optional[int]) -> None: ...
