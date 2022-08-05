"""Contains constant variables for direction and movement.

* **MOVEMENT**: how much coordinate should be added
to an object's location based on direction.
* **DIRECTIONS**: Typical NORTH, SOUTH, EAST, WEST
"""

from collections import OrderedDict

from toy_robot.coordinate import Coordinate

# Directions
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"


# Format:
#     <direction>:
#     <How much coordinate should be added to move
#       it to the specified direction>
#
# I'm sure that these values can be generated via a mathematical function,
# but for simplicity, these are pre-computed already and should
# only be computed once.
MOVEMENT: OrderedDict = OrderedDict(
    {
        NORTH: Coordinate(x=0, y=1),
        EAST: Coordinate(x=1, y=0),
        SOUTH: Coordinate(x=0, y=-1),
        WEST: Coordinate(x=-1, y=0),
    }
)

# List of directions without the mapping for movement.
DIRECTIONS: list = list(MOVEMENT.keys())
