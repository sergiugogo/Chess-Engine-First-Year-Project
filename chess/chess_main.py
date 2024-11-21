'''
This is our main driver file. It is responsible for handling user input and displaying the current game_state object.
'''

import pygame as p
import chess_engine

p.init()
WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 # chess boards are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation
IMAGES = {}


'''
Initialize a global dictionary of images. This will be called exactly once in the main.
'''

def load_images():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    # Note: we can access an image by saying 'IMAGES["wp"]'

'''
The main driver for our code. This will handle user input and updating the graphics.
'''

def main():
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.game_state()

    valid_moves = gs.get_valid_moves()
    move_made = False # flag variable for when a move is made

    load_images() # only once, before the loop
    running = True
    sq_selected = () #no square is selected, keep track of the last click of the user (tuple: (row, col))
    player_clicks = []   #keep track of the player clicks (two tuples: [(6,4), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                print(f"Mouse clicked at {row}, {col}")
                if sq_selected == (row, col): #the user clicked the same square twice
                    sq_selected = () #deselect
                    player_clicks = []  #clear player clicks
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected) #append for boths 1st and 2nd clicks
                if len(player_clicks) == 2:  #after the 2nd click
                        move = chess_engine.Move(player_clicks[0], player_clicks[1], gs.board)
                        print(f"Trying to make move: {move.get_chess_notation()}")
                        if move in valid_moves:
                            gs.make_move(move)
                            print(f"Move made: {move.get_chess_notation()}")
                            move_made = True
                        else:
                            print(f"Invalid move: {move.get_chess_notation()}")
                        sq_selected = () #reset the user clicks
                        player_clicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # we undo a move if 'z' is pressed
                    gs.undo()
                    move_made = True
                    print("Move undone.")
            if move_made:
                print("Updating valid moves...")  # Debug log
                valid_moves = gs.get_valid_moves()
                move_made = False
                print(move_made)


        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
Responsible for all the graphics within a current game state.
'''
def draw_game_state(screen, gs):
    draw_board(screen) # draw squares on the board
    # add in piece highlighting or move suggestions
    draw_pieces(screen, gs.board) # draw pieces on top of the squares

'''
Draw the squares on the board
'''
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board using the current game_state.board
'''
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': # not an empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
if __name__ == '__main__':
    main()