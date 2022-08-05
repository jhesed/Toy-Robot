import pytest

from toy_robot.coordinate import Coordinate


@pytest.mark.parametrize(
    argnames=("xy_coordinate", "expected_value"),
    argvalues=(
        # Case: str to number
        ("1", 1),
        # Case: int should be retained as int
        (-1, -1),
        # Case: float to number
        (0.0, 0),
    ),
)
def test_xy_normalization(
    xy_coordinate: str | int | float, expected_value: int
):
    """Data types of both `x` and `y` coordinates should be normalized during
    setup, and should be of type int."""
    coord = Coordinate(x=xy_coordinate, y=xy_coordinate)
    assert all(
        getattr(coord, attr) == expected_value
        and isinstance(getattr(coord, attr), int)
        for attr in ("x", "y")
    )


@pytest.mark.parametrize(
    argnames=("x", "y", "expected_exception"),
    argvalues=(
        (1, "INVALID_Y_VALUE", ValueError),
        ("INVALID_X_VALUE", 1, ValueError),
    ),
)
def test_invalid_xy_values(
    x: int | str, y: int | str, expected_exception: Exception | ValueError
):
    """Users should be prevented to create a coordinate from invalid x and y
    values."""
    try:
        Coordinate(x=x, y=y)
    except expected_exception:
        # Expected to raise an exception due to invalid value
        pass
    else:
        pytest.fail("Invalid x / y value should raise ValueError")


def test_comparison():
    """Asserts comparison between coordinates."""
    assert Coordinate(x=1, y=1) >= Coordinate(x=1, y=0)
    assert Coordinate(x=2, y=1) > Coordinate(x=1, y=0)
    assert Coordinate(x=2, y=2) <= Coordinate(x=2, y=2)
    assert Coordinate(x=1, y=1) < Coordinate(x=2, y=2)
    assert Coordinate(x=1, y=1) == Coordinate(x=1, y=1)
