import time
import random

def is_valid_move(board, player, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    if board[row][col] != 0:
        return False

    opponent = -player

    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        found_opponent = False

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            r += dr
            c += dc
            found_opponent = True

        if found_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            return True

    return False

def valid_moves(board, player):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, player, row, col):
                valid_moves.append((row, col))

    return valid_moves

def evaluate_board(board, player):
    opponent = -player
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    x_squares = [(1, 1), (1, 6), (6, 1), (6, 6)]
    c_squares = [(0, 1), (1, 0), (0, 6), (1, 7), (6, 0), (7, 1), (6, 7), (7, 6)]
    
    score = 0
    player_moves = len(valid_moves(board, player))
    opponent_moves = len(valid_moves(board, opponent))

    for row in range(8):
        for col in range(8):
            if board[row][col] == player:
                score += 1
                if (row, col) in corners:
                    score += 100
                elif (row, col) in x_squares:
                    score -= 50
                elif (row, col) in c_squares:
                    score -= 20

            elif board[row][col] == opponent:
                score -= 1
                if (row, col) in corners:
                    score -= 100
                elif (row, col) in x_squares:
                    score += 50
                elif (row, col) in c_squares:
                    score += 20

    # Añadir la movilidad a la evaluación
    score += (player_moves - opponent_moves) * 10

    return score

def make_move(board, player, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    opponent = -player
    board[row][col] = player
    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        tiles_to_flip = []
        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            tiles_to_flip.append((r, c))
            r += dr
            c += dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            for flip_r, flip_c in tiles_to_flip:
                board[flip_r][flip_c] = player

def minimax(board, player, depth, alpha, beta, maximizing):
    if depth == 0 or not valid_moves(board, player):
        return evaluate_board(board, player)

    if maximizing:
        max_eval = float('-inf')
        for move in valid_moves(board, player):
            row, col = move
            new_board = [row[:] for row in board]
            make_move(new_board, player, row, col)
            eval = minimax(new_board, -player, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in valid_moves(board, player):
            row, col = move
            new_board = [row[:] for row in board]
            make_move(new_board, player, row, col)
            eval = minimax(new_board, -player, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def AI_MOVE(board, player):
    start_time = time.time()
    _valid_moves = valid_moves(board, player)
    if not _valid_moves:
        return None

    best_moves = []
    best_score = float('-inf')
    depth = 3  # Profundidad inicial

    # Ajustar la profundidad basada en el estado del juego
    total_pieces = sum(row.count(1) + row.count(-1) for row in board)
    if total_pieces > 44:  # Fase final del juego
        depth = 5
        deterministic = True
    else:
        deterministic = False

    if total_pieces < 12:  # Apertura del juego
        depth = 2

    for move in _valid_moves:
        row, col = move
        new_board = [row[:] for row in board]
        make_move(new_board, player, row, col)
        move_score = minimax(new_board, -player, depth, float('-inf'), float('inf'), False)
        
        if move_score > best_score:
            best_score = move_score
            best_moves = [move]  # Reiniciar la lista de mejores movimientos
        elif move_score == best_score:
            best_moves.append(move)  # Agregar el movimiento a la lista de mejores movimientos

    end_time = time.time()
    print(f"Tiempo de ejecucion {end_time - start_time}")

    # Seleccionar determinísticamente en la fase final
    if deterministic:
        return best_moves[0]  # Selecciona el primer mejor movimiento
    else:
        return random.choice(best_moves)  # Seleccionar aleatoriamente entre los mejores movimientos


