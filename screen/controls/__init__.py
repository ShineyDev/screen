from typing import Optional

import abc
import collections
import re
import textwrap

from screen.controls.primitives import HorizontalAlignment
from screen.controls.primitives import Thickness
from screen.controls.primitives import VerticalAlignment
from screen.drawing import Color
from screen.utils.internal import get_type_doc


_builtins_property = property


property = collections.namedtuple("property", "type default optional remeasure")
property.__doc__ = """
Registers a property on a :class:`~.Control`.

Parameters
----------
type: Type[Any]
    The value type.
default: Any
    The default value for the property. This can be accessed,
    overwritten, and overridden by inheriting classes as ``default_*``.
optional: :class:`bool`
    A boolean indicating whether the property should be an optional
    parameter to :meth:`Control.__init__ <Control>`.
remeasure: Union[:class:`bool`, Callable[[Any, Any], :class:`bool`]]
    A boolean (or a callable taking the current and modified values and
    returning a boolean) indicating whether modifying the property
    should invalidate cached measures.

Examples
--------

.. code-block:: python3

    class Text(Control):
        content = property(str, None, False, True)

.. code-block:: python3

    class Border(Control):
        header = property(Optional[str], None, True, lambda c, v: len(c) != len(v))
"""

_property = collections.namedtuple("_property", "name type default optional remeasure")

_property_getter = """

def {name}(self):
    return self._{name}

""".strip()

_property_setter_simple = """

def {name}(self, value):
    if value is not None and not isinstance(value, type):
        raise ValueError

    self._{name} = value if value is not None else self.__class__.default_{name}

""".strip()

_property_setter_remeasure_simple = """

def {name}(self, value):
    if value is not None and not isinstance(value, type):
        raise ValueError

    value = value if value is not None else self.__class__.default_{name}
    if value != self._{name}:
        self._{name} = value
        self._measure_cache = dict()

""".strip()

_property_setter_remeasure_callable = """

def {name}(self, value):
    if value is not None and not isinstance(value, type):
        raise ValueError

    value = value if value is not None else self.__class__.default_{name}
    if value != self._{name}:
        self._{name} = value

        if remeasure():
            self._measure_cache = dict()

"""


class ControlMeta(abc.ABCMeta):
    def __new__(cls_meta, cls_name, cls_bases, cls_attrs, **kwargs):
        properties = list()
        for (attr_name, attr_value) in cls_attrs.items():
            if isinstance(attr_value, property):
                properties.append(_property(attr_name, *attr_value))

        for cls_base in cls_bases:
            try:
                properties.extend(cls_base.__control_properties__)
            except (AttributeError) as e:
                pass

        properties.sort(key=lambda p: (p.optional, p.name))

        cls_attrs["__control_properties__"] = properties

        def _compile(source, p):
            source = source.format(name=p.name)
            code = compile(source, "<string>", "exec")
            exec(code, p._asdict(), locals())
            return locals()[p.name]

        slots = list(cls_attrs.get("__slots__", []))

        parameters_doc = "Parameters\n----------\n"

        properties = cls_attrs["__control_properties__"]
        for p in properties:
            slots.append(f"_{p.name}")

            cls_attrs[f"default_{p.name}"] = p.default

            getter = _compile(_property_getter, p)

            if callable(p.remeasure):
                _property_setter = _property_setter_remeasure_callable
            elif p.remeasure:
                _property_setter = _property_setter_remeasure_simple
            else:
                _property_setter = _property_setter_simple

            setter = _compile(_property_setter, p)

            if p.name.startswith("is_"):
                descriptor_doc = f"Whether the {cls_name.lower()} {p.name.replace('_', ' ')}."
            else:
                descriptor_doc = f"The {cls_name.lower()}'s {p.name.replace('_', ' ')}."

            type_doc = get_type_doc(p.type)

            descriptor = _builtins_property(getter, setter)
            descriptor.__doc__ = f"{descriptor_doc}\n\n:type: {type_doc}"

            cls_attrs[p.name] = descriptor

            type_doc = get_type_doc(p.type, optional=False)

            if not p.optional:
                descriptor_doc += " This parameter is not optional."

            parameters_doc += f"{p.name}: {type_doc}\n    {descriptor_doc}\n"

        cls_doc = cls_attrs["__doc__"]
        if cls_doc:
            match = re.search(r"\n( *)\|parameters\|\n", cls_doc)
            if match:
                cls_doc = cls_doc.replace(
                    " " * len(match.group(1)) + "|parameters|",
                    textwrap.indent(parameters_doc, " " * len(match.group(1))),
                )
            else:
                cls_doc += "\n\n\n" + textwrap.indent(parameters_doc, "    ")
        else:
            cls_doc = parameters_doc

        cls_attrs["__doc__"] = cls_doc
        cls_attrs["__slots__"] = tuple(set(slots))

        return super().__new__(cls_meta, cls_name, cls_bases, cls_attrs, **kwargs)


class Control(metaclass=ControlMeta):
    """
    Represents the base class for a control.
    """

    # fmt: off
    background           = property(Optional[Color],     None,                     True, False)
    foreground           = property(Optional[Color],     None,                     True, False)
    height               = property(Optional[int],       None,                     True, True)
    horizontal_alignment = property(HorizontalAlignment, HorizontalAlignment.left, True, True)
    is_resizable         = property(bool,                False,                    True, False)
    layer                = property(int,                 0,                        True, True)
    margin               = property(Thickness,           Thickness(0),             True, True)
    max_height           = property(Optional[int],       None,                     True, True)
    max_width            = property(Optional[int],       None,                     True, True)
    min_height           = property(Optional[int],       None,                     True, True)
    min_width            = property(Optional[int],       None,                     True, True)
    padding              = property(Thickness,           Thickness(0),             True, True)
    vertical_alignment   = property(VerticalAlignment,   VerticalAlignment.top,    True, True)
    width                = property(Optional[int],       None,                     True, True)
    # fmt: on

    __slots__ = ("_measure_cache",)

    def __init__(self, **kwargs):
        for p in self.__class__.__control_properties__:
            try:
                value = kwargs.pop(p.name)
            except (KeyError) as e:
                if p.optional:
                    value = getattr(self.__class__, f"default_{p.name}")
                else:
                    raise TypeError(f"__init__ missing a required argument: '{p.name}'") from e

            setattr(self, f"_{p.name}", value)

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
            self._measure_cache[h, w] = value = self.measure_core(h, w, **kwargs)
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


from screen.controls.popup import Popup


__all__ = [
    "property",
    "Control",
    "Popup",
]
