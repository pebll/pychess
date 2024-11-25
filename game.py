from board import Board
from utils import Position
from pieces import Piece, PieceType


pos1 = Position(1,2)
board = Board()


board._place_piece(Piece(PieceType.ROOK, True), Position(6, 2))
board._place_piece(Piece(PieceType.KNIGHT, True), Position(6, 3))
board._place_piece(Piece(PieceType.BISHOP, True), Position(2, 7))
board._place_piece(Piece(PieceType.QUEEN, True), Position(3, 2))
board._place_piece(Piece(PieceType.ROOK, False), Position(1, 1))
board._place_piece(Piece(PieceType.KNIGHT, False), Position(4, 4))
board._place_piece(Piece(PieceType.BISHOP, False), Position(6, 5))
board._place_piece(Piece(PieceType.QUEEN, False), Position(4, 2))

print(board)
pieces = board.get_pieces()
print()
for piece in pieces:
    print(f"piece: \n{str(piece)}")
    moves = board.get_possible_moves(piece=piece)
    board.highlight_cells(moves)
    print(board)
    print()



