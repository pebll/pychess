
from utils import Position, Util
from pieces import Piece, PieceType
from typing import Optional, List


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.util = Util()
        self.movement = Movement(self)
        self._setup_board()

    
    def get_cell(self, pos : Position) -> Optional[Piece]:
        if not pos.is_valid():
            self.util.print_warning(f"Cell at {pos} is not valid! This should never happen!")
            return None
        return self.board[pos.y][pos.x]
    
    def get_pieces(self) -> List[Piece]:
        pieces = []
        for row in self.board:
            for piece in row:
                if piece:
                    pieces.append(piece)
        return pieces

    def _set_cell(self, value: Optional[Piece], pos: Position):
        self.board[pos.y][pos.x] = value
    
    def _place_piece(self, piece: Piece, pos: Position) -> bool:
        if self.get_cell(pos):
            self.util.print_warning("Cannot place piece here, position is not empty!")
            return False
        self._set_cell(piece, pos)
        piece.pos = pos
        return True
    
    def _setup_board(self):
        # Initialize white pieces
        self._place_piece(Piece(PieceType.ROOK, True), Position(0, 0))
        self._place_piece(Piece(PieceType.KNIGHT, True), Position(1, 0))
        self._place_piece(Piece(PieceType.BISHOP, True), Position(2, 0))
        self._place_piece(Piece(PieceType.QUEEN, True), Position(3, 0))
        self._place_piece(Piece(PieceType.KING, True), Position(4, 0))
        self._place_piece(Piece(PieceType.BISHOP, True), Position(5, 0))
        self._place_piece(Piece(PieceType.KNIGHT, True), Position(6, 0))
        self._place_piece(Piece(PieceType.ROOK, True), Position(7, 0))
        for x in range(8):
            self._place_piece(Piece(PieceType.PAWN, True), Position(x, 1))

        # Initialize black pieces
        self._place_piece(Piece(PieceType.ROOK, False), Position(0, 7))
        self._place_piece(Piece(PieceType.KNIGHT, False), Position(1, 7))
        self._place_piece(Piece(PieceType.BISHOP, False), Position(2, 7))
        self._place_piece(Piece(PieceType.QUEEN, False), Position(3, 7))
        self._place_piece(Piece(PieceType.KING, False), Position(4, 7))
        self._place_piece(Piece(PieceType.BISHOP, False), Position(5, 7))
        self._place_piece(Piece(PieceType.KNIGHT, False), Position(6, 7))
        self._place_piece(Piece(PieceType.ROOK, False), Position(7, 7))
        for x in range(8):
            self._place_piece(Piece(PieceType.PAWN, False), Position(x, 6))
    
    def __str__(self):
        string = ""
        for row in self.board:
            for piece in row:
                if piece:
                    string += f"{str(piece)}"
                else:
                    string += " "
                string += " |"
            string = string[:-1] + "\n"
        return string
        

class Movement():
    def __init__(self, board : Board):
        self.board = board

    def get_possible_moves(self, piece: Piece):
        assert self.board.get_cell(piece.pos) == piece
        params = MovementParameters(piece_type=piece.type)
        cells = []
        if params.horizontal:
            pos = piece.pos
            stop = False
            while not stop:
                pos += Position(1, 0)
                #if pos.is_valid() ...
                #self.board.get_cell(pos + offset)
                pass



class MovementParameters():
    def __init__(self, piece_type: PieceType):
        self.horizontal = False
        if piece_type == PieceType.ROOK or piece_type == PieceType.QUEEN:
            self.horizontal = True
        self.diagonal = False
        if piece_type == PieceType.BISHOP or piece_type == PieceType.QUEEN:
            self.diagonal = True



