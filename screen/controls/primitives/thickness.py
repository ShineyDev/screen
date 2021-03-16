class Thickness:
    """
    Represents the thickness of a frame around a rectangle.

    Parameters
    ----------
    left: :class:`int`
        The left thickness.
    top: :class:`int`
        The top thickness. Defaults to :attr:`~.left`.
    right: :class:`int`
        The right thickness. Defaults to :attr:`~.left`.
    bottom: :class:`int`
        The bottom thickness. Defaults to :attr:`~.top`.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares the :attr:`values <.left>` of two
            :class:`~.Thickness` objects.

        .. describe:: x + y

            Combines two :class:`~.Thickness` objects.

        .. describe:: hash(x)

            Returns the hash of the thickness :attr:`values <.left>`.

    Attributes
    ----------
    left: :class:`int`
        The left thickness.
    top: :class:`int`
        The top thickness.
    right: :class:`int`
        The right thickness.
    bottom: :class:`int`
        The bottom thickness.
    """

    __slots__ = ("left", "top", "right", "bottom")

    def __init__(self, left, top=None, right=None, bottom=None):
        self.left = left
        self.top = top if top is not None else self.left
        self.right = right if right is not None else self.left
        self.bottom = bottom if bottom is not None else self.top

    def __hash__(self):
        return hash((self.left, self.top, self.right, self.bottom))

    def __repr__(self):
        return (
            f"<Thickness left={self.left} top={self.top} right={self.right} bottom={self.bottom}>"
        )

    def __add__(self, other):
        cls = self.__class__

        if isinstance(other, cls):
            return cls(
                self.left + other.left,
                self.top + other.top,
                self.right + other.right,
                self.bottom + other.bottom,
            )

        return NotImplemented

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.left == other.left
            and self.top == other.top
            and self.right == other.right
            and self.bottom == other.bottom
        )
