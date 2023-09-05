"""
Tic Tac Toe Player
"""

import math

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
    # Este código conta as ocorrências de 'X' e 'O' em um 'quadro' de lista 2D,
    # retornando 'X' se as contagens forem iguais, caso contrário, 'O'.

    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1

    return X if countX == countO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(len(board[0])):
        if board[row][col] == EMPTY:
            posssible_moves.add((row, col))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action
    #print(action)
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise IndexError()


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
