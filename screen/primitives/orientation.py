from enum import IntEnum


class Orientation(IntEnum):
    """
    Represents the orientation of a control.

    Attributes
    ----------
    horizontal
        Orient horizontally; stack children side-by-side.
    vertical
        Orient vertically; stack children on top of one another.
    """

    horizontal = 1
    vertical = 2