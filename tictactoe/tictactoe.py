"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = ''


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

    # Verifique a diagonal principal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    # Verifique a diagonal secundária
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # Verifique linhas diagonais adicionais
    if board[0][1] == player and board[1][2] == player and board[2][0] == player:
        return True
    
    if board[0][0] == player and board[1][2] == player and board[2][1] == player:
        return True
    
    # Adicione mais verificações diagonais, se necessário
    return False
    
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
def is_draw(board):
    countEmpty = len(board) * len(board[0])
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                countEmpty -= 1
    return countEmpty == 0



# Função minimax recursiva chamando a si mesma para prever movimentos futuros
def minimax(board):
    
    if terminal(board):
        return best_move
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

possible_moves = None

# A função terminal deve aceitar a board como entrada e retornar
# um valor booleano indicando se o jogo acabou.
def terminal(board):

    # Verifique se o jogo acabou (vitória, empate ou em andamento)
    winner = check_winner(board)
    if winner is not None:
        return winner
    elif is_board_full(board):
        return 'Empate'
    else:
        return False

def check_win(board, player):
    # Verificar linhas
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Verificar colunas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Verificar diagonais
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def ai_move(board):
    IA = X
    PLAYER = O

# Verifique se há ameaças
    threat = check_threat(board, PLAYER)
    if threat is not None:
        return threat
    
    # Verifique se o tabuleiro está vazio e caso sim jogue no centro
    if board[1][1] == EMPTY:
        return (1, 1)
    
    # Crie uma lista de campos vazios para jogar nos cantos
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in corners:
        if board[corner[0]][corner[1]] == EMPTY:
            return corner
        
    # Verificar se a IA pode ganhar a próxima jogada
    move = check_threat(board, IA)
    if move is not None:
        return move
        
    # Verifica se o jogador pode ganhar a próxima jogada
    move = check_threat(board, PLAYER)
    if move is not None:
        return move
    
    # Se ninguém está prestes a ganhar, faça uma jogada aleatória
    empty_positions = [(i, j) for i in range(3) 
                       for j in range(3) 
                       if board[i][j] == EMPTY]
    
    # Escolhe uma posição vazia aleatória
    return random.choice(empty_positions)

def is_board_full(board):
    # Verifique se o tabuleiro está cheio (condição de sorteio)
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def is_board_empty(board):
    # Verifique se o tabuleiro está vazio
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Verifique as linhas
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    #Verifique as colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col] 
          
    # Verifique a diagonal primária
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    # Verifique a diagonal secundária
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]



# Verifica se há duas jogadas do jogador em uma posição vazia
def check_threat(board, player):
    # Verifica as linhas
    for i, row in enumerate(board):
        if row.count(player) == 2 and row.count(EMPTY) == 1:
            return (i, row.index(EMPTY))
        
    # Verifica as colunas
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(player) == 2 and col.count(EMPTY) == 1:
            return (col.index(EMPTY), j)
        
    # Verifica a diagonal primária
    if (board[0][0] == player and board[1][1] == player and board[2][2] == EMPTY):
        return (2, 2)
    elif (board[0][0] == player and board[2][2] == player and board[1][1] == EMPTY):
        return (1, 1)
    elif (board[1][1] == player and board[2][2] == player and board[0][0] == EMPTY):
        return (0, 0)
    
    # Verifica a diagonal secundária
    if (board[0][2] == player and board[1][1] == player and board[2][0] == EMPTY):
        return (2, 0)
    elif (board[0][2] == player and board[2][0] == player and board[1][1] == EMPTY):
        return (1, 1)
    elif (board[1][1] == player and board[2][0] == player and board[0][2] == EMPTY):
        return (0, 2)
    
    # Retorna None se não houver ameaças
    return None  
        
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


def minimax_helper(board, is_maximizing):
    if terminal(board):
        return utility(board)

    if is_maximizing:
        best_score = float('-infinity')
        possible_moves = get_possible_moves(board)
        for move in possible_moves:
            board_copy = make_move(board, move)
            score = minimax_helper(board_copy, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('infinity')
        possible_moves = get_possible_moves(board)
        for move in possible_moves:
            board_copy = make_move(board, move)
            score = minimax_helper(board_copy, not is_maximizing)
            best_score = min(score, best_score)
        return best_score
    
def get_possible_moves(board):
    # Código para calcular os movimentos possíveis
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible_moves.append((row, col))
    return possible_moves

def make_move(board, move):
    current_player = player(board)
    new_board = board.copy()
    new_board[move[0]][move[1]] = current_player
    return new_board