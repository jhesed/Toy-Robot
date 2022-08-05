from toy_robot.constants.pattern import PATTERN
from toy_robot.coordinate import Coordinate
from toy_robot.plane import Plane
from toy_robot.robot import Robot


class RobotConsoleRunner:
    def __init__(self, world_width: int, world_height: int):
        self.world_width = world_width
        self.world_height = world_height

        self.robot = Robot(world=Plane(width=world_width, height=world_height))
        self.world_array = self.build_world()

    def build_world(self):
        rows, cols = self.world_width, self.world_height
        self.world_array = [["-"] * cols for _ in range(rows)]
        return self.world_array

    def update_world(self):
        self.world_array = self.build_world()  # Resets world before update

        try:
            self.world_array[self.robot.location.x][
                self.robot.location.y
            ] = self.robot.direction[0]

        except (IndexError, TypeError):
            print("Invalid command. Bot placement should be inside world.")
        else:
            self.render_world()

    def render_world(self):
        """Render world.

        Since (0,0) is located at southwest index, We need to rotate the
        2D list.
        """
        for row in list(reversed(list(zip(*self.world_array)))):
            print(row)


def instantiate_runner() -> RobotConsoleRunner:
    """Instantiates a runner and the world."""
    while True:
        try:
            width = int(input("Please enter world width (int): "))
        except ValueError:
            print("Incorrect width")
            continue

        try:
            height = int(input("Please enter world height (int): "))
        except ValueError:
            print("Incorrect height")
            continue

        runner = RobotConsoleRunner(world_height=height, world_width=width)
        runner.build_world()
        runner.render_world()
        return runner


def run() -> None:
    """Runs an interactive console of toy robot."""

    runner = instantiate_runner()

    while True:
        user_command = input(
            "Enter command (LEFT, RIGHT, MOVE, REPORT, PLACE, QUIT): "
        ).upper()
        if user_command == "QUIT":
            print("Thanks for playing. Bye.")
            return

        match = PATTERN.match(user_command.rstrip("\n"))
        if match is None:
            continue

        command = match.group("command").lower()
        if command:
            if command == "place":
                runner.robot = runner.robot.place(
                    location=Coordinate(
                        x=match.group("x"), y=match.group("y")
                    ),
                    direction=match.group("direction"),
                )
                runner.update_world()
            elif hasattr(runner.robot, command):
                try:
                    getattr(runner.robot, command)()
                except (ValueError, AttributeError):
                    print(
                        "Invalid command. "
                        "Ensure that bot is placed in world."
                    )
                else:
                    runner.update_world()
            else:
                print("Invalid command.")


if __name__ == "__main__":
    run()
