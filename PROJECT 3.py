import numpy as np
# ---------------------varieables--------------------

game_not_over = False

turn = 0

ROW_COUNT = 6

COLUMN_COUNT = 7
# --------------------functions----------------------


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_coin(board, row, coulumn, coin):
    board[row][coulumn] = coin


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, coin):
    # check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == coin and board[r][c+1] == coin and board[r][c+2] and board[r][c+3] == coin:
                return True

    # check  vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == coin and board[r+1][c] == coin and board[r+2][c] and board[r+3][c] == coin:
                return True

    # check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == coin and board[r+1][c+1] == coin and board[r+2][c+2] and board[r+3][c+3] == coin:
                return True

    # check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == coin and board[r-1][c+1] == coin and board[r-2][c+2] and board[r-3][c+3] == coin:
                return True


board = create_board()
# ----------------------main loop---------------------
print(board)
while not game_not_over:
    # ask player 1's input
    if turn == 0:
        col = int(
            input("Where would you like to play, player 1? (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_coin(board, row, col, 1)
            if winning_move(board, 1):
                print_board(board)
                print("PLAYER 1 WINS!!! CONGRATS!")
                game_over = True
                break

        # ask player 2's input
    else:
        col = int(
            input("Where would you like to play, player 2? (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_coin(board, row, col, 2)
            if winning_move(board, 2):
                print_board(board)
                print("PLAYER 2 WINS!!! CONGRATS!")
                game_over = True
                break

    print_board(board)
    turn += 1
    turn %= 2
