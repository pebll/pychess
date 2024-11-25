from colorama import Fore, Style, init

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Position to Position")

    def is_valid(self) -> bool: 
        if self.x < 0 or self.x > 7 or self.y < 0 or self.y > 7:
            return False
        return True

class Util:
    def __init__(self):
        pass

    def print_warning(self, message):
        init(autoreset=True)
        print(Fore.YELLOW + Style.BRIGHT + "Warning: " + message)