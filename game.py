from board import Board
from utils import Position
from pieces import Piece, PieceType


pos1 = Position(1,2)
board = Board()

print(board)

pieces = board.get_pieces()
print(f"piece: \n{str(pieces[0])}")
board.movement.get_possible_moves(piece=pieces[0])


