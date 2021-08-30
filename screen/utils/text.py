import re
import string
import unicodedata


def decimal_to_latin(d):
    """
    Translates a decimal to a latin string.

    Parameters
    ----------
    d: :class:`int`
        A decimal in the range ``[1..]``.

    Returns
    -------
    :class:`str`
        A latin string.

    Examples
    --------

    .. code:: python3

        >>> decimal_to_latin(15)
        "o"

        >>> decimal_to_latin(29)
        "ac"
    """

    r = list()

    while d:
        d -= 1
        d, m = divmod(d, 26)
        r.append(string.ascii_lowercase[m])

    return "".join(reversed(r))


_decimal_roman_map = {
    1000: "m",
    900: "cm",
    500: "d",
    400: "cd",
    100: "c",
    90: "xc",
    50: "l",
    40: "xl",
    10: "x",
    9: "ix",
    5: "v",
    4: "iv",
    1: "i",
}


def decimal_to_roman(d):
    """
    Translates a decimal to a Roman numeral string.

    Parameters
    ----------
    d: :class:`int`
        A decimal in the range ``[1..]``.

    Returns
    -------
    :class:`str`
        A Roman numeral string.

    Examples
    --------

    .. code:: python3

        >>> decimal_to_roman(15)
        "xv"

        >>> decimal_to_roman(29)
        "xxix"
    """

    r = list()

    for (i, n) in _decimal_roman_map.items():
        i, d = divmod(d, i)
        r.append(n * i)

    return "".join(r)


def height(s):
    """
    Calculates the height of a string.

    .. note::

        The string passed to this function is expected to have been
        :attr:`normalized <normalize>`.

    Parameters
    ----------
    s: :class:`str`
        The string to calculate the height of.

    Returns
    -------
    :class:`int`
        The calculated height of the string.
    """

    return s.count("\n") + 1


def len(s):
    """
    Calculates the length of a string. This function takes into account
    CJK and zero-width characters.

    .. note::

        The string passed to this function is expected to have been
        :attr:`normalized <normalize>`.

    Parameters
    ----------
    s: :class:`str`
        The string to calculate the length of.

    Returns
    -------
    :class:`int`
        The calculated length of the string.

    Examples
    --------

    .. code:: python3

        >>> len("oranges")
        7

        >>> len("\\x00")
        0

        >>> len("\u65E5\u672C\u8A9E")
        6

        >>> len("\\u0061\\u0301")  # \u0061\u0301
        2

        >>> len(normalize("\\u0061\\u0301"))  # \u00E1
        1
    """

    # NOTE: unicode characters 0001-0006, 0010-001A, 001C-001F appear
    #       to be replaced in WT by 263A-263B, 2665-2666, 2663, 2660,
    #       25BA, 25C4, 2195, 203C, 00B6, 00A7, 25AC, 21A8, 2191, 2193,
    #       2192, 221F, 2194, 25B2, and 25BC respectively.

    l = 0

    for c in s:
        # NOTE: unicode characters 0000-001F, and 007F-009F get special
        #       cased to zero-width
        if ord(c) <= 31 or 127 <= ord(c) <= 159:
            continue

        w = unicodedata.east_asian_width(c)

        if w in "FW":
            l += 2
        else:
            l += 1

    return l


def normalize(s):
    """
    Normalizes a string.

    This function does the following, in order:

    - Calls :func:`unicodedata.normalize("NFC", ...) \
      <unicodedata.normalize>`.
    - Normalizes line endings.
    - Expands horizontal tabs with a width of four columns.
    - Expands vertical tabs with a height of one row, and emulates
      carriage return.
    - Emulates backspace and delete.

    Parameters
    ----------
    s: :class:`str`
        The string to normalize.

    Returns
    -------
    :class:`str`
        The normalized string.

    Examples
    --------

    .. code:: python3

        >>> normalize("\\u0061\\u0301")  # \u0061\u0301
        "\\u00E1"

        >>> normalize("cool text\\vtext")
        "cool text\\r\\n         text"

        >>> normalize("text text\\rcool")
        "cool text"
    """

    s = unicodedata.normalize("NFC", s)

    s = s.replace("\r\n", "\n")
    s = s.replace("\f", "\n")

    s = s.expandtabs(4)

    if "\r" in s or "\v" in s:
        s = re.sub(r"\r|\v", "\f\\g<0>", s)

        lines = s.split("\n")
        for (i, line) in enumerate(lines):
            if "\f" in line:
                parts = line.split("\f")

                line = ""
                column = 0

                for part in parts:
                    if not part:
                        continue

                    code, part = part[0], part[1:]

                    if code == "\r":
                        try:
                            line, current_line = line.rsplit("\n", 1)
                            line += "\n"
                        except (ValueError) as e:
                            line, current_line = "", line

                        remaining = ""
                        for c in reversed(current_line):
                            if len(current_line) - (len(remaining) + len(part)) < len(c):
                                break

                            remaining = c + remaining

                        line += part + remaining
                        column = len(part)
                    elif code == "\v":
                        line += "\n" + " " * column + part
                        column += len(part)
                    else:
                        line += code + part
                        column = len(code + part)

                lines[i] = line

        s = "\n".join(lines)

    while "\b" in s or "\u007F" in s:
        s = re.sub(r".?((?:\u0008|\u007F)*)\u0008|\u007F((?:\u0008|\u007F)*).?", r"\1\2", s)

    s = s.replace("\n", "\r\n")

    return s


def width(s):
    """
    Calculates the width of a string.

    .. note::

        The string passed to this function is expected to have been
        :attr:`normalized <normalize>`.

    Parameters
    ----------
    s: :class:`str`
        The string to calculate the width of.

    Returns
    -------
    :class:`int`
        The calculated width of the string.
    """

    return max(len(s) for s in s.split("\n"))


__all__ = [
    "decimal_to_latin",
    "decimal_to_roman",
    "height",
    "len",
    "normalize",
    "width",
]
