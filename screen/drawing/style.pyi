class Style:
    reset: Style
    intensity_increased: Style
    intensity_decreased: Style
    italic_on: Style
    underline_on: Style
    blink_slow_on: Style
    blink_fast_on: Style
    invert_on: Style
    conceal_on: Style
    strikethrough_on: Style
    underline_double_on: Style
    intensity_normal: Style
    italic_off: Style
    underline_off: Style
    blink_off: Style
    invert_off: Style
    conceal_off: Style
    strikethrough_off: Style
    reset_foreground_color: Style
    reset_background_color: Style
    overline_on: Style
    overline_off: Style

    reset_color: Style

    def __init__(self, *values: int) -> None: ...
