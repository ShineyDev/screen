from screen.utils.internal import Enum


class Placement(Enum):
    """
    Represents the placement of a pop-up control.

    Attributes
    ----------
    cursor
        Place the control relative to the cursor position at the time
        of opening.
    parent
        Place the control relative to the parent control.
    screen
        Place the control relative to the screen.
    """

    cursor = 1
    parent = 2
    screen = 3


__all__ = [
    "Placement",
]
