# TicTacToe
# Plays TicTacToe against human
# Jaiden Lewis
# 11/13/2020


# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


# Build functions
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
    if go_first == "y" or go_first == "yes":
        print("n\Then take the first move. You'll need it.")
        human = X
        computer = O
    else:
        print("n\ Your bravery will be your death. I'll go first.")
        human = O
        computer = X
    return computer, human


def yesNo(question):
    """Ask a question and receive yes or no"""
    response = None
    while response not in ("y", "n", "no", "yes"):
        response = input(question).lower()
    return response


def newBoard():
    """Create new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def displayBoard(board):
    print("\t", board[0], " | ", board[1], " | ", board[2], " | ")
    print("\t", "-----------------")
    print("\t", board[3], " | ", board[4], " | ", board[5], " | ")
    print("\t", "-----------------")
    print("\t", board[6], " | ", board[7], " | ", board[8], " | ")


def legalMoves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def humanMove(board, human):
    """Get human move"""
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = askNumber("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied.")
    print("Fine...")
    return move


def askNumber(question, low, high):
    """Ask for a number within range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def win(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (2, 5, 8), (1, 4, 7))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def computerMove(board, computer, human):
    cboard = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    for move in legalMoves(board):
        cboard[move] = computer
        if win(cboard) == computer:
            print(move)
            return move
        cboard[move] = EMPTY

    for move in legalMoves(board):
        cboard[move] = human
        if win(cboard) == human:
            print(move)
            return move
        cboard[move] = EMPTY

    for move in BEST_MOVES:
        if move in legalMoves(board):
            print(move)
            return move

################################################################

# Main game
def main():
    displayIns()
    turn = X
    computer, human = pieces()
    board = newBoard()
    displayBoard(board)
    while not win(board):
        if turn == human:
           move = humanMove(board, human)
           board[move] = human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)
    winner = win(board)
    print(winner)



main()
