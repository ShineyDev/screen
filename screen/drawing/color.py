import colorsys
import enum

from screen import utils


class ColorInterpolationMethod(enum.IntEnum):
    hsl = 1
    hsv = 2
    rgb = 3

class Color():
    __slots__ = ("value",)

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Color) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"<Color r={self.r} g={self.g} b={self.b}>"

    @classmethod
    def from_argb(cls, a, r, g, b):
        a = int(a * 255)
        return cls((a << 24) + (r << 16) + (g << 8) + b)

    @classmethod
    def from_hsl(cls, h, s, l):
        return cls.from_rgb(*cls._hsl_to_rgb(h, s, l))

    @classmethod
    def from_hsv(cls, h, s, v):
        return cls.from_rgb(*cls._hsv_to_rgb(h, s, v))

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls.from_argb(1, r, g, b)

    @property
    def a(self):
        a = self.value >> 24 & 0xFF
        return a / 255

    @property
    def r(self):
        return self.value >> 16 & 0xFF

    @property
    def g(self):
        return self.value >> 8 & 0xFF

    @property
    def b(self):
        return self.value & 0xFF

    @staticmethod
    def interpolate(c1, c2, p, *, method=None):
        method = method or ColorInterpolationMethod.rgb
        meth = Color._interpolation_method_map[method]
        return meth(c1, c2, p)

    def _interpolate_hsl(c1, c2, p):
        h1, s1, l1 = Color._rgb_to_hsl(c1.r, c1.g, c1.b)
        h2, s2, l2 = Color._rgb_to_hsl(c2.r, c2.g, c2.b)

        return Color.from_hsl(
            int(utils.interpolate(h1, h2, p)),
            utils.interpolate(s1, s2, p),
            utils.interpolate(l1, l2, p),
        )

    def _interpolate_hsv(c1, c2, p):
        h1, s1, v1 = Color._rgb_to_hsv(c1.r, c1.g, c1.b)
        h2, s2, v2 = Color._rgb_to_hsv(c2.r, c2.g, c2.b)

        return Color.from_hsv(
            int(utils.interpolate(h1, h2, p)),
            utils.interpolate(s1, s2, p),
            utils.interpolate(v1, v2, p),
        )

    def _interpolate_rgb(c1, c2, p):
        return Color.from_rgb(
            int(utils.interpolate(c1.r, c2.r, p)),
            int(utils.interpolate(c1.g, c2.g, p)),
            int(utils.interpolate(c1.b, c2.b, p)),
        )

    _interpolation_method_map = {
        ColorInterpolationMethod.hsl: _interpolate_hsl,
        ColorInterpolationMethod.hsv: _interpolate_hsv,
        ColorInterpolationMethod.rgb: _interpolate_rgb,
    }

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
