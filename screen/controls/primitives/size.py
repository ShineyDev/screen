import re


_size_re = re.compile(r"(auto)|([0-9]+)?(\*)?")


class Size:
    """
    Represents the height or width of a cell.

    Parameters
    ----------
    value: Union[:class:`int`, :class:`str`]
        Can be "auto", an integer, or a star-size; for example, "*" or
        "4*". A value of "*" is equal to "1*".


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares the :attr:`~.value` of two :class:`~.Size`
            objects.

        .. describe:: hash(x)

            Returns the hash of the size :attr:`~.value`.
    """

    __slots__ = ("_match", "_value")

    def __init__(self, value):
        try:
            self._match = _size_re.match(str(value))
        except (re.error) as e:
            raise ValueError(f"invalid value of '{value}'") from e

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        if self.is_auto:
            value = "auto"
        elif self.is_star:
            value = f"{self.value}*"
        else:
            value = self.value

        return f"<{self.__class__.__name__} value={value!r}>"

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.is_auto == other.is_auto
            and self.is_star == other.is_star
            and self.value == other.value
        )

    @property
    def is_auto(self):
        """
        Whether the size is automatically-sized. An automatically-sized
        cell inherits its size from its child control.

        :type: :class:`bool`
        """

        return bool(self._match.group(1))

    @property
    def is_star(self):
        """
        Whether the size is star-sized. A star-sized cell is calculated
        as a weighted proportion of available space. The weight is
        :attr:`~.value`.

        :type: :class:`bool`
        """

        return bool(self._match.group(3))

    @property
    def value(self):
        """
        The value of the size.

        :type: :class:`int`
        """

        return int(self._match.group(2) or 1)
