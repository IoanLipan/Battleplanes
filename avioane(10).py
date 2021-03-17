from random import randint

board = []

for x in range(0,10):
    board.append(['0 '] *10)

def print_board(board):
    for row in board:
        print (' '.join(row))

def random_row(board):
    return randint(1, len(board)-2)

def random_col(board):
    return randint(1, len(board[0])-2)

plane_row = random_row(board)
plane_col = random_col(board)

print_board(board)

for turn in range(25):
    print ("Turn: {}".format(turn+1))
    guess_row = int(input("Guess Row:"))
    guess_col = int(
        input("Guess Col:"))

    if  guess_row == plane_row and guess_col == plane_col or \
        guess_row == plane_row-1 and guess_col == plane_col or \
        guess_row == plane_row+1 and guess_col == plane_col or \
        guess_row == plane_row and guess_col == plane_col-1 or \
        guess_row == plane_row and guess_col == plane_col+1 :
        print("Congrats! You guessed right! :D")
        break
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print("Not on the board.. try harder! :-?")
        elif(board[guess_row][guess_col] == "X "):
            print("Already missed that. >:(")
        else:
            print("You missed.. :(")
            board[guess_row][guess_col] = "X "
    if turn == 24:
        print("You lost! :((")
    turn =+ 1
    print_board(board)

board[plane_row][plane_col] = 'M '
board[plane_row-1][plane_col] = 'M '
board[plane_row+1][plane_col] = 'M '
board[plane_row][plane_col-1] = 'M '
board[plane_row][plane_col+1] = 'M '
print_board(board)