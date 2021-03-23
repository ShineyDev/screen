from typing import ClassVar, List, Optional, Union

from screen.controls import Control
from screen.controls.primitives import Bullet


class Stack(Control):
    default_bullet: ClassVar[Union[Bullet, str]]
    default_spacing: ClassVar[int]

    def __init__(
        self,
        *,
        children: List[Control],
        bullet: Union[Bullet, str]=...,
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
    def spacing(self) -> int: ...
    @spacing.setter
    def spacing(self, value: Optional[int]) -> None: ...
