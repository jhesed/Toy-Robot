import pytest

from toy_robot.constants.direction_movement_map import NORTH, WEST, SOUTH, EAST
from toy_robot.coordinate import Coordinate
from toy_robot.plane import Plane
from toy_robot.robot import Robot

# Defining these variables once to be reusable across the tests.
WORLD: Plane = Plane(width=5, height=5)
LOCATION: Coordinate = Coordinate(x=0, y=0)


@pytest.mark.parametrize(
    argnames=("current_bot_direction", "expected_new_bot_direction"),
    argvalues=(
        (NORTH, EAST),
        (EAST, SOUTH),
        (SOUTH, WEST),
        (WEST, NORTH),
    ),
)
def test_rotate_right(
    current_bot_direction: str, expected_new_bot_direction: str
):
    assert (
        Robot(
            location=LOCATION,
            direction=current_bot_direction,
            world=WORLD,
        ).right()
        == expected_new_bot_direction
    )


@pytest.mark.parametrize(
    argnames=("current_bot_direction", "expected_new_bot_direction"),
    argvalues=(
        (NORTH, WEST),
        (EAST, NORTH),
        (SOUTH, EAST),
        (WEST, SOUTH),
    ),
)
def test_rotate_left(
    current_bot_direction: str, expected_new_bot_direction: str
):
    assert (
        Robot(
            location=LOCATION, direction=current_bot_direction, world=WORLD
        ).left()
        == expected_new_bot_direction
    )


@pytest.mark.parametrize(
    ("new_placement", "expected_new_location"),
    (
        # Case: New placement is INSIDE the plane
        (Coordinate(x=3, y=3), Coordinate(x=3, y=3)),
        # Case: New placement is OUTSIDE the plane: +x
        (Coordinate(x=6, y=5), LOCATION),
        # Case: New placement is OUTSIDE the plane: +y
        (Coordinate(x=5, y=6), LOCATION),
        # Case: New placement is OUTSIDE the plane: -x
        (Coordinate(x=-1, y=5), LOCATION),
        # Case: New placement is OUTSIDE the plane: -y
        (Coordinate(x=5, y=-1), LOCATION),
    ),
)
def test_placement(
    new_placement: Coordinate, expected_new_location: Coordinate
):
    """Placement should only happen within world.

    Placement is the same as initializing the robot.
    """
    assert (
        Robot(world=WORLD, location=LOCATION)
        .place(location=new_placement, direction=NORTH)
        .location
        == expected_new_location
    )


def test_invalid_mid_placement():
    """Invalid placement after a valid placement should return the previous."""
    assert (
        Robot(world=WORLD, location=LOCATION, direction=NORTH)
        .place(location=Coordinate(x=100, y=100), direction=NORTH)
        .location
        == LOCATION
    )


@pytest.mark.parametrize(
    ("current_bot_location", "current_bot_direction", "expected_new_location"),
    (
        # Scenario: Movement is INSIDE world
        # Case: Move left, INSIDE world
        (Coordinate(x=2, y=2), WEST, Coordinate(x=1, y=2)),
        # Case: Move right, INSIDE world
        (Coordinate(x=2, y=2), EAST, Coordinate(x=3, y=2)),
        # Case: Move up, INSIDE world
        (Coordinate(x=2, y=2), NORTH, Coordinate(x=2, y=3)),
        # Case: Move down, INSIDE world
        (Coordinate(x=2, y=2), SOUTH, Coordinate(x=2, y=1)),
        # Scenario: Movement is OUTSIDE world
        # Case: Move left, OUTSIDE world
        (Coordinate(x=0, y=0), WEST, Coordinate(x=0, y=0)),
        # Case: Move right, OUTSIDE world
        (Coordinate(x=4, y=4), EAST, Coordinate(x=4, y=4)),
        # Case: Move up, OUTSIDE world
        (Coordinate(x=4, y=4), NORTH, Coordinate(x=4, y=4)),
        # Case: Move down, OUTSIDE world
        (Coordinate(x=0, y=0), SOUTH, Coordinate(x=0, y=0)),
    ),
)
def test_move(
    current_bot_location: Coordinate,
    current_bot_direction: str,
    expected_new_location: Coordinate,
):
    assert (
        Robot(
            world=WORLD,
            location=current_bot_location,
            direction=current_bot_direction,
        ).move()
        == expected_new_location
    )


def test_report():
    expected_report_location = f"2,4,{EAST}"
    assert (
        Robot(
            world=WORLD, location=Coordinate(x=2, y=4), direction=EAST
        ).report()
        == expected_report_location
    )
