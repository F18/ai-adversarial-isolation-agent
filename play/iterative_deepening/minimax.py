
# DO NOT MODIFY THE PLAYER ID
player_id = 0

def my_moves(gameState):
    loc = gameState._player_locations[player_id]
    return len(gameState.liberties(loc))


def minimax_decision(gameState, depth):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    best_score = float("-inf")
    best_move = None
    for a in gameState.actions():
        # call has been updated with a depth limit
        v = min_value(gameState.result(a), depth - 1)
        if v > best_score:
            best_score = v
            best_move = a
    return best_move


def min_value(gameState, depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    
    if depth <= 0:
        return my_moves(gameState)
    
    v = float("inf")
    for a in gameState.actions():
        # the depth should be decremented by 1 on each call
        v = min(v, max_value(gameState.result(a), depth - 1))
    return v


def max_value(gameState, depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    
    if depth <= 0:
        return my_moves(gameState)
    
    v = float("-inf")
    for a in gameState.actions():
        # the depth should be decremented by 1 on each call
        v = max(v, min_value(gameState.result(a), depth - 1))
    return v

