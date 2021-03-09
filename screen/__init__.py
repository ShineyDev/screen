import collections


__all__ = [
    "drawing",
]


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "0.2.0a"
version_info = _VersionInfo(0, 2, 0, "alpha", 0)
