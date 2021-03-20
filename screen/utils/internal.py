from typing import Union, _GenericAlias, _SpecialForm

import types


def get_type_doc(t, *, optional=True):
    if isinstance(t, _GenericAlias):
        origin = t.__origin__

        if origin is Union and type(None) in t.__args__:
            t = Union[tuple(a for a in t.__args__ if a is not type(None))]

            doc = get_type_doc(t, optional=optional)

            if optional:
                return f"Optional[{doc}]"
            else:
                return doc

        if isinstance(origin, _SpecialForm):
            name = origin._name
        else:
            name = origin.__name__.capitalize()

        args = ", ".join(get_type_doc(t, optional=optional) for t in t.__args__)
        return f"{name}[{args}]"
    elif t.__module__ == "builtins":
        return f":class:`{t.__name__}`"
    elif t.__module__.startswith("screen."):
        return f":class:`~{t.__module__.rsplit('.', 1)[0]}.{t.__name__}`"
    else:
        return t.__name__


factory_ignore_types = (classmethod, property, staticmethod, types.FunctionType)


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
