from typing import List, Union

from .text import Text
from screen.controls import Control, property
from screen.controls.primitives import Bullet, Orientation
from screen.utils import len


class Stack(Control):
    """
    Represents a control used to display a stack of controls.

    |parameters|

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two :class:`~.Stack` objects.

        .. describe:: hash(x)

            Returns the hash of the :class:`~.Stack` object.
    """

    # fmt: off
    bullet      = property(Union[Bullet, Text], Bullet.none,            False, Text._invalidate_measure, True)
    children    = property(List[Control],       None,                   True,  True,                     True)
    orientation = property(Orientation,         Orientation.horizontal, False, True,                     True)
    spacing     = property(int,                 0,                      False, True,                     True)
    # fmt: on

    def measure_core(self, h, w):
        raise NotImplementedError

    def render_core(self, h, w):
        raise NotImplementedError


__all__ = [
    "Stack",
]
