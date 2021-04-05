from typing import Optional

from screen.controls import Control, property
from screen.controls.primitives import Boundary, Case, HorizontalAlignment, VerticalAlignment


class Text(Control):
    """
    Represents a control used to display text.
    """

    # fmt: off
    case                      = property(Case,                Case.normal,              True,  True,  True)
    content                   = property(str,                 None,                     False, True,  True)
    horizontal_text_alignment = property(HorizontalAlignment, HorizontalAlignment.left, True,  False, True)
    is_editable               = property(bool,                False,                    True,  False, False)
    max_length                = property(Optional[int],       None,                     True,  True,  True)
    trim_boundary             = property(Boundary,            Boundary.word,            True,  False, True)
    vertical_text_alignment   = property(VerticalAlignment,   VerticalAlignment.top,    True,  False, True)
    wrap_boundary             = property(Boundary,            Boundary.word,            True,  True,  True)
    # fmt: on

    def measure_core(self, h, w):
        raise NotImplementedError

    def render_core(self, h, w):
        raise NotImplementedError


__all__ = [
    "Text",
]
