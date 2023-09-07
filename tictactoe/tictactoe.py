"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Este código conta o número de 'X' e 'O' em uma lista 2D chamada
    # 'tabuleiro'. Se houver mais 'X' do que 'O', retorna 'O', caso contrário,
    # retorna 'X'.

    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Este código gera um conjunto de movimentos possíveis
    # verificando espaços vazios em cada linha do ‘tabuleiro’.
    possible_actions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Este código valida uma ação, então cria uma cópia do 'tabuleiro',
    # aplica a 'ação' para o 'jogador' atual e retorna o tabuleiro atualizado.
    if action not in actions(board):
        raise Exception("Not valid action")
    row, col = action
    board_copy = copy.deepcoy(board)
    board_copy[row][col] = player(board)
    return board_copy



# Esta função verifica se um jogador ganhou preenchendo uma linha inteira
# no 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkRows(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


# Esta função verifica se um jogador ganhou preenchendo a diagonal do canto superior
# esquerdo ao canto inferior direito do 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkCol(board, player)
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        return False

# Esta função verifica se todas as células do 'quadro' estão vazias.
# Retorna True se todas as células estiverem vazias, caso contrário, False.
def checkPrim(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def checkSeg(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or grav(board):
        return True
    else:
        return false


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
