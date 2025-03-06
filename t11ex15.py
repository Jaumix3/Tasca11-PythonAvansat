import pygame
import sys
import random

# Configuració de la pantalla
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inicialitzar pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Ratlla")
screen.fill(WHITE)

# Tauler de joc
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Dibuixar línies del tauler
def draw_lines():
    pygame.draw.line(screen, BLACK, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)

def draw_symbol(row, col, player):
    center_x = col * WIDTH // 3 + WIDTH // 6
    center_y = row * HEIGHT // 3 + HEIGHT // 6
    if player == 'X':
        pygame.draw.line(screen, RED, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), LINE_WIDTH)
        pygame.draw.line(screen, RED, (center_x + 50, center_y - 50), (center_x - 50, center_y + 50), LINE_WIDTH)
    else:
        pygame.draw.circle(screen, BLACK, (center_x, center_y), 50, LINE_WIDTH)

def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def ai_move():
    empty_cells = [(r, c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if board[r][c] is None]
    if empty_cells:
        return random.choice(empty_cells)
    return None

draw_lines()
player_turn = 'X'
game_mode = 2  # 1 = contra IA, 2 = dos jugadors
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // (HEIGHT // 3), x // (WIDTH // 3)
            if board[row][col] is None:
                board[row][col] = player_turn
                draw_symbol(row, col, player_turn)
                winner = check_winner()
                if winner:
                    print(f"Guanyador: {winner}")
                    game_over = True
                player_turn = 'O' if player_turn == 'X' else 'X'
        
        if game_mode == 1 and player_turn == 'O' and not game_over:
            move = ai_move()
            if move:
                board[move[0]][move[1]] = 'O'
                draw_symbol(move[0], move[1], 'O')
                winner = check_winner()
                if winner:
                    print(f"Guanyador: {winner}")
                    game_over = True
                player_turn = 'X'
    
    pygame.display.update()
