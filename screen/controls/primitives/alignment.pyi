from enum import Enum


class HorizontalAlignment(Enum):
    left: int
    center: int
    right: int
    stretch: int

class VerticalAlignment(Enum):
    top: int
    center: int
    bottom: int
    stretch: int
