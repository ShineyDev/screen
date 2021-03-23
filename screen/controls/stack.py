from typing import List, Union

from screen.controls import Control, property
from screen.controls.primitives import Bullet, Orientation


def _bullet_invalidate_measure(before, after):
    return not (isinstance(before, str) and isinstance(after, str) and len(before) == len(after))


class Stack(Control):
    """
    Represents a control used to display a stack of controls.
    """

    # fmt: off
    bullet      = property(Union[Bullet, str], Bullet.none,            True,  _bullet_invalidate_measure, True)
    children    = property(List[Control],      None,                   False, True,                       True)
    orientation = property(Orientation,        Orientation.horizontal, True,  True,                       True)
    spacing     = property(int,                0,                      True,  True,                       True)
    # fmt: on

    def measure_core(self, h, w, **kwargs):
        raise NotImplementedError

    def render_core(self, h, w, **kwargs):
        raise NotImplementedError


__all__ = [
    "Stack",
]
