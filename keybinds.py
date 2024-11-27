from enum import Enum

class Keybind(Enum):
    QUIT = "q"
    ENTER_1 = "e"
    UP_1 = "w"
    RIGHT_1 = "d"
    DOWN_1 = "s"
    LEFT_1 = "a"
    ENTER_2 = "page down"
    UP_2 = "up"
    RIGHT_2 = "right"
    DOWN_2 = "down"
    LEFT_2 = "left"

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        return super().__eq__(other)