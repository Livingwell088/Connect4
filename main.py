

# Connect 4 Game

# 6 Rows and 7 Columns

import numpy as np
import pygame
import math
import sys



ROW_COUNT = 6
COLUMN_COUNT = 7


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)




def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, selection, piece):
    board[row][selection] = piece

def is_valid_location(board, selction):
    return board[ROW_COUNT-1][selction] == 0

def get_next_open_row(board, selection):
    for r in range(ROW_COUNT):
        if board[r][selection] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            # Check for horizontal locations for winning
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c + 3] == piece:
                return True

            # Check for vertical locations for winning
    for c in range(COLUMN_COUNT) :
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

            # Check for + sloped winning move
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                        return True

            # Check for - sloped winning move
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                        return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0




pygame.init()


over_text = pygame.font.Font("Metal Lady - Personal Use.otf", 100)

SQUARE_SIZE = 100
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
RADIUS = int(SQUARE_SIZE/2 - 5)


size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()





# Game Loop

running = True
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)
        pygame.display.update()



        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))

            if turn == 0:
                posx = event.pos[0]
                selection = int( math.floor(posx/SQUARE_SIZE))

                if is_valid_location(board, selection):
                    row = get_next_open_row(board, selection)
                    drop_piece(board, row, selection, 1)

                    if winning_move(board, 1):
                        label = over_text.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True


            else:
                posx = event.pos[0]
                selection = int(math.floor(posx / SQUARE_SIZE))

                if is_valid_location(board, selection):
                    row = get_next_open_row(board, selection)
                    drop_piece(board, row, selection, 2)

                    if winning_move(board, 2):
                        label = over_text.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)












































