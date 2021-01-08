# -----------------------------------------------------------
# * A basic Tic Tac Toe game written in Python with no external modules
# ? Next step: Implement AI for a better computer plays
# TODO: Finalize documentation of functions, improve readability.
from random import randrange

# Board numbers initialization
#//global digitos
digitos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # ? The list used to store the user and machine inputs, is edited as global variable inside functions.
victoria = 0

print("\n\nWelcome to the Tic, Tac, Toe Game by Techno, enjoy and may the best player win!!!\n\n")

def DisplayBoard(board):
    """[summary]

    the function accepts one parameter containing the board's current status
    and prints it out to the console

    Arguments:
        board {[list]} -- [expected global variable digitos as input]

    Returns:
        [None] -- [None]
    """

    print("+-------" * 3, end = "+\n")
    print("|       " * 3, end = "|\n")
    print("|   {}   |   {}   |   {}   ".format(board[0][0], board[0][1], board[0][2]), end = "|\n")
    print("|       " * 3, end = "|\n")
    print("+-------" * 3, end = "+\n")
    print("|       " * 3, end = "|\n")
    print("|   {}   |   {}   |   {}   ".format(board[1][0], board[1][1], board[1][2]), end = "|\n")
    print("|       " * 3, end = "|\n")
    print("+-------" * 3, end = "+\n")
    print("|       " * 3, end = "|\n")
    print("|   {}   |   {}   |   {}   ".format(board[2][0], board[2][1], board[2][2]), end = "|\n")
    print("|       " * 3, end = "|\n")
    print("+-------" * 3, end = "+\n")
    return None


def EnterMove(board):
    """[summary]
    
    the function accepts the board current status, asks the user about their move,
    checks the input and updates the board according to the user's decision
    
    Arguments:
        board {[list]} -- [expected global variable digitos as input]
    
    Returns:
        [None] -- [None]
    """
    global digitos
    move = int(input("Your turn!, Select your play (1 - 9): "))
    legal_moves = MakeListOfFreeFields(digitos)
    for i in range(len(board)):
        for j in range(len(board)):
            if (digitos[i][j] == move and ((i,j) in legal_moves)):
                digitos[i][j] = "o"
                legal_moves = MakeListOfFreeFields(digitos)
            else:
                continue
    DisplayBoard(digitos)
    return None

def MakeListOfFreeFields(board):
    """[summary]
    
    the function browses the board and builds a list of all the free squares;
    the list consists of tuples, while each tuple is a pair of row and column numbers
    
    Arguments:
        board {[list]} -- [expected global variable digitos as input]
    
    Returns:
        [list] -- [lista_tup is a list of tuple pairs representing the free positions in the board]
    """
    lista_tup = []
    for i in range(len(board)):
        for j in range(len(board)):
            if (digitos[i][j] != "x" and digitos[i][j] != "o"):
                lista_tup.append((i,j))
            else:
                continue
    return lista_tup

def VictoryFor(board, sign):
    """[summary]
    
    the function analyzes the board status in order to check if
    the player using 'O's or 'X's has won the game
    
    Arguments:
        board {[list]} -- [expected global variable digitos as input]
        sign {[str]} -- [expected sinbol used to play "x" for computer or "o" for the user]
    
    Returns:
        [int] -- [victoria is an int variable that stores 0 if no one has won, or 1 is there is a winner, used to exit the while loop]
    """
    
    print("\nHas anyone won?: ", end="")
    global digitos
    global victoria
    legal_moves = MakeListOfFreeFields(digitos)
    for i in range(len(board)):
        if ((digitos[i][0] == sign and digitos[i][1] == sign and digitos[i][2] == sign) or\
            (digitos[0][i] == sign and digitos[1][i] == sign and digitos[2][i] == sign) or\
            (digitos[0][0] == sign and digitos[1][1] == sign and digitos[2][2] == sign) or\
            (digitos[0][2] == sign and digitos[1][1] == sign and digitos[2][0] == sign)):
            print("Yes!")
            print("\nThe {} has won!!\n".format(sign))
            victoria = 1
            return victoria
    if len(legal_moves) == 0 and victoria == 0:
            print("No!\n")
            print("\nGame Over is a Tie!!\n")
            victoria = -1
            return victoria
    elif len(legal_moves) != 0 and victoria == 0:
            print("No!\n")
            return victoria

def DrawMove(board):
    """[summary]
    
    the function draws the computer's move and updates the board
    
    Arguments:
        board {[list]} -- [expected global variable digitos as input]
    
    Returns:
        [None] -- [None]
    """
    
    global digitos
    legal_moves = MakeListOfFreeFields(digitos)
    counter = 0
    while counter == 0:
        comp_move = randrange(1,10,1)
        for i in range(len(board)):
            for j in range(len(board)):
                if (digitos[i][j] == comp_move and ((i,j) in legal_moves)):
                    digitos[i][j] = "x"
                    legal_moves = MakeListOfFreeFields(digitos)
                    print("My turn!, I shall play like so!: {}".format(comp_move))
                    DisplayBoard(digitos)
                    counter = 1
                else:
                    continue
    return None

# ? Testing code
#//digitos = [["x", "o", "o"],["x", "x", "o"],["o", "o", "x"]] # x win
#//digitos = [["x", "o", "x"], ["x", "o", "o"],["o", "x", "x"]] # Tie
#//digitos = [["x", "o", "x"],["x", "o", "o"],["o", "o", "x"]] # o win
#//digitos = [["x", "o", "x"],["x", "x", "o"],["o", "o", "9"]] # Continue
rondas = 0 # To visualize number rounds of the game.
while  victoria == 0:
    rondas += 1
    print("------------------------------------ Ronda: {}".format(rondas))
    DrawMove(digitos)
    victoria = VictoryFor(digitos,"x")
    if victoria != 0:
        break
    EnterMove(digitos)
    victoria = VictoryFor(digitos,"o")