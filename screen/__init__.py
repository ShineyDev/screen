import collections

from screen import controls
from screen import drawing
from screen import primitives
from screen import utils


__all__ = [
    "controls",
    "drawing",
    "primitives",
]


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "0.3.0a"
version_info = _VersionInfo(0, 3, 0, "alpha", 0)
