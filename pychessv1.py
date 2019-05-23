# Created by Daniel Lurie

# CONSTANTS
WHITE = 0
BLACK = 1

# CLASSES
class Piece:
    def __init__(self, c, n):
        self.color = -1
        self.name = "uninitialized"

class Pawn(Piece):
    WHITE_START_ROW = 1
    BLACK_START_ROW = 6

    def __init__(self, c, n, column):
        Piece.__init__(self, c, "Pawn")
        if c == WHITE:
            self.row = WHITE_START_ROW
        else:
            self.row = BLACK_START_ROW
        self.col = column

    def fw1():
        if self.color == WHITE:
            if self.row < 7:
                self.row += 1
            else:
                print("Error: Pawn cannot move forward. Too close to edge.")
        else:
            if self.row > 0:
                self.row -= 1
            else:
                print("Error, Pawn cannot move forward. Too close to edge.")

    def fw2():
        if self.color == WHITE && self.row == WHITE_START_ROW:
            self.row += 2
        elif self.color == BLACK && self.row == BLACK_START_ROW:
            self.row -= 2
        else:
            print("Error, Pawn cannot move forward")

class Rook(Piece):
    WHITE_START_ROW = 0
    BLACK_START_ROW = 7

    def __init__(self, c, column):
        Piece.__init__(self, c, "Rook")
        if c == WHITE:
            self.row = WHITE_START_ROW
        else:
            self.row = BLACK_START_ROW
        self.col = column
