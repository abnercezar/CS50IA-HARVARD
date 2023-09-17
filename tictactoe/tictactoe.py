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
    # A função player deve receber uma entrada e
    # retorna de quem é a vez do jogador X ou O

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
    new_board = [row[:] for row in board]
    row, col = action
    new_board[row][col] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Este código verifica uma condição de vitória para 'X' ou 'O' nas linhas, colunas ou diagonais do
    # 'tabuleiro', retornando o vencedor ou Nenhum se não houver vencedor.
    if checkRows(board, 'X') or checkColumns(board, 'X') or checkDiagonals(board, 'X'):
        return 'X'
    elif checkRows(board, 'O') or checkColumns(board, 'O') or checkDiagonals(board, 'O'):
        return 'O'
    else:
        return None

# Esta função verifica se um jogador ganhou preenchendo uma linha inteira
# no 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkRows(board, player):
    for row in range(len(board[0])):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False

# Esta função verifica se um jogador ganhou preenchendo a diagonal do canto superior
# esquerdo ao canto inferior direito do 'tabuleiro'. Ele retorna True se for o caso, caso contrário, False.
def checkDiagonals(board, player):
    count1 = 0
    count2 = 0
    for i in range(len(board)):
        if board[i][i] == player:
            count1 += 1
        if board[i][len(board) - 1 - i] == player:
            count2 += 1
    return count1 == len(board) or count2 == len(board)

# Esta função verifica se um jogador ganhou preenchendo as colunas
def checkColumns(board, player):
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board[0])):
            if board[row][col] == player:
                count += 1
        if count == len(board):
            return True
    return False

# Esta função verifica se todas as células do 'quadro' estão vazias.
# Retorna True se todas as células estiverem vazias, caso contrário, False.
def grav(board):
    countEmpty = len(board) * len(board[0])
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                countEmpty -= 1
    return countEmpty == 0

# A função terminal deve aceitar a board como entrada e retornar
# um valor booleano indicando se o jogo acabou.
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) or grav(board)

# A função utility deve aceitar um terminal placa
# como entrada e saída da utilidade da placa.
# Ela retorna 1 se o jogador X ganhou o jogo, -1 se o jogador
# O ganhou o jogo ou 0 caso contrário.
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
    if terminal(board):
        return None
    best_score = float('-infinity')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = player(board)
                score = minimax_helper(board_copy, False)
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def minimax_helper(board, is_maximizing):
    if terminal(board):
        return utility(board)

    if is_maximizing:
        possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        best_score = float('-inf')
        new_board_after_move = make_move(board, move)
        for move in possible_moves(board):
            score = minimax_helper(new_board_after_move, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = ('inf')
        for move in possible_moves(board):
            new_board_after_move = make_move(board, move)
            score = minimax_helper(new_board_after_move, True)
            best_score = min(score, best_score)
        return best_score

def make_move(board, move):
    current_player = "X"
    new_board = board.copy()
    new_board[move] = current_player
    return new_board