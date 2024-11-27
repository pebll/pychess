from utils import Position
from enum import Enum
from typing import Optional

class PieceType(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    BISHOP = 4
    KNIGHT = 5
    PAWN = 6

    def __str__(self):
        return self.name.lower()


        
class Piece():
    def __init__(self, type: PieceType, white: bool):
        self.type = type
        self.white = white
        self.pos : Optional[Position] = None
    
    def __str__(self):
        unicode_pieces = {
            'king': ('♔', '♚'),
            'queen': ('♕', '♛'),
            'rook': ('♖', '♜'),
            'bishop': ('♗', '♝'),
            'knight': ('♘', '♞'),
            'pawn': ('♙', '♟')
        }
        piece_char = unicode_pieces[str(self.type)][0] if self.white else unicode_pieces[str(self.type)][1]
        return piece_char

    


