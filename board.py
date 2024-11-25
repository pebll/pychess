
from utils import Position, Util
from pieces import Piece, PieceType
from typing import Optional, List, Any


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.highlights = [[False for i in range(8)] for j in range(8)]
        self.util = Util()
        self.movement = Movement(self)
        #self._setup_board()

    
    def get_cell(self, pos : Position, board: List = None) -> Optional[Piece]:
        board = self.board if not board else board
        if not pos.is_valid():
            self.util.print_warning(f"Cell at {pos} is not valid! This should never happen!")
            return None
        return board[pos.y][pos.x]
    
    def get_pieces(self) -> List[Piece]:
        pieces = []
        for pos in self._all_positions():
            piece = self.get_cell(pos)
            if piece:
                pieces.append(piece)
        return pieces

    def get_possible_moves(self, piece: Piece):
        return self.movement.get_possible_moves(piece)

    def highlight_cells(self, cells: List[Position]):
        self._reset_highlights()
        for cell in cells:
            self._set_cell(True, cell, self.highlights)
    
    def _all_positions(self) -> List[Position]:
        positions = []
        for x in range(8):
            for y in range(8):
                positions.append(Position(x, y))
        return positions
    
    def _reset_highlights(self):
        for pos in self._all_positions():
            self._set_cell(False, pos, self.highlights)

    def _set_cell(self, value : Any, pos: Position, board: List = None):
        board = self.board if not board else board
        board[pos.y][pos.x] = value
    
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
        for y, row in enumerate(self.board):
            string += f" {str(y)} |"
            for x, piece in enumerate(row):
                highlight = self.get_cell(Position(x, y), self.highlights)
                if highlight:
                    start_format = "\033[1;33m"  # Bold and orange
                    end_format = "\033[0m"  # Reset to default
                else:
                    start_format = ""
                    end_format = ""
                if piece:
                    string += f"{start_format}{str(piece)} {end_format}"
                else:
                    cell = "◉︎" if highlight else "  "
                    string += f"{start_format}{cell}{end_format}"
                string += "|"
            string = string + "\n"
        string += "    a  b  c  d  e  f  g  h"
        return string 
class Movement():
    def __init__(self, board : Board):
        self.board = board

    def get_possible_moves(self, piece: Piece):
        assert self.board.get_cell(piece.pos) == piece
        params = MovementParameters(piece_type=piece.type)
        cells = []
        if params.horizontal:
            cells.extend(self._get_cells_in_direction(piece.pos, Position(1,0), piece.white))
            cells.extend(self._get_cells_in_direction(piece.pos, Position(-1,0), piece.white))
            cells.extend(self._get_cells_in_direction(piece.pos, Position(0,1), piece.white))
            cells.extend(self._get_cells_in_direction(piece.pos, Position(0,-1), piece.white))
        if params.diagonal:
            cells.extend(self._get_cells_in_direction(piece.pos, Position(1,1), piece.white))
            cells.extend(self._get_cells_in_direction(piece.pos, Position(1,-1), piece.white))
            cells.extend(self._get_cells_in_direction(piece.pos, Position(-1,1), piece.white))
            cells.extend(self._get_cells_in_direction(piece.pos, Position(-1,-1), piece.white))
        return cells

    def _get_cells_in_direction(self, start_pos: Position, direction: Position, white: bool) -> List[Position]:
        pos = start_pos
        cells = []
        while True: 
            pos += direction
            if not pos.is_valid():
                break
            piece = self.board.get_cell(pos)
            if piece:
                if piece.white == white: 
                    break
                else:
                    cells.append(pos)
                    break
            cells.append(pos)
        return cells


class MovementParameters():
    def __init__(self, piece_type: PieceType):
        self.horizontal = False
        if piece_type == PieceType.ROOK or piece_type == PieceType.QUEEN:
            self.horizontal = True
        self.diagonal = False
        if piece_type == PieceType.BISHOP or piece_type == PieceType.QUEEN:
            self.diagonal = True



