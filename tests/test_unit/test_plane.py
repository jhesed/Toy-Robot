import pytest

from toy_robot.coordinate import Coordinate
from toy_robot.plane import Plane


@pytest.mark.parametrize(
    argnames=(
        "height",
        "width",
        "expected_southwest_corner",
        "expected_northeast_corner",
    ),
    argvalues=(
        # Case: square
        (
            5,
            5,
            Coordinate(x=0, y=0),
            Coordinate(x=5, y=5),
        ),
        # Case: rectangle
        (
            5,
            2,
            Coordinate(x=0, y=0),
            Coordinate(x=2, y=5),
        ),
    ),
)
def test_plane_corner_computations(
    height: int,
    width: int,
    expected_southwest_corner: Coordinate,
    expected_northeast_corner: Coordinate,
):
    """Northeast and southeast corners should be computed correctly regardless
    of the dimension values."""
    plane = Plane(width=width, height=height)
    assert plane.northeast_corner == expected_northeast_corner
    assert plane.southwest_corner == expected_southwest_corner


def test_empty_plane():
    """Users should be prevented to create an empty plane."""
    try:
        Plane(width=0, height=0)
    except ValueError:
        # Expected to raise an exception due to invalid value
        pass
    else:
        pytest.fail("Should not be able to create an empty plane.")


@pytest.mark.parametrize(
    argnames=("plane", "coordinate_map"),
    argvalues=(
        # Case: Square
        (
            Plane(width=5, height=5),
            {
                "inside": (
                    Coordinate(x=4, y=4),
                    Coordinate(x=1, y=4),
                    Coordinate(x=0, y=0),
                ),
                "outside": (
                    Coordinate(x=5, y=6),
                    Coordinate(x=6, y=1),
                    Coordinate(x=-1, y=-1),
                    Coordinate(x=5, y=1),
                    Coordinate(x=5, y=5),
                ),
            },
        ),
        # Case: Rectangle
        (
            Plane(width=10, height=2),
            {
                "inside": (
                    Coordinate(x=2, y=1),
                    Coordinate(x=9, y=1),
                    Coordinate(x=9, y=0),
                ),
                "outside": (
                    Coordinate(x=10, y=10),
                    Coordinate(x=9, y=2),
                    Coordinate(x=11, y=3),
                ),
            },
        ),
    ),
)
def test_is_inside_plane(plane: Plane, coordinate_map: dict):
    """Checks if a coordinate resides in the current plane provided."""

    # Verifies that these coordinates are INSIDE the plane
    for coord in coordinate_map["inside"]:
        assert plane.is_inside_plane(coordinate=coord) is True

    # Verifies that these coordinates are OUTSIDE the plane
    for coord in coordinate_map["outside"]:
        assert plane.is_inside_plane(coordinate=coord) is False


@pytest.mark.parametrize(
    ("height", "width"),
    (
        # Case: invalid height
        (-1, 5),
        # Case: invalid width
        (5, -1),
    ),
)
def test_invalid_properties(height: int, width: int):
    try:
        Plane(height=height, width=width)
    except ValueError:
        # Expected to fail on initialization
        pass
    else:
        pytest.fail("Invalid height / width should raise error")
