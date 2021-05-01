import colorsys
import math


def distance(*pairs):
    """
    Calculates euclidean distance.

    Parameters
    ----------
    *pairs: Tuple[:class:`int`, :class:`int`]
        An iterable of pairs to compare.

    Returns
    -------
    :class:`float`
        The euclidean distance.
    """

    return math.sqrt(sum((p[0] - p[1]) ** 2 for p in pairs))


def hsl_to_rgb(h, s, l):
    """
    Converts HSL to RGB.

    Parameters
    ----------
    h: :class:`int`
        The hue value in the range ``[0, 360]``.
    s: :class:`float`
        The saturation value in the range ``[0, 1]``.
    l: :class:`float`
        The lightness value in the range ``[0, 1]``.

    Returns
    -------
    Tuple[:class:`int`, :class:`int`, :class:`int`]
        The RGB tuple.
    """

    h /= 360

    r, g, b = colorsys.hls_to_rgb(h, l, s)

    r = int(round(r * 255, 0))
    g = int(round(g * 255, 0))
    b = int(round(b * 255, 0))

    return (r, g, b)


def hsv_to_rgb(h, s, v):
    """
    Converts HSV to RGB.

    Parameters
    ----------
    h: :class:`int`
        The hue value in the range ``[0, 360]``.
    s: :class:`float`
        The saturation value in the range ``[0, 1]``.
    v: :class:`float`
        The brightness value in the range ``[0, 1]``.

    Returns
    -------
    Tuple[:class:`int`, :class:`int`, :class:`int`]
        The RGB tuple.
    """

    h /= 360

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    r = int(round(r * 255, 0))
    g = int(round(g * 255, 0))
    b = int(round(b * 255, 0))

    return (r, g, b)


def rgb_to_hsl(r, g, b):
    """
    Converts RGB to HSL.

    Parameters
    ----------
    r: :class:`int`
        The red value in the range ``[0, 255]``.
    g: :class:`int`
        The green value in the range ``[0, 255]``.
    b: :class:`int`
        The blue value in the range ``[0, 255]``.

    Returns
    -------
    Tuple[:class:`int`, :class:`float`, :class:`float`]
        The HSL tuple.
    """

    r /= 255
    g /= 255
    b /= 255

    h, l, s = colorsys.rgb_to_hls(r, g, b)

    h = int(h * 360)

    return (h, s, l)


def rgb_to_hsv(r, g, b):
    """
    Converts RGB to HSV.

    Parameters
    ----------
    r: :class:`int`
        The red value in the range ``[0, 255]``.
    g: :class:`int`
        The green value in the range ``[0, 255]``.
    b: :class:`int`
        The blue value in the range ``[0, 255]``.

    Returns
    -------
    Tuple[:class:`int`, :class:`float`, :class:`float`]
        The HSV tuple.
    """

    r /= 255
    g /= 255
    b /= 255

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h = int(h * 360)

    return (h, s, v)


def interpolate(v1, v2, p):
    """
    Calculates linear interpolation.

    Parameters
    ----------
    v1: :class:`float`
        The start value.
    v2: :class:`float`
        The end value.
    p: :class:`float`
        The point along the line in the range ``[0, 1]``.

    Returns
    -------
    :class:`float`
        The interpolated value.
    """

    return (1 - p) * v1 + p * v2


__all__ = [
    "distance",
    "hsl_to_rgb",
    "hsv_to_rgb",
    "rgb_to_hsl",
    "rgb_to_hsv",
    "interpolate",
]
