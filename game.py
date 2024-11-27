#!/usr/bin/env python
from board import Board
from utils import Position
from keybinds import Keybind
from utils import Util

from typing import Optional
import sys
import keyboard

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.loop = False
        self.util = Util()
        self.board.setup_board()

    def start(self):
        self.loop = True
        while self.loop:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                self._handle_input(event.name)
            self._print_game_state()
        print("Thanks for playing!")

    def _print_game_state(self):
        sys.stdout.write("\033[H")
        print(self.board)

    def _handle_input(self, key : str):
        if key == Keybind.QUIT:
            sure = input("Quit: are you sure? Press Enter to continue")
            if sure == "":
                self.loop = False
        else: 
            self.util.print_warning(f"The key '{key}' is not a valid keybinding")

class Pointer:
    def __init__(self, white) -> None:
        self.white = white
        self.util = Util()
        self.pos : Position = Position(3,3) if white else Position(4,4)
        self.selected : Optional[Position] = None
    
    def move(self, direction : Position):
        if direction not in [Position(1,0), Position(-1, 0), Position(0,1), Position(0,-1)]:
            self.util.print_warning(f"Cannot move by into direction {direction}, can only move cardinally")
        new_pos = self.pos + direction
        if new_pos.is_valid():
            self.pos = new_pos
    
    def select(self, position : Position):
        self.seleceted = position

if __name__ == "__main__":
    game = Game()
    game.start()