from typing import ClassVar, Tuple


class Style:
    reset: ClassVar[Style]
    intensity_increased: ClassVar[Style]
    intensity_decreased: ClassVar[Style]
    italic_on: ClassVar[Style]
    underline_on: ClassVar[Style]
    blink_slow_on: ClassVar[Style]
    blink_fast_on: ClassVar[Style]
    invert_on: ClassVar[Style]
    conceal_on: ClassVar[Style]
    strikethrough_on: ClassVar[Style]
    underline_double_on: ClassVar[Style]
    intensity_normal: ClassVar[Style]
    italic_off: ClassVar[Style]
    underline_off: ClassVar[Style]
    blink_off: ClassVar[Style]
    invert_off: ClassVar[Style]
    conceal_off: ClassVar[Style]
    strikethrough_off: ClassVar[Style]
    reset_foreground_color: ClassVar[Style]
    reset_background_color: ClassVar[Style]
    overline_on: ClassVar[Style]
    overline_off: ClassVar[Style]
    reset_color: ClassVar[Style]

    values: Tuple[int, ...]

    def __init__(self, *values: int) -> None: ...
