"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = " "


def initial_state():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


# A playerfunção deve receber um board estado como entrada e retornar qual é a vez do jogador (ou X ou O).
def player(board):
    countX = sum(row.count("X") for row in board)
    countO = sum(row.count("O") for row in board)

    if countX <= countO:
        return "X"
    else:
        return "O"


# A actionsfunção deve retornar uma lista set de todas as ações possíveis que podem ser executadas em um determinado quadro.


def actions(board):
    possible_actions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


# A result função recebe a board e action como entrada e deve retornar um novo estado da placa, sem modificar a placa original.
def result(board, action):
    if action not in actions(board):
        raise Exception("Ação inválida")
    new_board = [row[:] for row in board]
    row, col = action
    new_board[row][col] = player(board)
    return new_board


# A winner função deve aceitar a board como entrada e retornar o vencedor do tabuleiro, se houver.
def winner(board):
    if checkRows(board, "X") or checkColumns(board, "X") or checkDiagonals(board, "X"):
        return "X"
    elif (
        checkRows(board, "O") or checkColumns(board, "O") or checkDiagonals(board, "O")
    ):
        return "O"
    else:
        return None


# A terminal função deve aceitar a "board" como entrada e retornar um valor booleano indicando se o jogo acabou.
def terminal(board):
    if check_winner(board):
        return True
    if is_board_full(board):
        return True
    return False


# A utilityfunção deve aceitar um terminal boardcomo entrada e saída da utilidade da placa.
def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


# A minimaxfunção deve receber a boardcomo entrada e retornar o movimento ideal para o jogador se mover naquele tabuleiro.
def minimax(board):
    if terminal(board):
        return None

    alpha = float("-infinity")
    beta = float("infinity")
    best_score = float("-infinity")
    best_move = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = player(board)
                if check_win(board, player(board)):
                    return [(i, j)]
                score = minimax_helper(board, False, alpha, beta)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = [(i, j)]
                elif score == best_score:
                    best_move.append((i, j))
    return random.choice(best_move)


possible_moves = None

def best_move(board):
    best_val = -1000
    move_value = -1
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                if(move_val > best_val):
                    best_val = move_val
                    move_value = (i, j)

    return move_value


# Função para implementar o algoritmo Minimax com poda alfa-beta.
# A função recebe o estado atual do tabuleiro, um booleano indicando se o jogador atual está maximizando ou minimizando,
# e os valores alfa e beta, que são usados para a poda alfa-beta.
def minimax_helper(board, is_maximizing, alpha, beta):
    if terminal(board):
        return utility(board)

    # Obtém todos os movimentos possíveis usando a função 'actions'
    possible_moves = actions(board)

    if is_maximizing:
        best_score = float("-infinity")
        possible_moves = get_possible_moves(board)

        for move in possible_moves:
            make_move(board, move)
            score = minimax_helper(board, False, alpha, beta)
            undo_move(board, move)
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float("infinity")
        possible_moves = get_possible_moves(board)
        for move in possible_moves:
            make_move(board, move)
            print
            score = minimax_helper(board, True, alpha, beta)
            undo_move(board, move)
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


# Esta função verifica se um jogador ganhou preenchendo uma linha inteira no 'tabuleiro'.
def checkRows(board, player):
    for row in range(len(board[0])):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False


# Esta função verifica se um jogador ganhou preenchendo as diagonais do 'tabuleiro'.
def checkDiagonals(board, player):
    # Verifique a diagonal principal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    # Verifique a diagonal secundária
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True


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
def is_draw(board):
    countEmpty = len(board) * len(board[0])
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                countEmpty -= 1
    return countEmpty == 0


# Verifique se o tabuleiro está cheio (condição de sorteio)
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


# Função verifique o vencedor
def check_winner(board):
    # Verifique as linhas
    for row in board:
        if all(cell == "X" for cell in row):
            return "X"
        elif all(cell == "O" for cell in row):
            return "O"

    # Verifique as colunas
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return "X"
        elif all(board[row][col] == "O" for row in range(3)):
            return "O"

    # Check diagonals
    if all(board[i][i] == "X" for i in range(3)) or all(
        board[i][2 - i] == "X" for i in range(3)
    ):
        return "X"
    elif all(board[i][i] == "O" for i in range(3)) or all(
        board[i][2 - i] == "O" for i in range(3)
    ):
        return "O"

    return None


# Função para calcular os movimentos possíveis
def get_possible_moves(board):
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible_moves.append((row, col))
    return possible_moves


# Função para realizar uma jogada em um tabuleiro de jogo, receber o estado atual e retornar um novo tabuleiro.
def make_move(board, move):
    current_player = player(board)
    new_board = board.copy()
    new_board[move[0]][move[1]] = current_player
    return new_board


# Função para desfazer uma jogada em um tabuleiro de jogo.
def undo_move(board, move):
    board[move[0]][move[1]] = EMPTY


# Verificar linhas, colunas e diagonais para ver quem venceu
def check_win(board, player):
    for i in range(3):
        # Vitória na linha
        if all(board[i][j] == player for j in range(3)):
            return True

        # Vitória na coluna
        if all(board[j][i] == player for j in range(3)):
            return True

    # Vitória nas diagonais
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True

    return False

# Esta função controla o fluxo do jogo e alterna entre os jogadores
human = "X"


def play_game():
    current_player = X  # Começar com o jogador X
    board = initial_state()
    game_over = False

    while not game_over:
        if current_player == human:
            move = get_human_move()
        else:
            move = minimax(board)

        board = make_move(board, move)
        game_over = check_win(board)

        # Alternar o jogador
        current_player = O if current_player == X else X


def get_human_move():
    while True:
        try:
            row = int(input("Digite o número da linha (0, 1 ou 2): "))
            col = int(input("Digite o número da coluna (0, 1 ou 2): "))

            # Verifique se as coordenadas são válidas
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return (row, col)
            else:
                print("Coordenadas inválidas. Digite novamente.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros para a linha e a coluna.")
