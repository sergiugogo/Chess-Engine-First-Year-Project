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
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.moveFuncitons = {'p': self.get_pawn_moves, 'R': self.get_rook_moves, 'N': self.get_knight_moves,
                              'B': self.get_bishop_moves, "Q":self.get_queen_moves, "K": self.get_king_moves}

        self.white_to_move = True
        self.move_log = []
    '''
    function that takes a move as a parameter and executes it. this will not work for 
    castling, en passant and pawn promotion.
    '''
    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move) #log the move so we can undo it later
        self.white_to_move = not self.white_to_move #swap players


    '''
    function that undoes the last move made
    '''

    def undo(self):
        if len(self.move_log) > 0: # make sure there is a move to remove
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

    '''
    all moves considering checks - includes all moves that could be followed by king capture
    '''

    def get_valid_moves(self):
        return self.get_all_possible_moves() # for now we don't worry about checks

    '''
    all moves without checks
    '''

    def get_all_possible_moves(self):
        moves = []
        for r in range(len(self.board)): # number of rows
            for c in range(len(self.board[r])): # number of columns
                turn = self.board[r][c][0]

                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]
                    self.moveFuncitons[piece](r, c, moves) #calls the appropriate move function based on piece type


        return moves

    '''
    all moves for a pawn situated at a row and column, adding moves to the list
    '''
    def get_pawn_moves(self, row, col, moves):
        if self.white_to_move: #white pawn moves
            if self.board[row-1][col] == '--': #1 square pawn advance
                moves.append(Move((row, col), (row-1, col), self.board))
                if row == 6 and self.board[row-2][col] == "--":
                    moves.append(Move((row, col), (row-2, col), self.board))
            if col-1 >=0:
                if self.board[row-1][col-1][0] == 'b': #enemy piece to capture
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            if col+1 <= 7:
                if self.board[row+1][col+1][0] == 'b':
                    moves.append(Move((row, col), (row-1, col+1), self.board))
        else: #black pawn moves
            if self.board[row+1][col] == '--':
                moves.append(Move((row, col), (row+1, col), self.board))
                if row == 1 and self.board[row+2][col] == "--":
                    moves.append(Move((row, col), (row+2, col), self.board))
            #captures
            if col-1 >= 0: #capture left
                if self.board[row+1][col-1][0] == 'w':
                    moves.append(Move((row, col), (row+1, col-1), self.board))
                if col+1 <= 7:
                    if self.board[row+1][col+1][0] == 'w':
                        moves.append(Move((row, col), (row+1, col+1), self.board))

    '''
    all moves for a rook situated at a row and column, adding moves to the list
    '''
    def get_rook_moves(self, row, col, moves):
        directions = ((-1, 0), (0,-1), (1,0), (0,1))
        enemy_color = "b" if self.white_to_move else "w"
        for d in directions:
            for i in range(1,8):
                end_row = row + d[0]*i
                end_col = col + d[1]*i
                if 0 <= end_row < 8 and 0 <= end_col < 8:#on board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':#valid move
                        moves.append(Move((row,col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color: #enemy space valid
                        moves.append(Move((row,col), (end_row, end_col), self.board))
                        break
                    else: break # friendly fire on
                else: break  # off board

    def get_knight_moves(self, row, col, moves):
        knight_moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        ally_color = "w" if self.white_to_move else "b"
        for n in knight_moves:
            end_row = row + n[0]
            end_col = col + n[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece == '--':
                    end_piece = self.board[end_row][end_col]
                    if end_piece[0] != ally_color:
                        moves.append(Move((row,col), (end_row, end_col), self.board))

    def get_bishop_moves(self, row, col, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1) )
        enemy_color = 'b' if self.white_to_move else 'w'
        for d in directions:
            for i in range(1,8):
                end_row = row + d[0]*i
                end_col = col + d[1]*i
                if 0<= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':
                        moves.append(Move((row,col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves.append(Move((row,col), (end_row, end_col), self.board))
                        break
                    else: break
                else:
                        break

    def get_queen_moves(self, row, col, moves):
        self.get_rook_moves(row, col, moves)
        self.get_bishop_moves(row, col, moves)

    def get_king_moves(self, row, col, moves):
        king_moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        ally_color = "w" if self.white_to_move else "b"
        for i in range(8):
            end_row = row + king_moves[i][0]
            end_col = col + king_moves[i][1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:
                    moves.append(Move((row,col), (end_row, end_col), self.board))


class Move():
    # maps keys to values
    # key : value
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    row_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b" : 1, "c" : 2, "d" : 3,
                   "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col


    '''
    overriding the equal method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False


    def get_chess_notation(self):
        #you can add to make this like real chess notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.row_to_ranks[r]