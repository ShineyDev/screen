from screen.utils.internal import AttributeFactoryMeta


class Style(metaclass=AttributeFactoryMeta):
    """
    Represents an ANSI SGR sequence.

    Parameters
    ----------
    *values: Iterable[:class:`int`]
        The style values.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares the :attr:`value <.values>` of ``x`` and ``y``.

        .. describe:: x + y

            Combines two :class:`.Style` objects (not unlike binary or)
            or combines a :class:`.Style` and a :class:`str` (and
            returns the new :class:`str`).

        .. describe:: x | y

            Combines the :attr:`value <.values>` of ``x`` and ``y``.
            Raises :class:`ArithmeticError` when combining with
            :attr:`.reset`.

        .. describe:: hash(x)

            Returns the hash of the style :attr:`value <.values>`.

    Attributes
    ----------
    values: Tuple[:class:`int`, ...]
        The style values.
    """

    def __attr_init__(cls, value):
        try:
            return cls(*value)
        except TypeError as e:
            return cls(value)

    reset = 0
    intensity_increased = 1
    intensity_decreased = 2
    italic_on = 3
    underline_on = 4
    blink_slow_on = 5
    blink_fast_on = 6
    invert_on = 7
    conceal_on = 8
    strikethrough_on = 9

    # [10-20] are font sequences

    underline_double_on = 21
    intensity_normal = 22
    italic_off = 23
    underline_off = 24
    blink_off = 25

    # monospace_on = 26

    invert_off = 27
    conceal_off = 28
    strikethrough_off = 29

    # [30-38] are foreground colors

    reset_foreground_color = 39

    # [40-48] are background colors

    reset_background_color = 49

    # monospace_off = 50
    # frame_on = 51
    # encircle_on = 52

    overline_on = 53

    # frame_off = 54

    overline_off = 55

    # [56-57] are unknown
    # 58 is underline color
    # reset_underline_color = 59
    # [60-64] are ideograms
    # ideogram_off = 65
    # [66-72] are unknown
    # superscript = 73
    # subscript = 74
    # [90-97] are bright foreground colors
    # [100-107] are bright background colors
    # [108-n] are unknown

    reset_color = (reset_foreground_color, reset_background_color)

    __slots__ = ("values",)

    def __init__(self, *values):
        self.values = tuple(set(values))

    def __hash__(self):
        return hash(self.values)

    def __repr__(self):
        value = self.build()
        return f"<{self.__class__.__name__} \\ESC{value[1:]}\x1B[0m>"

    def __str__(self):
        return self.build()

    def __add__(self, other):
        if isinstance(other, str):
            return self.build() + other
        elif isinstance(other, self.__class__):
            return self.__or__(other)

        return NotImplemented

    __radd__ = __add__

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.values == other.values

    def __or__(self, other):
        cls = self.__class__

        if not isinstance(other, cls):
            return NotImplemented

        if self == cls.reset or other == cls.reset:
            raise ArithmeticError(f"cannot combine with {cls.__name__}.reset")

        return cls(*self.values, *other.values)

    def build(self):
        value = ";".join(str(v) for v in sorted(self.values))
        return f"\x1B[{value}m"
