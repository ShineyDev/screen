from typing import Optional

from screen.controls import Control, property
from screen.controls.primitives import Boundary, Case, HorizontalAlignment, VerticalAlignment


class Text(Control):
    """
    Represents a control used to display text.

    |parameters|

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two :class:`~.Text` objects.

        .. describe:: hash(x)

            Returns the hash of the :class:`~.Text` object.
    """

    # fmt: off
    case                      = property(Case,                Case.normal,              False, True,  True)
    content                   = property(str,                 None,                     True,  True,  True)
    horizontal_text_alignment = property(HorizontalAlignment, HorizontalAlignment.left, False, False, True)
    trim_boundary             = property(Boundary,            Boundary.word,            False, False, True)
    vertical_text_alignment   = property(VerticalAlignment,   VerticalAlignment.top,    False, False, True)
    wrap_boundary             = property(Boundary,            Boundary.word,            False, True,  True)
    # fmt: on

    def measure_core(self, h, w):
        raise NotImplementedError

    def render_core(self, h, w):
        raise NotImplementedError


__all__ = [
    "Text",
]
