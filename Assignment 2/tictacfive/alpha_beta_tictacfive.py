import math

def alphabeta_max(current_game):
    alpha = float('-inf')
    beta = float('inf')
    return maximin(current_game, alpha, beta)

def alphabeta_min(current_game):
    alpha = float('-inf')
    beta = float('inf')
    return minimax(current_game, alpha, beta)

def maximin(current_game, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        mx, _ = minimax(move, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
        if v >= beta:
            break  # Beta cutoff
        alpha = max(alpha, v)
    return v, best_move

def minimax(current_game, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        mn, _ = maximin(move, alpha, beta)
        if v > mn:
            v = mn
            best_move = move
        if v <= alpha:
            break  # Alpha cutoff
        beta = min(beta, v)
    return v, best_move