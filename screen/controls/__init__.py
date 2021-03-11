import collections
import sys

from screen.drawing import Color
from screen.primitives import HorizontalAlignment
from screen.primitives import Thickness
from screen.primitives import VerticalAlignment


_option = collections.namedtuple("_option", "name type default optional remeasure")

_option_getter = """

def {attr_name}(self):
    return self._{attr_name}

""".strip()

_option_setter_simple = """

def {attr_name}(self, value):
    self._{attr_name} = value if value is not None else self.__class__.default_{attr_name}

""".strip()

_option_setter_remeasurable = """

def {attr_name}(self, value):
    value = value if value is not None else self.__class__.default_{attr_name}
    if value != self._{attr_name}:
        self._{attr_name} = value
        self._size = None

""".strip()


def option(attr_name, attr_type, attr_default, attr_optional, attr_remeasure):
    def wrapper(cls):
        # set cls.__control_options__

        option = _option(attr_name, attr_type, attr_default, attr_optional, attr_remeasure)
        try:
            cls.__control_options__.append(option)
        except (AttributeError) as e:
            cls.__control_options__ = [option]

        # set cls.default_* for the below data descriptors

        setattr(cls, f"default_{attr_name}", attr_default)

        # set cls.* data descriptors

        def compile_function(source):
            source = source.format(attr_name=attr_name)
            code = compile(source, "<string>", "exec")
            exec(code)
            return locals()[attr_name]

        getter = compile_function(_option_getter)

        if attr_remeasure:
            setter = compile_function(_option_setter_remeasurable)
        else:
            setter = compile_function(_option_setter_simple)

        setattr(cls, attr_name, property(getter, setter))

        return cls

    return wrapper


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
        cls_options = getattr(self.__class__, "__control_options__", [])
        for (attr_name, _, attr_default, attr_optional, _) in cls_options:
            try:
                attr_value = kwargs.pop(attr_name)
            except (KeyError) as e:
                if attr_optional:
                    attr_value = attr_default
                else:
                    raise TypeError(f"__init__ missing a required argument: '{attr_name}'")

            setattr(self, f"_{attr_name}", attr_value)

        self._size = None

    def measure(self, h, w, **kwargs):
        if not self._size:
            self._size = self.measure_core(h, w, **kwargs)

        return self._size

    def measure_core(self, h, w, **kwargs):
        raise NotImplementedError

    def render(self, h, w, **kwargs):
        raise NotImplementedError


__all__ = [
    "Control",
]
