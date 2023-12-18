"""
Tic Tac Toe Player
"""
import math
from copy import deepcopy

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

    x = 0
    o = 0

    for row in board:
        x += row.count(X)
        o += row.count(O)

    if x <= o:
        return X
    else:
        return O





def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    a = set()

    for init, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                a.add((init, column_index))
    return a





def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    a = player(board)

    b = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        b[i][j] = a
    return b





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for player in (X, O):
            for row in board:
                if row == [player] * 3:
                    return player

            for y in range(3):
                column = [board[x][y] for x in range(3)]
                if column == [player] * 3:
                    return player

            if [board[y][y] for y in range(0, 3)] == [player] * 3:
                return player

            elif [board[y][~y] for y in range(0, 3)] == [player] * 3:
                return player
    return None





def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    a = winner(board)

    if a == X:
        return 1
    elif a == O:
        return -1
    else:
        return 0





def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxi(board):
        am = ()
        if terminal(board):
            return utility(board), am
        else:
            f = -5
            for action in actions(board):
                b = mini(result(board, action))[0]
                if b > f:
                    f = b
                    am = action
            return f, am



    def mini(board):
        am = ()
        if terminal(board):
            return utility(board), am
        else:
            f = 5
            for action in actions(board):
                b = maxi(result(board, action))[0]
                if b < f:
                    f = b
                    am = action
            return f, am



    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return maxi(board)[1]

    else:
        return mini(board)[1]