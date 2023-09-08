"""
Tic Tac Toe Player
"""

import copy
import math
import pdb

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


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
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            return True
    return False


# Esta função verifica se um jogador ganhou preenchendo a diagonal do canto superior
# esquerdo ao canto inferior direito do 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkCols(board, player):
    for col in range(len(board)):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True
    return False


# Esta função verifica uma condição de vitória no jogo,
# verificando se um jogador tem três de suas marcas em uma linha diagonal
# do canto superior esquerdo ao canto inferior direito do tabuleiro do jogo.
# Se o fizerem, a função retornará True, indicando uma vitória para aquele jogador.
# Caso contrário, retorna False.
def checkPrimary(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

# Esta função verifica uma condição de vitória no jogo.
# Verifica se um jogador tem três de suas marcas em uma linha diagonal
# do canto inferior esquerdo ao canto superior direito do tabuleiro do jogo.
# Se o fizerem, a função retornará True, indicando uma vitória para aquele jogador.
# Caso contrário, retorna False.
def checkSecond(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

# Esta função verifica se há um vencedor em um jogo.
# Verifica linhas, colunas e ambas as diagonais de cada jogador (X e O).
# Se encontrar um vencedor, devolve a marca do jogador vencedor.
# Se não houver vencedor, ele retornará vazio.
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (
        checkRows(board, X)
        or checkCols(board, X)
        or checkPrimary(board, X)
        or checkSecond(board, X)
    ):
        return X
    elif (
        checkRows(board, X)
        or checkCols(board, X)
        or checkPrimary(board, X)
        or checkSecond(board, X)
    ):
        return O
    else:
        return None

# Esta função verifica se o jogo acabou.
# Isso é feito verificando se há um vencedor ou se todas as células do tabuleiro estão preenchidas.
# Se houver um vencedor ou nenhuma célula vazia, retornará True,
# indicando que o jogo acabou. Se ainda houver células vazias e nenhum vencedor,
# retornará False, indicando que o jogo não acabou.
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board[row])):
        if board[row][col] == EMPTY:
            return False
        return True

# Esta função é usada para avaliar o estado do tabuleiro de jogo.
# Se o jogador X ganhou, retorna 1. Se o jogador O ganhou, retorna -1.
# Se não houver vencedor, ele retornará 0. Isso normalmente é usado em algoritmos
# de jogos para determinar o valor de um estado específico do jogo.
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

# Esta função max_value(board) calcula o valor máximo possível para o
# jogador atual em um algoritmo Minimax para um jogo de tabuleiro.
def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        return v


# Esta função min_value(board) calcula o valor mínimo possível para o
# jogador adversário em um algoritmo Minimax para um jogo de tabuleiro.
def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        return v

# Esta função minimax(board) retorna a ação ótima para o jogador atual no tabuleiro,
# usando o algoritmo Minimax.
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    plays = [] # inicializa a lista de jogadas
    if terminal(board):
        return None

    elif player(board) == X:
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]

