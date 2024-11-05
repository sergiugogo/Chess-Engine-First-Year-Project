'''
This class is responsible for storing all the information about the current state of a chess game. It will also be responsible for
determining the valid moves at the current state. It will also keep a move log.
'''

class game_state():
    def __init__(self):
        # the board is an 8x8 2-dimensional list, each element has 2 characters.
        # the first - the color of the piece : 'b' or 'w'
        # the second - the type of the piece : 'K', 'Q', 'R', 'B', 'N' or 'P'
        # '--' represents an empty space or no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.move_log.append(move) #log the move so we can undo it later
        self.white_to_move = not self.white_to_move #swap players


class Move():
    # maps keys to values
    # key : value
    rankstorows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowtoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {"a": 0, "b" : 1, "c" : 2, "d" : 3,
                   "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    colstofiles = {v: k for k, v in filestocols.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]

    def getchessnotation(self):
        #you can add to make this like real chess notation
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.colstofiles[c] + self.rowtoranks[r]


