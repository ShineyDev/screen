import abc
import collections
import sys
import typing

from screen.controls.primitives import HorizontalAlignment
from screen.controls.primitives import Thickness
from screen.controls.primitives import VerticalAlignment
from screen.drawing import Color


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
    """
    Adds an option to a :class:`~.Control`.

    Parameters
    ----------
    name: :class:`str`
        The name of the option. The string should pass the
        :meth:`~str.isidentifier` check.
    type: Type[Any]
        The type of the option value.
    default: Optional[Any]
        The default value for the option.
    optional: :class:`bool`
        Whether the option should be an optional argument to
        :meth:`Control.__init__ <Control>`.
    remeasure: :class:`bool`
        Whether modifying the option should invalidate cached measures.

    Example
    -------

    .. code-block:: python3

        @option("content", str, None, False, True)
        class Text(Control):
            ...
    """

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

        def get_type_doc(t):
            try:
                if isinstance(t, typing._GenericAlias):
                    origin = t.__origin__
                    if isinstance(origin, typing._SpecialForm):
                        name = origin._name
                    else:
                        # PEP 585
                        name = origin.__name__.capitalize()

                    args = ", ".join(get_type_doc(a) for a in t.__args__)
                    return f"{name}[{args}]"
                elif t.__module__ == cls.__module__:
                    return f":class:`~.{t.__name__}`"
                elif t.__module__ == "builtins":
                    return f":class:`~{t.__name__}`"
                elif t.__module__ == "screen.controls":
                    return f":class:`~{module}.{t.__name__}`"
                else:
                    module = t.__module__.rsplit(".", 1)[0]
                    return f":class:`~{module}.{t.__name__}`"
            except (BaseException) as e:
                return ""

        type_doc = get_type_doc(type)
        doc = f"The {cls.__name__.lower()}'s {name.replace('_', ' ')}."

        descriptor = property(getter, setter)
        descriptor.__doc__ = f"\n    {doc}\n\n    :type: {type_doc}\n    "

        setattr(cls, name, descriptor)

        if cls.__doc__:
            cls.__doc__ += f"{name}: {type_doc}\n        {doc}\n    "

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
class Control(metaclass=abc.ABCMeta):
    """
    Represents the base class for TUI controls.

    Parameters
    ----------
    """

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
        """
        Calculates the desired size of the control. This method is a
        cached implementation of :meth:`~.measure_core`.

        Parameters to this method are identical to
        :meth:`~.measure_core`.

        Returns
        -------
        Tuple[:class:`int`, :class:`int`]
            The desired size of the control.
        """

        try:
            return self._measure_cache[h, w]
        except (KeyError) as e:
            value = self.measure_core(h, w, **kwargs)
            self._measure_cache[h, w] = value
            return value

    @abc.abstractmethod
    def measure_core(self, h, w, **kwargs):
        """
        Calculates the desired size of the control.

        Parameters
        ----------
        h: Optional[:class:`int`]
            The available height. Can be ``None`` when the parent wants
            to measure the child. This is a soft constraint and this
            method may return a smaller or larger integer and hope the
            parent can accommodate.
        w: Optional[:class:`int`]
            The available width. Can be ``None`` when the parent wants
            to measure the child. This is a soft constraint and this
            method may return a smaller or larger integer and hope the
            parent can accommodate.

        Returns
        -------
        Tuple[:class:`int`, :class:`int`]
            The desired size of the control.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def render(self, h, w, **kwargs):
        """
        Renders the control.

        Parameters
        ----------
        h: :class:`int`
            The available height. This is a hard constraint and the
            iterator returned by this method is expected to yield a
            correctly sized block.
        w: :class:`int`
            The available width. This is a hard constraint and the
            iterator returned by this method is expected to yield a
            correctly sized block.

        Returns
        -------
        Iterator[:class:`str`]
            An iterator yielding lines.
        """

        raise NotImplementedError


__all__ = [
    "Control",
]
