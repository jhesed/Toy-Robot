class Coordinate:
    """Represents a coordinate in a 2D plane (with `x` and `y` axis).

    This class overrides dunder methods like `__ge__`, `__le__`, etc. to
    allow easier comparison of Coordinate objects.
    """

    def __init__(self, x: int | str | float, y: int | str | float) -> None:
        """Instantiates a coordinate object.

        :param x: x coordinate in a plane, e.g. abscissa.
        :param y: y coordinate in a plane, e.g. ordinate
        """
        self.x = x
        self.y = y

    def __ge__(self, other) -> bool:
        """Overrides `>=` operator to make comparison between Coordinate
        objects simpler.

        Example Usage: Coordinate(x, y) >= Coordinate(v, x)
        """
        return True if self.x >= other.x and self.y >= other.y else False

    def __le__(self, other) -> bool:
        """Example Usage: Coordinate(x, y) <= Coordinate(v, x)"""
        return True if self.x <= other.x and self.y <= other.y else False

    def __gt__(self, other) -> bool:
        """Example Usage: Coordinate(x, y) > Coordinate(v, x)"""
        return True if self.x > other.x and self.y > other.y else False

    def __lt__(self, other) -> bool:
        """Example Usage: Coordinate(x, y) < Coordinate(v, x)"""
        return True if self.x < other.x and self.y < other.y else False

    def __eq__(self, other) -> bool:
        return True if self.x == other.x and self.y == other.y else False

    def __add__(self, other):
        return Coordinate(x=self.x + other.x, y=self.y + other.y)

    def __repr__(self):
        """Converts class to a readable string, instead of printing an object.

        Useful for debugging failing unit tests.
        """
        return f"{self.x},{self.y}"

    @property
    def x(self) -> int:
        """A valid abscissa of type int."""
        return self._x

    @x.setter
    def x(self, value: int | str) -> None:
        """Ensures correct data type of x coordinate."""
        self._x = int(value)

    @property
    def y(self) -> int:
        """A valid ordinate of type int."""
        return self._y

    @y.setter
    def y(self, value: int | str) -> None:
        """Ensures correct data type of y coordinate."""
        self._y = int(value)
