import collections

from screen.controls import *
from screen.controls import __all__ as _controls__all__


__all__ = [
    "controls",
    *_controls__all__,
    "drawing",
    "primitives",
]


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "0.3.0a"
version_info = _VersionInfo(0, 3, 0, "alpha", 0)
