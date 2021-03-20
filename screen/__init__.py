import collections

from screen import controls
from screen import drawing
from screen import utils


__all__ = [
    "controls",
    "drawing",
    "utils",
]


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "0.4.0a"
version_info = _VersionInfo(0, 4, 0, "alpha", 0)
