"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_played = sum(row.count(X) + row.count(O) for row in board)

    if number_of_played  == 0:
        return X

    if number_of_played  % 2 != 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_to_move = player(board)

    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player_to_move
    else:
        raise ValueError("Invalid move")

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal winner
    horizontal_winner = [row for row in board if row == [X,X,X] or row == [O,O,O]]

    if len(horizontal_winner) > 0:
        return horizontal_winner[0][0]

    # Vertical winner
    for col_line in range(3):
        if board[0][col_line] == board[1][col_line] == board[2][col_line] and board[0][col_line] != EMPTY:
            return board[0][col_line]

    # Diagonal winner 
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    row_full = [row for row in board if row.count(EMPTY) == 0]

    return len(row_full) == 3


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
