from sample_players import DataPlayer


class CustomPlayer(DataPlayer):
    """Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """

    def get_action(self, state):
        """Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE:
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """

        import random

        if state.ply_count < 2:
            # randomly select a move as player 1 or 2 on an empty board
            self.queue.put(random.choice(state.actions()))
        else:
            # return the optimal minimax move at a fixed search depth
            self.queue.put(self.alpha_beta_search(state, depth=5))

    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_lib = len(state.liberties(own_loc))
        opp_lib = len(state.liberties(opp_loc))

        # Define heuristics
        # -----------------
        # 1 = Offensive strategy
        # 2 = Defensive strategy
        # 3 = Dynamic offensive to defensive strategy
        heuristic = 3

        if heuristic == 1:
            # This offensive heuristic puts more weight on increasing its own
            # liberties than on limiting the opponent's liberties
            m = 0.25
        elif heuristic == 2:
            # This defensive heuristic puts more weight on limiting the
            # opponent's liberties than on increasing its own liberties
            m = 0.75
        elif heuristic == 3:
            # This dynamic heuristic gives a sense of time in the game by taking
            # the ratio of the number of moves played to the total number of
            # moves available on the board. This ratio is used to apply a smooth
            # transition from an offensive to a defensive strategy throughout
            # the game
            m = state.ply_count / state.board_size()
        else:
            raise ValueError("Invalid heuristic")

        return m * own_lib - (1 - m) * opp_lib

    def alpha_beta_search(self, state, depth):
        """Return the move along a branch of the game tree that
        has the best possible value.  A move is a pair of coordinates
        in (column, row) order corresponding to a legal move for
        the searching player.

        You can ignore the special case of calling this function
        from a terminal state.
        """
        alpha = float("-inf")
        beta = float("inf")
        best_score = float("-inf")
        best_move = None
        for a in state.actions():
            v = self.min_value(state.result(a), alpha, beta, depth - 1)
            alpha = max(alpha, v)
            if v > best_score:
                best_score = v
                best_move = a
        return best_move

    def min_value(self, state, alpha, beta, depth):
        """Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        if state.terminal_test():
            return state.utility(self.player_id)

        if depth <= 0:
            return self.score(state)

        v = float("inf")
        for a in state.actions():
            v = min(v, self.max_value(state.result(a), alpha, beta, depth - 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value(self, state, alpha, beta, depth):
        """Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        if state.terminal_test():
            return state.utility(self.player_id)

        if depth <= 0:
            return self.score(state)

        v = float("-inf")
        for a in state.actions():
            v = max(v, self.min_value(state.result(a), alpha, beta, depth - 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
