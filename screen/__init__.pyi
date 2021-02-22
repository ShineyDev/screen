from typing import NamedTuple

from screen.drawing import *


class _VersionInfo(NamedTuple):
    major: int
    minor: int
    patch: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
