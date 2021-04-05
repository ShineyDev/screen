from screen.controls import Control, property
from screen.controls.primitives import Placement


class Popup(Control):
    """
    Represents a pop-up control.
    """

    # fmt: off
    child             = property(Control,   None,             False, True,  True)
    horizontal_offset = property(int,       0,                True,  False, False)
    placement         = property(Placement, Placement.cursor, True,  False, False)
    vertical_offset   = property(int,       0,                True,  False, False)
    # fmt: on

    def measure_core(self, h, w):
        raise NotImplementedError

    def render_core(self, h, w):
        raise NotImplementedError


__all__ = [
    "Popup",
]
