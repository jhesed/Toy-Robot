from toy_robot.constants.pattern import PATTERN
from toy_robot.coordinate import Coordinate
from toy_robot.plane import Plane
from toy_robot.robot import Robot


class RobotConsoleRunner:
    """Exposes the toy robot functionality in a simple UI."""

    def __init__(self, world_width: int, world_height: int) -> None:
        self.world_width = world_width
        self.world_height = world_height

        self.robot = Robot(world=Plane(width=world_width, height=world_height))
        self.world_array = self.reset_world()

    def reset_world(self) -> list:
        """Generates a 2D array representation of world, with its initial
        values."""
        rows, cols = self.world_width, self.world_height
        self.world_array = [["-"] * cols for _ in range(rows)]
        return self.world_array

    def update_world(self):
        """Updates world based on the robot's new location.

        The robot is in the world as either
        one of these characters:

            * N: When the user is facing NORTH
            * E: for EAST
            * S: for SOUTH
            * W: for WEST
        """
        # Resets world before update to avoid
        # duplicate renders of the bot.
        self.world_array = self.reset_world()

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

    @classmethod
    def instantiate_runner(cls):
        """Instantiates a runner and the world."""
        while True:

            width = cls.get_dimension(dimension_name="width")
            if not width:
                continue

            height = cls.get_dimension(dimension_name="height")
            if not height:
                continue

            runner = cls(world_height=height, world_width=width)
            runner.reset_world()
            runner.render_world()
            return runner

    @classmethod
    def run(cls) -> None:
        """Runs an interactive console of toy robot."""

        runner = cls.instantiate_runner()

        while True:
            user_command = input(
                "Enter command (LEFT, RIGHT, MOVE, REPORT, PLACE, QUIT): "
            ).upper()
            if user_command == "QUIT":
                print("Thanks for playing. Bye.")
                return

            match = PATTERN.match(user_command.rstrip("\n"))
            if match is None:
                # Ignore invalid user inputs
                print(
                    "Invalid command. Please refer "
                    "to README for complete syntax of commands."
                )
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
                            "Ensure that the bot is placed in world."
                        )
                    else:
                        runner.update_world()
                else:
                    print(f"Invalid command `{command}`.")

    @staticmethod
    def get_dimension(dimension_name: str) -> int | None:
        """Retrieves, validates and sanitizes the dimension from user input."""
        try:
            dimension = int(
                input(f"Please enter world {dimension_name} (int): ")
            )
            if dimension <= 0:
                print(f"{dimension_name} should be > 0")
                return None
        except ValueError:
            print(f"{dimension_name} should be a valid int")
            return None
        else:
            return dimension


if __name__ == "__main__":
    RobotConsoleRunner.run()
