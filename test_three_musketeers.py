import random
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

board2 =  [ [_, _, _, M, _],
            [_, _, R, _, _],
            [_, R, _, R, _],
            [_, R, R, _, _],
            [M, _, _, _, M] ]

board3 = [  [_, _, _, _, M],
            [_, _, R, _, _],
            [_, R, _, R, _],
            [_, R, R, _, M],
            [_, _, _, _, M] ] 

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
    with pytest.raises(ValueError):
        raise ValueError("X3")
        raise ValueError("B6")
    assert string_to_location("A1") == (0,0)
    assert string_to_location("C4") == (2,3)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        raise ValueError((2,5))
        raise ValueError((-1,2))
    assert location_to_string((2,2)) == "C3"
    assert location_to_string((1,4)) == "B5"

def test_at():
     assert at((1,1)) == _
     assert at((4,3)) == R
     assert at((2,2)) == M
     assert at((0,3)) == M
     set_board(board2)
     assert at((3,2)) == R

def test_all_locations():
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),
                               (1,0),(1,1),(1,2),(1,3),(1,4),
                               (2,0),(2,1),(2,2),(2,3),(2,4),
                               (3,0),(3,1),(3,2),(3,3),(3,4),
                               (4,0),(4,1),(4,2),(4,3),(4,4)]
    

def test_adjacent_location():
    set_board(board1)
    assert adjacent_location((0,4),down) == (1,4)
    assert adjacent_location((3,3),"left") == (3,2)
    assert adjacent_location((4,1),"up") == (3,1)
    
    
def test_is_legal_move_by_musketeer():
    with pytest.raises(ValueError):
        raise ValueError(at((2,1)) == R)
    assert is_legal_move_by_musketeer((2,2),"up") == True
    assert is_legal_move_by_musketeer((2,2),"down") == False
    assert is_legal_move_by_musketeer((0,3),"down") == False
    
def test_is_legal_move_by_enemy():
    with pytest.raises(ValueError):
        raise ValueError(at((0,0)) == _)
        raise ValueError(at((4,4)) == _)
        raise ValueError(ar((2,2)) == M)
    assert is_legal_move_by_enemy((2,1),"down") == False
    assert is_legal_move_by_enemy((3,1),"down") == True
    assert is_legal_move_by_enemy((1,2),"left") == True
    assert is_legal_move_by_enemy((2,3),"left") == False
    

def test_is_legal_move():
    assert is_legal_move((2,2), "right") == True
    assert is_legal_move((0,3), "up") == False

    assert is_legal_move((3,1), "up") == False
    assert is_legal_move((4,3), "left") == True

def test_can_move_piece_at():
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((0,0)) == False
    assert can_move_piece_at((0,3)) == False
    assert can_move_piece_at((4,3)) == True
    assert can_move_piece_at((2,1)) == True
    

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,2)) == ["left","right","up"]
    assert possible_moves_from((2,1)) == ["left","up"]
    assert possible_moves_from((0,0)) == []
    assert possible_moves_from((0,3)) == []
    
    

def test_is_legal_location():
    assert is_legal_location((2,2)) == True
    assert is_legal_location((1,5)) == False
    assert is_legal_location((5,2)) == False
    assert is_legal_location((0,4)) == True
    assert is_legal_location((-1,4)) == False

def test_is_within_board():
    assert is_within_board((2,2), "left") == True
    assert is_within_board((0,0), "up") == False
    assert is_within_board((0,4), "right") == False
    assert is_within_board((0,3), "down") == True

def test_all_possible_moves_for():
    assert all_possible_moves_for("M") == [((1,3),"left"),((1,3),"down"),
                                           ((2,2),"left"),((2,2),"right"),
                                           ((2,2),"up")]

    assert all_possible_moves_for("R") == [((1,2),"left"),((1,2),"up"),
                                           ((2,1),"left"),((2,1),"up"),
                                           ((2,3),"right"),((2,3),"down"),
                                           ((3,1),"left"),((3,1),"right"),
                                           ((3,1),"down"),((4,3),"left"),
                                           ((4,3),"right"),((4,3),"up")]
    
def test_make_move():
    # need more tests
    make_move((2,2), "left")
    assert board1 == [[_, _, _, M, _],
                      [_, _, R, M, _],
                      [_, M, _, R, _],
                      [_, R, _, _, _],
                      [_, _, _, R, _] ]
    
def test_choose_computer_move():
    assert choose_computer_move("M") == ((1,3) , "left")
    assert choose_computer_move("R") == ((3,1) , "down")

def test_is_enemy_win():
    assert is_enemy_win() == False
    set_board(board3)
    assert is_enemy_win() == True
    


