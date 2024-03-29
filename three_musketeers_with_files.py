import random
import pickle
import os
# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    valid_input = "ABCDE12345"
    axis_converter = {"A":0,"B":1,"C":2,"D":3,"E":4,"1":0,"2":1,"3":2,"4":3,"5":4}

    if s[0] in valid_input and s[1] in valid_input:
        return (axis_converter[s[0]], axis_converter[s[1]])
    else:
        raise ValueError("Invalid input")
    

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    num = [0,1,2,3,4]
    x = {0:"A",1:"B",2:"C",3:"D",4:"E"}
    y = {0:"1",1:"2",2:"3",3:"4",4:"5"}
    
    try:
        user_input = (num.index(location[0]), num.index(location[1]))
        return x[location[0]] + y[location[1]]
        
    except(ValueError):
        print("Invalid input")

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    every_location = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            every_location.append((i,j))
    return every_location

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""

    if direction == "up":
        adj_location = (location[0]-1, location[1])
        return adj_location
    elif direction == "down":
        adj_location = (location[0]+1, location[1])
        return adj_location
    elif direction == "right":
        adj_location = (location[0], location[1]+1)
        return adj_location
    else:
        adj_location = (location[0], location[1]-1)
        return adj_location
    

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    M = "M"
    
    try:
        at(location) == M
    except(ValueError):
        print("A musketeer is not at this location")

    #Checks if location is within the board and if the location is occupied by an enemy (R).
    if adjacent_location(location, direction) in all_locations() and at(adjacent_location(location, direction)) == "R":
        return True

    else: return False

 
def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""

    try:
        at(location) == "R"
    except(ValueError):
        print("A musketeer is not at this location")

    #Checks if location is within the board and if the location is empty.
    if adjacent_location(location, direction) in all_locations() and at(adjacent_location(location, direction)) == "-":
        return True
    
    else: return False


def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    #I am assuming location given will always be a non-empty location.

    if at(location) == "M":
        return is_legal_move_by_musketeer(location, direction)
    else:
        return is_legal_move_by_enemy(location, direction)

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""

    directions = ["right","left","up","down"]
    if at(location) == "M" or at(location) == "R":
        for i in directions:
            if is_legal_move(location, i)==True:
                break
            #else:
                #continue

        return is_legal_move(location, i)
                    
    else:
        return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    flag = False

    # Checks through all locations to find a player.
    # Whenever a player is found, location of the player
    # is passed into the can_move_piece_at function, to
    # find if there is atleast a move available.
    if who == "M":
        for i in all_locations():
            if at(i) == "M":
                if can_move_piece_at(i) == True:
                    flag = True
                    break
            
    if who == "R":
        for i in all_locations():
            if at(i) == "R":
                if can_move_piece_at(i) == True:
                    flag = True
                    break
        
    return flag

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""

    directions = ["left","right","up","down"]   #possible directions are added
    legal_directions = []                       # to legal_directions list
    if at(location) == "M" or at(location) == "R":
        for i in directions:
            if is_legal_move(location, i):
                legal_directions.append(i)
                
        return legal_directions
    
    else: return []
                

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will be a pair of integer numbers."""
    
    if location in all_locations():
        return True
    else: return False
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    
    if adjacent_location(location, direction) in all_locations():
        return True
    else: return False

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    
    possible_locations = []

    for i in all_locations():
        if at(i) == player:
            if len(possible_moves_from(i)) >= 1:     #if there are moves available
                for j in possible_moves_from(i):     #add location & directions
                    possible_locations.append((i,j)) #to the list as a tuple

    return possible_locations
    
    

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""

    board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]] = at(location) 
        
    board[location[0]][location[1]] = "-"


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    #Selects a random move from all possible moves available for the player.
    
    return random.choice(all_possible_moves_for(who))

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    lst = []
    for i in all_locations():
        if at(i) == "M":
            lst.append(i)
    if lst[0][0] == lst[1][0] == lst[2][0] or lst[0][1] == lst[1][1] == lst[2][1]:
        return True
    else: return False

def save():
    print("Saved")

    pickle.dump(board, open("board.txt", "wb"))
    pickle.dump(users_side, open("user.txt", "wb"))

def load():
    load_game = input("If you would like to load a previous game, "
                      "\ntype in 'YES', "
                      "otherwise type in 'NO' ").upper()

    if load_game == "YES":
        board = pickle.load(open("board.txt", "rb"))
        global users_side
        users_side = pickle.load(open("user.txt", "rb"))
        set_board(board)
        
        if is_enemy_win():
                    print("Cardinal Richleau's men win!")
        else: pass


        if users_side == "M":
            print()
            print("You are playing as the Musketeer (M)")
            print()
            print_board()
            continue_as_musketeer()
        else:
            print()
            print("You are playing as the enemy (R)")
            print()
            print_board()
            continue_as_enemy()
    elif load_game == "NO":
        pass

    else:
        print("Do not understand " + load_game + ". Try again.")
        load()
    
        
     
#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()
    print("""The game is saved automatically after every move""")

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    global users_side
    # convert directory to a string
    # then replace all '\\' with '/'
    # because python only recognises directories with '/'
    # therefore measures must be taken so that it can work (save) on
    # Windows aswell as Mac.
    
    directory = str(os.getcwd())
    directory.replace('\\','/')
    exists1 = os.path.isfile(directory+'/user.txt')
    exists2 = os.path.isfile(directory+'/board.txt')
    if exists1 and exists2:
        load() 
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            save()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
            save()
        else:
            print("The Musketeers win!")
            break

def continue_as_musketeer():
    
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            save()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
            save()
        else:
            print("The Musketeers win!")
            break

def continue_as_enemy():
    
    if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
            save()
    else:
        print("The Musketeers win!")
        
    continue_as_musketeer()
