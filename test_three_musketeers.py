import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(KeyError, message = "Invalid location"):
        string_to_location('X3')
    assert string_to_location('A0') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    assert location_to_string((2,2)) == "C3"

def test_at():
     assert at((1,1)) == _
     assert at((4,3)) == R
     assert at((2,2)) == M
     assert at((0,3)) == M

def test_all_locations():
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),
                               (1,0),(1,1),(1,2),(1,3),(1,4),
                               (2,0),(2,1),(2,2),(2,3),(2,4),
                               (3,0),(3,1),(3,2),(3,3),(3,4),
                               (4,0),(4,1),(4,2),(4,3),(4,4)]
    

def test_adjacent_location():
    assert adjacent_location((0,4),down) == (1,4)
    #assert adjacent_location((3,3),"left") == (3,2)
    #assert adjacent_location((4,1),"up") == (3,1)
    
    
def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer((2,2),"up") == True
    
def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy((0,0),"down") == False

def test_is_legal_move():
    assert is_legal_move((0,0), "right") == True
    assert is_legal_move((0,4), "left") == True

def test_can_move_piece_at():
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((0,0)) == False

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    assert possible_moves_from((0,0)) == ["right", "down"]
    

def test_is_legal_location():
    assert is_legal_location((2,2)) == True
    assert is_legal_location((1,5)) == False

def test_is_within_board():
    assert is_within_board((2,2), "left") == True
    assert is_within_board((0,0), "up") == False

def test_all_possible_moves_for():
    assert all_possible_moves_for("M") == [(2,3),(3,2),(2,1),(1,2),
                                           (0,3),(1,4),(3,0),(4,1)]
    
def test_make_move():
    if make_move((2,2), "left"):
        assert board[location[2],location[1]] == "M"
    
def test_choose_computer_move():
    assert choose_computer_move("M") == ((2,3) , "right")
    assert choose_computer_move("R") == ((0,0) , "down")

def test_is_enemy_win():
    assert is_enemy_win() == False 


