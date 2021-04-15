from typing import Optional

from .text import Text
from screen.controls import Control, property
from screen.controls.primitives import Thickness
from screen.utils import len


class Border(Control):
    """
    Represents a control used to display a border around another.

    |parameters|

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two :class:`~.Border` objects.

        .. describe:: hash(x)

            Returns the hash of the :class:`~.Border` object.
    """

    # fmt: off
    child     = property(Control,        None,         True,  True,                          True)
    header    = property(Optional[Text], None,         False, lambda b, a: len(b) != len(a), True)
    thickness = property(Thickness,      Thickness(1), False, True,                          True)
    # fmt: on

    def measure_core(self, h, w):
        raise NotImplementedError

    def render_core(self, h, w):
        raise NotImplementedError


__all__ = [
    "Border",
]
