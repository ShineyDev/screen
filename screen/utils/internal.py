from types import FunctionType
from typing import (
    Any,
    Dict,
    FrozenSet,
    List,
    Literal,
    Set,
    Tuple,
    Union,
    _GenericAlias as typing_GenericAlias,
    _SpecialForm as SpecialForm,
)

try:
    from types import GenericAlias as types_GenericAlias
except (ImportError) as e:
    types_GenericAlias = typing_GenericAlias


builtins_isinstance = isinstance


def get_type_doc(t, *, optional=True):
    if isinstance(t, (types_GenericAlias, typing_GenericAlias)):
        origin = t.__origin__

        if origin is Union and type(None) in t.__args__:
            t = Union[tuple(a for a in t.__args__ if a is not type(None))]

            doc = get_type_doc(t, optional=optional)

            if optional:
                return f"Optional[{doc}]"
            else:
                return doc

        if isinstance(origin, SpecialForm):
            name = origin._name
        else:
            name = origin.__name__.capitalize()

        args = ", ".join(get_type_doc(t, optional=optional) for t in t.__args__)
        return f"{name}[{args}]"
    elif t.__module__ == "builtins":
        return f":class:`{t.__name__}`"
    elif t.__module__ == "screen.controls":
        return f":class:`~{t.__module__}.{t.__name__}`"
    elif t.__module__.startswith("screen."):
        return f":class:`~{t.__module__.rsplit('.', 1)[0]}.{t.__name__}`"
    else:
        return t.__name__


def isinstance(obj, t):
    if builtins_isinstance(t, tuple):
        return any(isinstance(obj, t) for t in t)

    if builtins_isinstance(t, (types_GenericAlias, typing_GenericAlias)):
        if t.__origin__ in (Dict, dict):
            k_T, v_T = t.__args__

            return (
                isinstance(obj, dict)
                and all(isinstance(k, k_T) and isinstance(v, v_T) for (k, v) in obj.items())
            )
        elif t.__origin__ in (FrozenSet, frozenset):
            return isinstance(obj, frozenset) and all(isinstance(e, t.__args__[0]) for e in obj)
        elif t.__origin__ in (List, list):
            return isinstance(obj, list) and all(isinstance(e, t.__args__[0]) for e in obj)
        elif t.__origin__ is Literal:
            return obj in t.__args__
        elif t.__origin__ in (Set, set):
            return isinstance(obj, set) and all(isinstance(e, t.__args__[0]) for e in obj)
        elif t is tuple or t.__origin__ in (Tuple, tuple):
            try:
                args = t.__args__
                variable = False

                if args[-1] is Ellipsis:
                    args = args[:-1]
                    variable = True
            except (AttributeError) as e:
                args = (Any, )
                variable = True

            if not isinstance(obj, tuple):
                return False

            if variable:
                return all(isinstance(e, args) for e in obj)
            else:
                return len(obj) == len(args) and all(isinstance(obj[i], args[i]) for i in range(len(args)))
        elif t.__origin__ is Union:
            return isinstance(obj, t.__args__)

    if builtins_isinstance(t, SpecialForm) and t._name == "Any":
        return True

    return builtins_isinstance(obj, t)


factory_ignore_types = (classmethod, property, staticmethod, FunctionType)


class AttributeFactoryMeta(type):
    def __new__(cls, cls_name, bases, attrs):
        attr_init = attrs.pop("__attr_init__", lambda c, v: c(v))
        attr_repr = attrs.pop("__attr_repr__", repr)

        cls = super().__new__(cls, cls_name, bases, attrs)

        for (attr_name, attr_value) in attrs.items():
            if attr_name.startswith("_") or isinstance(attr_value, factory_ignore_types):
                continue

            setattr(cls, attr_name, attr_init(cls, attr_value))

            cls.__doc__ += (
                f"{attr_name}: :class:`.{cls_name}`\n    "
                f"    A {cls_name.lower()} with a :attr:`value <.{cls.__slots__[0]}>` of "
                f"``{attr_repr(attr_value)}``.\n    "
            )

        return cls


__all__ = [
    "get_type_doc",
    "AttributeFactoryMeta",
]
