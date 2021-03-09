from typing import NamedTuple


class _VersionInfo(NamedTuple):
    major: int
    minor: int
    patch: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
