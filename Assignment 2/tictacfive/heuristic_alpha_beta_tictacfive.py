import math
def alphabeta_max_h(current_game, h, max_depth):
    """
    Alpha-beta pruning for the maximizing player with heuristic support.

    :param current_game: The current game state
    :param h: The heuristic function (not used directly, kept for consistency)
    :param max_depth: Maximum depth to search
    :return: Best score and corresponding move
    """
    alpha = float('-inf')
    beta = float('inf')
    return maximin(current_game, alpha, beta, max_depth, h)


def alphabeta_min_h(current_game, h, max_depth):
    """
    Alpha-beta pruning for the minimizing player with heuristic support.

    :param current_game: The current game state
    :param h: The heuristic function (not used directly, kept for consistency)
    :param max_depth: Maximum depth to search
    :return: Best score and corresponding move
    """
    alpha = float('-inf')
    beta = float('inf')
    return minimax(current_game, alpha, beta, max_depth, h)


def maximin(current_game, alpha, beta, depth, h):
    """
    Maximizing player's turn in alpha-beta pruning.

    :param current_game: The current game state
    :param alpha: The current alpha value
    :param beta: The current beta value
    :param depth: The remaining depth to search
    :param h: The heuristic function to evaluate non-terminal states
    :return: Best score and corresponding move
    """
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None  # Use heuristic evaluation here

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        mx, _ = minimax(move, alpha, beta, depth - 1, h)
        if v < mx:
            v = mx
            best_move = move
        if v >= beta:
            break  # Beta cutoff
        alpha = max(alpha, v)
    return v, best_move


def minimax(current_game, alpha, beta, depth, h):
    """
    Minimizing player's turn in alpha-beta pruning.

    :param current_game: The current game state
    :param alpha: The current alpha value
    :param beta: The current beta value
    :param depth: The remaining depth to search
    :param h: The heuristic function to evaluate non-terminal states
    :return: Best score and corresponding move
    """
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None  # Use heuristic evaluation here

    v = math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        mn, _ = maximin(move, alpha, beta, depth - 1, h)
        if v > mn:
            v = mn
            best_move = move
        if v <= alpha:
            break  # Alpha cutoff
        beta = min(beta, v)
    return v, best_move