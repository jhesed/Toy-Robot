"""These tests use the actual examples indicated in the PDF document.

It parses these files under `tests/test_integration/data` and matches
the `Output` text with the report from the bot
"""
import os

from tests.test_unit.test_robot import WORLD
from toy_robot.constants.pattern import PATTERN
from toy_robot.coordinate import Coordinate
from toy_robot.robot import Robot

DATA_PATH = f"{os.path.dirname(__file__)}/data"


def run_via_file(file_location: str) -> dict:
    """Runs toy bot against a txt file.
    :returns: Example:
        {'expected_output': '0,1,NORTH', 'actual_output': '0,1,NORTH'}
    """

    reports = {}

    # Initialize a bot
    robot = Robot(
        world=WORLD,
    )
    found_valid_place_command = False

    with open(file_location, "r") as _file:
        for line in _file:
            match = PATTERN.match(line.rstrip("\n"))
            if match is None:
                continue

            command = match.group("command").lower()

            if command == "place":

                robot = robot.place(
                    location=Coordinate(
                        x=match.group("x"), y=match.group("y")
                    ),
                    direction=match.group("direction"),
                )
                if robot.direction and robot.location:
                    found_valid_place_command = True
            elif command == "output:":
                reports["expected_output"] = (
                    f"{match.group('x')},"
                    f"{match.group('y')},"
                    f"{match.group('direction')}"
                )
            elif hasattr(robot, command) and found_valid_place_command:
                getattr(robot, command)()

    reports["actual_output"] = f"{str(robot.location)},{robot.direction}"
    return reports


def test_integration_via_file():
    """Retrieves all files in the data/ directory and compares `Output` with
    the currently result of the bot."""
    for file_name in os.listdir(DATA_PATH):
        print(f"{'-'*20} Processing file {file_name}")
        result = run_via_file(file_location=f"{DATA_PATH}/{file_name}")
        assert result["actual_output"] == result["expected_output"]
        print(f"Test case passed. {result}")
