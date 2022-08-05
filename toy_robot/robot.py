from toy_robot.constants.direction_movement_map import (
    MOVEMENT,
    DIRECTIONS,
)
from toy_robot.coordinate import Coordinate
from toy_robot.plane import Plane


class Robot:
    def __init__(
        self, world: Plane, direction: str = None, location: Coordinate = None
    ):
        """
        :param direction: Direction where the bot is currently
        facing, e.g. in (NORTH, SOUTH, EAST, WEST)
        :param world: The world where the bot resides,
        e.g. a table, a 2D plane, etc.
        :param location: Current location of the bot in the `world`
        """
        self.world = world

        self.direction = direction
        if location:
            self.location = location

    def move(self) -> Coordinate | None:
        """Moves the bot one point at a time, with respect to the current
        direction it is facing.

        *Note:*

            * `location` property won't allow updates if movement
            will fall outside world.
        """

        self.location = self.location + MOVEMENT[self.direction]
        return self.location

    def right(self):
        """Rotates bot to right.

        Examples:

            * From NORTH to EAST
            * From EAST to SOUTH

        Logic explained:

            * Let DIRECTIONS = (NORTH, EAST, SOUTH, "WEST)
            * Rotating left means adding one index from current in this list.
            Example, NORTH-> LEFT
            * For the last element WEST->NORTH, modulo was used to
            return to the first index.

        # TODO: Future improvement: Move out index computation to avoid O(n)
        """
        self.direction = DIRECTIONS[
            (DIRECTIONS.index(self.direction) + 1) % len(DIRECTIONS)
        ]
        return self.direction

    def left(self):
        """Rotates bot to left.

        Refer to `right` method for more details.
        """
        self.direction = DIRECTIONS[
            (DIRECTIONS.index(self.direction) - 1) % len(DIRECTIONS)
        ]
        return self.direction

    def report(self) -> str:
        """Logs the current location of the bot.

        **Format:**

            <x>,<y>,<direction>

        Example response: `0,1,NORTH`
        """
        response = f"{str(self.location)},{self.direction}"
        print(response)
        return response

    @property
    def location(self):
        """A `coordinate` of the bot's current location."""
        return self._location

    @location.setter
    def location(self, value: Coordinate):
        """Ensures that `value` is a valid location and will fall inside
        `world`"""
        if self.world.is_inside_plane(coordinate=value) is False:
            print(
                f"Retaining current location {self.location} "
                "to avoid falling out from world with new "
                f"position {value}"
            )
            return
        self._location = value

    def place(self, location: Coordinate, direction: str):
        """Places the robot in the `world` provided the `location`.

        If the `location` given is outside world, `location` setter will
        raise an attribute error. In this case, we'll return the most
        recent valid bot placement.
        """
        try:
            return Robot(
                direction=direction, world=self.world, location=location
            )
        except AttributeError:
            if self.direction and self.location:
                print(
                    f"Invalid bot placement {location}. "
                    "Using the last known valid placement"
                )
            return self
