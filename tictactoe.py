#TicTacToe
#Plays TicTacToe against human
#Jaiden Lewis
#11/13/2020


#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#Build functions
################################################################
def displayIns():
    """Display Game instructions."""
    print("""
Welcome to the great intellectual challenge of all time. Tic Tac Toe.
This will be a showdown between your brain and a processor.

You will make your move by entering a number 0 - 8.
The number will correspond to the board position as illustrated.

            0 | 1 | 2
            _________
            
            3 | 4 | 5
            _________
            
            6 | 7 | 8

You better be prepared... \n
""")

def nextTurn(turn):
    """This function switches turns."""
    if turn == X:
        return O
    else:
        return X

def pieces():
    """Determines if you go first."""
    go_first = yesNo("Do you want to go first?")
    if go_first == "y" or "yes":
        print("n\Then take the first move. You'll need it.")
        human = X
        computer = O
    else:
        print("n\ Your bravery will be your death. I'll go first.")
        human = O
        computer = X
    return computer,human

def yesNo(question):
    """Ask a question and receive yes or no"""
    response = None
    while response not in ("y","n","no","yes"):
        response = input(question).lower()
    return response

def newBoard():
    """Create new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def displayBoard(board):
    print("\t",board[0]," | ",board[1]," | ",board[2]," | ")
    print("\t", "-----------------")
    print("\t",board[3]," | ",board[4]," | ",board[5]," | ")
    print("\t", "-----------------")
    print("\t",board[6]," | ",board[7]," | ",board[8]," | ")

def humanMove(board,human) :
    """Get human move"""
    move = None
    while move == None:
        move = askNumber("Where will you move? (0 - 8):", 0, NUM_SQUARES)
    return move

def askNumber(question, low, high):
    """Ask for a number within range"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response





################################################################



#Main game
def main():
    displayIns()
    turn = X
    computer,human = pieces()
    print(human)
    print(computer)
    board = newBoard()
    print(board)
    board[0] = X
    displayBoard(board)
    

main()
