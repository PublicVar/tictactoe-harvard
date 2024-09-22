import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tictactoe import player, result, EMPTY, X, O

def test_player_with_empty_board_should_return_X():
    empty_board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert X == player(empty_board)

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
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    action = (1, 1)
    new_board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert new_board == result(board, action)

def test_result_with_action_overrided_existing_plays_should_raise_error():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    action = (1, 1)

    with pytest.raises(ValueError):
        result(board, action)
    
