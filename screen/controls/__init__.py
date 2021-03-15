import collections
import sys

from screen.drawing import Color
from screen.primitives import HorizontalAlignment
from screen.primitives import Thickness
from screen.primitives import VerticalAlignment


_option = collections.namedtuple("_option", "name type default optional remeasure")

_option_getter = """

def {name}(self):
    return self._{name}

""".strip()

_option_setter_simple = """

def {name}(self, value):
    self._{name} = value if value is not None else self.__class__.default_{name}

""".strip()

_option_setter_remeasure = """

def {name}(self, value):
    value = value if value is not None else self.__class__.default_{name}
    if value != self._{name}:
        self._{name} = value
        self._measure_cache = dict()

""".strip()


def option(name, type, default, optional, remeasure):
    def deco(cls):
        option = _option(name, type, default, optional, remeasure)

        try:
            cls.__control_options__ = [*cls.__control_options__, option]
        except (AttributeError) as e:
            cls.__control_options__ = [option]

        setattr(cls, f"default_{name}", default)

        def compile_function(source):
            source = source.format(name=name)
            code = compile(source, "<string>", "exec")
            exec(code)
            return locals()[name]

        getter = compile_function(_option_getter)

        if remeasure:
            setter = compile_function(_option_setter_remeasure)
        else:
            setter = compile_function(_option_setter_simple)

        setattr(cls, name, property(getter, setter))

        return cls

    return deco


# fmt: off
@option("background",           Color,               None,                     True, False)
@option("foreground",           Color,               None,                     True, False)
@option("height",               int,                 None,                     True, True)
@option("horizontal_alignment", HorizontalAlignment, HorizontalAlignment.left, True, True)
@option("margin",               Thickness,           Thickness(0),             True, True)
@option("max_height",           int,                 sys.maxsize,              True, True)
@option("max_width",            int,                 sys.maxsize,              True, True)
@option("min_height",           int,                 0,                        True, True)
@option("min_width",            int,                 0,                        True, True)
@option("padding",              Thickness,           Thickness(0),             True, True)
@option("vertical_alignment",   VerticalAlignment,   VerticalAlignment.top,    True, True)
@option("width",                int,                 None,                     True, True)
# fmt: on
class Control:
    def __init__(self, **kwargs):
        options = getattr(self.__class__, "__control_options__", [])
        for (name, _, default, optional, _) in options:
            try:
                value = kwargs.pop(name)
            except (KeyError) as e:
                if optional:
                    value = default
                else:
                    raise TypeError(f"__init__ missing a required argument: '{name}'") from e

            setattr(self, f"_{name}", value)

        self._measure_cache = dict()

    def measure(self, h, w, **kwargs):
        try:
            return self._measure_cache[h, w]
        except (KeyError) as e:
            value = self.measure_core(h, w, **kwargs)
            self._measure_cache[h, w] = value
            return value

    def measure_core(self, h, w, **kwargs):
        raise NotImplementedError

    def render(self, h, w, **kwargs):
        raise NotImplementedError


__all__ = [
    "Control",
]
