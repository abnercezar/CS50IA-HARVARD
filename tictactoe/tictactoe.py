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
    board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Este código verifica uma condição de vitória para 'X' ou 'O' nas linhas, colunas ou diagonais do
    # 'tabuleiro', retornando o vencedor ou Nenhum se não houver vencedor.
    if checkRows(board, x) or checkColums(board, X) or checkBotton(board, X) or checkBotton(board, X):
        return X
    elif checkRows(board, O) or checkColums(board, O) or checkBotton(board, O) or checkBotton(board, O):
        return O
    else:
        return None
# Esta função verifica se um jogador ganhou preenchendo uma linha inteira
# no 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkRows(board, player):
    for row range(len(board[0])):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == player:
                count += 1
        if count == len(board[0]):
            return True
    return false

# Esta função verifica se um jogador ganhou preenchendo a diagonal do canto superior
# esquerdo ao canto inferior direito do 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkBotton(board, player)
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row == col and board[row][col] == player:
                count += 1
    return count == len(board[0])

# Esta função verifica se todas as células do 'quadro' estão vazias.
# Retorna True se todas as células estiverem vazias, caso contrário, False.
def grav(board):
    countEmpty = (len(board) * len(board[0]))
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                countEmpty += 1
    return countEmpty == 0


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
