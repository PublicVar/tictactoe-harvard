import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tictactoe import player, result, winner, terminal, EMPTY, X, O

EMPTY_BOARD = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def test_player_with_empty_board_should_return_X():

    assert X == player(EMPTY_BOARD)

def test_player_when_X_has_played_first_should_return_O():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert O == player(board)

def test_player_when_O_has_played_should_return_X():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, O]]

    assert X == player(board)

def test_result_with_valid_action_should_return_new_board():
    board = EMPTY_BOARD

    action = (1, 1)
    new_board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert new_board == result(board, action)

    assert board == EMPTY_BOARD

def test_result_with_action_overrided_existing_plays_should_raise_error():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    action = (1, 1)

    with pytest.raises(ValueError):
        result(board, action)
    
def test_winner_when_X_has_won_horizontally():
    board = [[X, X, X],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert X == winner(board)

def test_winner_when_0_has_won_horizontally():
    board = [[EMPTY, EMPTY, EMPTY],
            [O, O, O],
            [EMPTY, EMPTY, EMPTY]]

    assert O == winner(board)

def test_winner_when_X_has_won_vertically():
    board = [[X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY]]

    assert X == winner(board)

def test_winner_when_0_has_won_vertically():
    board = [[EMPTY, EMPTY, O],
            [EMPTY, EMPTY, O],
            [EMPTY, EMPTY, O]]

    assert O == winner(board)

def test_winner_when_0_has_won_diagonal_down():
    board = [[O, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, O]]

    assert O == winner(board)

def test_winner_when_X_has_won_diagonal_up():
    board = [[EMPTY, EMPTY, X],
            [EMPTY, X, EMPTY],
            [X, EMPTY, EMPTY]]

    assert X == winner(board)

def test_terminal_return_true_when_board_is_full():
    board = [[O, O, X],
            [O, X, O],
            [X, O, X]]

    assert True == terminal(board)

def test_terminal_return_false_when_board_is_not_full():
    board = [[O, O, EMPTY],
            [O, X, O],
            [X, O, X]]

    assert False == terminal(board)
