from board import Board
from utils import Position
from pieces import Piece, PieceType
from random import sample

pos1 = Position(1,2)
board = Board()

random_board = False

if random_board:
    positions = sample(board._all_positions(), 18)
    pieces = [PieceType.KING, PieceType.BISHOP, PieceType.QUEEN, PieceType.ROOK, PieceType.KNIGHT, PieceType.PAWN, PieceType.PAWN, PieceType.PAWN, PieceType.PAWN]
    for i, type in enumerate(pieces):
        for j, white in enumerate([True, False]):
            if True:
                board._place_piece(Piece(type, white), positions[2 * i + j])
else:
    board._setup_board()

print(board)
board.print_reverse = True

pieces = board.get_pieces()
print()
for piece in pieces:
    print(f"piece: \n{str(piece)}")
    board._reset_highlights()
    board.highlight_possible_moves(piece)
    print(board)
    print()



