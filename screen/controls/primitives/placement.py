from enum import IntEnum


class Placement(IntEnum):
    """
    Represents the placement of a pop-up control.

    Attributes
    ----------
    mouse
        Place the control relative to the mouse position at the time of
        opening.
    parent
        Place the control relative to the parent control.
    screen
        Place the control relative to the screen.
    """

    mouse = 1
    parent = 2
    screen = 3
