import collections

from screen.drawing import *
from screen.drawing import __all__ as _drawing__all__


__all__ = [
    "drawing",
    *_drawing__all__,
]


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor patch release serial")

version = "0.2.0a"
version_info = _VersionInfo(0, 2, 0, "alpha", 0)
