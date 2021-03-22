from screen.controls import Control, property
from screen.controls.primitives import Boundary, HorizontalAlignment, VerticalAlignment


class Text(Control):
    """
    Represents a control used to display text.
    """

    # fmt: off
    content                   = property(str,                 None,                     False, True)
    horizontal_text_alignment = property(HorizontalAlignment, HorizontalAlignment.left, True,  False)
    is_editable               = property(bool,                False,                    True,  False)
    trim_boundary             = property(Boundary,            Boundary.word,            True,  False)
    vertical_text_alignment   = property(VerticalAlignment,   VerticalAlignment.top,    True,  False)
    wrap_boundary             = property(Boundary,            Boundary.word,            True,  False)
    # fmt: on

    def measure_core(self, h, w, **kwargs):
        raise NotImplementedError

    def render(self, h, w, **kwargs):
        raise NotImplementedError


__all__ = [
    "Text",
]
