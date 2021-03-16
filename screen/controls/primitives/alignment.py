from enum import IntEnum


class HorizontalAlignment(IntEnum):
    """
    Represents the horizontal alignment of a control.

    Attributes
    ----------
    left
        Align to left.
    center
        Align to center.
    right
        Align to right.
    stretch
        Stretch to fit.
    """

    left = 1
    center = 2
    right = 3
    stretch = 4


class VerticalAlignment(IntEnum):
    """
    Represents the vertical alignment of a control.

    Attributes
    ----------
    top
        Align to top.
    center
        Align to center.
    bottom
        Align to bottom.
    stretch
        Stretch to fit.
    """

    top = 1
    center = 2
    bottom = 3
    stretch = 4
