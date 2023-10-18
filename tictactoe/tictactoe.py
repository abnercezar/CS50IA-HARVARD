"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = " "


def initial_state():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


# A player função deve receber um tabuleiro estado como entrada e retornar qual é a vez do jogador (ou X ou O).
def player(board):
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X


# A actions função deve retornar uma lista set de todas as ações possíveis que podem ser executadas em um determinado quadro.
def actions(board):
    allpossible_actions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                allpossible_actions.add((row, col))
    return allpossible_actions


# A result função recebe o 'tabuleiro' e a ação como entrada e deve retornar um novo estado da placa, sem modificar a placa original.
def result(board, action):
    if action not in actions(board):
        raise Exception("Ação inválida")
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy


# A winner função deve aceitar o 'tabuleiro' como entrada e retornar o vencedor do 'tabuleiro', se houver.
def winner(board):
    def check_line(line, player):
        return all(cell == player for cell in line)

    for row in board:
        if check_line(row, X):
            return X
        elif check_line(row, O):
            return O

    for col in range(3):
        if check_line([board[row][col] for row in range(3)], X):
            return X
        elif check_line([board[row][col] for row in range(3)], O):
            return O

    if check_line([board[i][i] for i in range(3)], X) or check_line([board[i][i] for i in range(3)], O):
        return X if X == board[1][1] else O

    if check_line([board[i][2 - i] for i in range(3)], X) or check_line([board[i][2 - i] for i in range(3)], O):
        return X if X == board[1][1] else O

    return None


# A terminal função deve aceitar o 'tabuleiro' como entrada e retornar um valor booleano indicando se o jogo acabou.
def terminal(board):
    return winner(board) is not None or all(
        all(cell != EMPTY for cell in row) for row in board
    )


# A utility função deve aceitar um terminal 'tabuleiro' como entrada e saída da utilidade da placa.
def utility(board):
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


# A minimax função deve receber o 'tabuleiro' como entrada e retornar o movimento ideal para o jogador se mover naquele 'tabuleiro'.
def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        value, best_move = float("-inf"), None
        for action in actions(board):
            new_board = result(board, action)
            move_value = min_value(new_board)
            if move_value > value:
                value = move_value
                best_move = action
        return best_move
    else:
        value, best_move = float("inf"), None
        for action in actions(board):
            new_board = result(board, action)
            move_value = max_value(new_board)
            if move_value < value:
                value = move_value
                best_move = action
        return best_move



def max_value(board):
    if terminal(board):
        return utility(board)
    value = float("-inf")
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = float("inf")
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


# Esta função verifica se um jogador ganhou preenchendo uma linha inteira no 'tabuleiro'.
def checkRows(board, player):
    for row in range(len(board)):
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            return True
    return False


# Esta função verifica se um jogador ganhou preenchendo as colunas
def checkColumns(board, player):
    for col in range(len(board)):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True
    return False


# Esta função verifica se um jogador ganhou preenchendo as diagonais do 'tabuleiro'.
# Verifique a diagonal principal
def checkFirstDiag(board, player):
    count = 0
    for row in range(len(board)):
        if board[row][row] == player:
            count += 1
    if count == 3:
        return True
    return False


# Verifique a diagonal secundária
def checkSecDiag(board, player):
    count = 0
    for row in range(len(board)):
        if board[row][2 - row] == player:
            count += 1
    if count == 3:
        return True
    return False
