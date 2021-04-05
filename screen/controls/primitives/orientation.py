from screen.utils.internal import Enum


class Orientation(Enum):
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


__all__ = [
    "Orientation",
]
