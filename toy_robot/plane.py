from toy_robot.coordinate import Coordinate


class Plane:
    """Represents a *2D plane*, e.g. a table."""

    def __init__(self, width: int, height: int) -> None:
        """Instantiates a plane provided `width` and `height` and determine the
        `southwest` and `northeast` corners to serve as boundary of the
        plane."""
        self.width = width
        self.height = height

        self.southwest_corner = Coordinate(x=0, y=0)
        self.northeast_corner = Coordinate(x=self.width, y=self.height)

    def is_inside_plane(self, coordinate: Coordinate) -> bool:
        """Checks if provided coordinate still resides on the plane."""
        return (
            True
            if self.southwest_corner <= coordinate < self.northeast_corner
            else False
        )

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int | str) -> None:
        """Ensures correct data type of width."""
        if value <= 0:
            raise ValueError("Invalid width for a plane")
        self._width = int(value)

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int | str) -> None:
        """Ensures correct data type of height."""
        if value <= 0:
            raise ValueError("Invalid height for a plane")
        self._height = int(value)
