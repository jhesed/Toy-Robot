"""Contains regex patterns to match user commands:

* **LEFT**: Rotate robot to the left
* **RIGHT**: Rotate robot to the right
* **MOVE**: Move bot 1 coordinate based on its current direction
* **REPORT**: Log current coordinate of bot
* **PLACE**: Place bot in the world based on the coordinate indicated
"""
import re

PATTERN = re.compile(
    r"""
    (?i)(?P<command>
        LEFT\s*$|
        RIGHT\s*$|
        MOVE\s*$|
        REPORT\s*$|
        (PLACE|OUTPUT:)
            (?=\s?                                    # spaces
            (?P<x>\d+),\s*                            # x coordinate
            (?P<y>\d+),\s*                            # y coordinate
            (?P<direction>NORTH|EAST|SOUTH|WEST)\s*   # direction
        $)
    )
    """,
    re.X,
)
