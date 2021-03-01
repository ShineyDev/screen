import colorsys
import enum
import random

from screen import utils
from screen.utils.internal import AttributeFactoryMeta


class Color(metaclass=AttributeFactoryMeta):
    """
    Represents a drawable color.

    Parameters
    ----------
    value: :class:`int`
        The color value.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares the :attr:`~.value` of ``x`` and ``y``.

        .. describe:: hash(x)

            Returns the hash of the color :attr:`~.value`.

    Attributes
    ----------
    value: :class:`int`
        The color value.
    """

    def __attr_repr__(value):
        return f"0x{value:08X}"

    black = 0xFF000000
    blue = 0xFF000080
    bright_black = 0xFF555555
    bright_blue = 0xFF0000FF
    bright_cyan = 0xFF00FFFF
    bright_green = 0xFF00FF00
    bright_magenta = 0xFFFF00FF
    bright_red = 0xFFFF0000
    bright_yellow = 0xFFFFFF00
    bright_white = 0xFFFFFFFF
    cyan = 0xFF008080
    green = 0xFF008000
    magenta = 0xFF800080
    red = 0xFF800000
    transparent = 0x00FFFFFF
    yellow = 0xFF808000
    white = 0xFFAAAAAA

    __slots__ = ("value",)

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"<{self.__class__.__name__} r={self.r} g={self.g} b={self.b}>"

    @classmethod
    def from_ahsl(cls, a, h, s, l):
        """
        Constructs a :class:`~.Color` from an AHSL tuple.

        Parameters
        ----------
        a: :class:`float`
            The alpha value in the range ``[0, 1]``.
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        l: :class:`float`
            The lightness value in the range ``[0, 1]``.
        """

        return cls.from_argb(a, *cls._hsl_to_rgb(h, s, l))

    @classmethod
    def from_ahsv(cls, a, h, s, v):
        """
        Constructs a :class:`~.Color` from an AHSV tuple.

        Parameters
        ----------
        a: :class:`float`
            The alpha value in the range ``[0, 1]``.
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        v: :class:`float`
            The brightness value in the range ``[0, 1]``.
        """

        return cls.from_argb(a, *cls._hsv_to_rgb(h, s, v))

    @classmethod
    def from_argb(cls, a, r, g, b):
        """
        Constructs a :class:`~.Color` from an ARGB tuple.

        Parameters
        ----------
        a: :class:`float`
            The alpha value in the range ``[0, 1]``.
        r: :class:`int`
            The red value in the range ``[0, 255]``.
        g: :class:`float`
            The green value in the range ``[0, 255]``.
        b: :class:`float`
            The blue value in the range ``[0, 255]``.
        """

        a = int(a * 255)
        return cls((a << 24) + (r << 16) + (g << 8) + b)

    @classmethod
    def from_hsl(cls, h, s, l):
        """
        Constructs a :class:`~.Color` from an HSL tuple.

        Calls :meth:`~.from_ahsl` with an alpha level of ``1``.

        Parameters
        ----------
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        l: :class:`float`
            The lightness value in the range ``[0, 1]``.
        """

        return cls.from_ahsl(1, h, s, l)

    @classmethod
    def from_hsv(cls, h, s, v):
        """
        Constructs a :class:`~.Color` from an HSV tuple.

        Calls :meth:`~.from_ahsv` with an alpha level of ``1``.

        Parameters
        ----------
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        v: :class:`float`
            The brightness value in the range ``[0, 1]``.
        """

        return cls.from_ahsv(1, h, s, v)

    @classmethod
    def from_rgb(cls, r, g, b):
        """
        Constructs a :class:`~.Color` from an RGB tuple.

        Calls :meth:`~.from_argb` with an alpha level of ``1``.

        Parameters
        ----------
        r: :class:`int`
            The red value in the range ``[0, 255]``.
        g: :class:`float`
            The green value in the range ``[0, 255]``.
        b: :class:`float`
            The blue value in the range ``[0, 255]``.
        """

        return cls.from_argb(1, r, g, b)

    @classmethod
    def from_random(cls):
        """
        Constructs a random :class:`~.Color`.

        .. tip::

            This method can create unsatisfactory colors. It is
            recommended to use :meth:`~.from_random_hsl` or
            :meth:`~.from_random_hsv` with custom-bound saturation and
            lightness/brightness values instead.
        """

        return cls(int(random.random() * 0xFFFFFFFF))

    @classmethod
    def from_random_ahsl(cls, a=None, h=None, s=None, l=None):
        """
        Constructs a partially random :class:`~.Color` from an AHSL
        tuple.

        Parameters
        ----------
        a: :class:`float`
            The alpha value in the range ``[0, 1]``.
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        l: :class:`float`
            The lightness value in the range ``[0, 1]``.
        """

        return cls.from_ahsl(
            a or random.random(),
            h or int(random.random() * 360),
            s or random.random(),
            l or random.random(),
        )

    @classmethod
    def from_random_ahsv(cls, a=None, h=None, s=None, v=None):
        """
        Constructs a partially random :class:`~.Color` from an AHSV
        tuple.

        Parameters
        ----------
        a: :class:`float`
            The alpha value in the range ``[0, 1]``.
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        v: :class:`float`
            The brightness value in the range ``[0, 1]``.
        """

        return cls.from_ahsv(
            a or random.random(),
            h or int(random.random() * 360),
            s or random.random(),
            v or random.random(),
        )

    @classmethod
    def from_random_argb(cls, a=None, r=None, g=None, b=None):
        """
        Constructs a partially random :class:`~.Color` from an ARGB
        tuple.

        .. tip::

            This method can create unsatisfactory colors. It is
            recommended to use :meth:`~.from_random_hsl` or
            :meth:`~.from_random_hsv` with custom-bound saturation and
            lightness/brightness values instead.

        Parameters
        ----------
        a: :class:`float`
            The alpha value in the range ``[0, 1]``.
        r: :class:`int`
            The red value in the range ``[0, 255]``.
        g: :class:`float`
            The green value in the range ``[0, 255]``.
        b: :class:`float`
            The blue value in the range ``[0, 255]``.
        """

        return cls.from_argb(
            a or random.random(),
            r or int(random.random() * 255),
            g or int(random.random() * 255),
            b or int(random.random() * 255),
        )

    @classmethod
    def from_random_hsl(cls, h=None, s=None, l=None):
        """
        Constructs a partially random :class:`~.Color` from an HSL
        tuple.

        Calls :meth:`~.from_random_ahsl` with an alpha level of ``1``.

        Parameters
        ----------
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        l: :class:`float`
            The lightness value in the range ``[0, 1]``.
        """

        return cls.from_random_ahsl(1, h, s, l)

    @classmethod
    def from_random_hsv(cls, h=None, s=None, v=None):
        """
        Constructs a partially random :class:`~.Color` from an HSV
        tuple.

        Calls :meth:`~.from_random_ahsv` with an alpha level of ``1``.

        Parameters
        ----------
        h: :class:`int`
            The hue value in the range ``[0, 360]``.
        s: :class:`float`
            The saturation value in the range ``[0, 1]``.
        v: :class:`float`
            The brightness value in the range ``[0, 1]``.
        """

        return cls.from_random_ahsv(1, h, s, v)

    @classmethod
    def from_random_rgb(cls, r=None, g=None, b=None):
        """
        Constructs a partially random :class:`~.Color` from an RGB
        tuple.

        Calls :meth:`~.from_random_argb` with an alpha level of ``1``.

        .. tip::

            This method can create unsatisfactory colors. It is
            recommended to use :meth:`~.from_random_hsl` or
            :meth:`~.from_random_hsv` with custom-bound saturation and
            lightness/brightness values instead.

        Parameters
        ----------
        r: :class:`int`
            The red value in the range ``[0, 255]``.
        g: :class:`float`
            The green value in the range ``[0, 255]``.
        b: :class:`float`
            The blue value in the range ``[0, 255]``.
        """

        return cls.from_random_argb(1, r, g, b)

    @property
    def a(self):
        """
        The alpha value in the range ``[0, 1]``.

        :type: :class:`float`
        """

        a = self.value >> 24 & 0xFF
        return a / 255

    @property
    def r(self):
        """
        The red value in the range ``[0, 255]``.

        :type: :class:`int`
        """

        return self.value >> 16 & 0xFF

    @property
    def g(self):
        """
        The green value in the range ``[0, 255]``.

        :type: :class:`int`
        """

        return self.value >> 8 & 0xFF

    @property
    def b(self):
        """
        The blue value in the range ``[0, 255]``.

        :type: :class:`int`
        """

        return self.value & 0xFF

    @classmethod
    def distance(cls, c1, c2):
        """
        Calculates euclidean distance.

        Parameters
        ----------
        c1: :class:`~.Color`
            The start color.
        c2: :class:`~.Color`
            The end color.

        Returns
        -------
        :class:`float`
            The euclidean distance in the range ``[0, 441.673...]``.
        """

        return utils.distance((c1.r, c2.r), (c1.g, c2.g), (c1.b, c2.b))

    @classmethod
    def interpolate(cls, c1, c2, p, *, method=None):
        """
        Calculates linear interpolation.

        Parameters
        ----------
        c1: :class:`~.Color`
            The start color.
        c2: :class:`~.Color`
            The end color.
        p: :class:`float`
            The point along the line in the range ``[0, 1]``.
        method: :class:`~.ColorInterpolationMethod`
            The method to use. Defaults to
            :attr:`.ColorInterpolationMethod.rgb`.

        Returns
        -------
        :class:`~.Color`
            The interpolated color.
        """

        name = (method or ColorInterpolationMethod.rgb).name
        meth = getattr(cls, f"_interpolate_{name}")
        return meth(cls, c1, c2, p)

    def _interpolate_hsl(cls, c1, c2, p):
        h1, s1, l1 = cls._rgb_to_hsl(c1.r, c1.g, c1.b)
        h2, s2, l2 = cls._rgb_to_hsl(c2.r, c2.g, c2.b)

        return cls.from_hsl(
            int(utils.interpolate(h1, h2, p)),
            utils.interpolate(s1, s2, p),
            utils.interpolate(l1, l2, p),
        )

    def _interpolate_hsv(cls, c1, c2, p):
        h1, s1, v1 = cls._rgb_to_hsv(c1.r, c1.g, c1.b)
        h2, s2, v2 = cls._rgb_to_hsv(c2.r, c2.g, c2.b)

        return cls.from_hsv(
            int(utils.interpolate(h1, h2, p)),
            utils.interpolate(s1, s2, p),
            utils.interpolate(v1, v2, p),
        )

    def _interpolate_rgb(cls, c1, c2, p):
        return cls.from_rgb(
            int(utils.interpolate(c1.r, c2.r, p)),
            int(utils.interpolate(c1.g, c2.g, p)),
            int(utils.interpolate(c1.b, c2.b, p)),
        )

    def _hsl_to_rgb(h, s, l):
        h /= 360

        r, g, b = colorsys.hls_to_rgb(h, l, s)

        r = int(round(r * 255, 0))
        g = int(round(g * 255, 0))
        b = int(round(b * 255, 0))

        return (r, g, b)

    def _rgb_to_hsl(r, g, b):
        r /= 255
        g /= 255
        b /= 255

        h, l, s = colorsys.rgb_to_hls(r, g, b)

        h = int(h * 360)

        return (h, s, l)

    def _hsv_to_rgb(h, s, v):
        h /= 360

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(round(r * 255, 0))
        g = int(round(g * 255, 0))
        b = int(round(b * 255, 0))

        return (r, g, b)

    def _rgb_to_hsv(r, g, b):
        r /= 255
        g /= 255
        b /= 255

        h, s, v = colorsys.rgb_to_hsv(r, g, b)

        h = int(h * 360)

        return (h, s, v)


class ColorInterpolationMethod(enum.IntEnum):
    """
    Represents the method used to interpolate a color.

    Attributes
    ----------
    hsl
        Interpolate via HSL values.
    hsv
        Interpolate via HSV values.
    rgb
        Interpolate via RGB values.
    """

    hsl = 1
    hsv = 2
    rgb = 3
