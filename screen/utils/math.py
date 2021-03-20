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
    "interpolate",
]
