from screen.utils.internal import Enum


class ColorInterpolationMethod(Enum):
    """
    Represents the method used to interpolate a color.

    Attributes
    ----------
    hsl
        Interpolate via HSL values.
    hsv
        Interpolate via HSV values.
    rgb
        Interpolate via RGB values.
    """

    hsl = 1
    hsv = 2
    rgb = 3


__all__ = [
    "ColorInterpolationMethod",
]
