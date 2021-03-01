import types


class AttributeFactoryMeta(type):
    def __new__(cls, cls_name, bases, attrs):
        attr_init = attrs.pop("__attr_init__", lambda c, v: c(v))
        attr_repr = attrs.pop("__attr_repr__", repr)

        cls = super().__new__(cls, cls_name, bases, attrs)

        for (attr_name, attr_value) in attrs.items():
            if attr_name.startswith("_") or isinstance(attr_value, types.FunctionType):
                continue

            setattr(cls, attr_name, attr_init(cls, attr_value))

            cls.__doc__ += (
                f"\n    {attr_name}: :class:`.{cls_name}`"
                f"\n        A {cls_name.lower()} with a :attr:`value <.{cls.__slots__[0]}>` of ``{attr_repr(attr_value)}``."
            )

        return cls
