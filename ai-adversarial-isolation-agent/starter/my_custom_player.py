from sample_players import DataPlayer
import time


class CustomPlayer(DataPlayer):
    """Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.d

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

        depth_limit = 5
        if state.ply_count < 2:
            # Randomly select a move as player 1 or 2 on an empty board
            self.queue.put(random.choice(state.actions()))
        else:
            # Return the optimal minimax move.
            #
            # Use a for loop for iterative deepening. Iterative deepening is a search
            # technique that allows minimax-style search functions to return an
            # approximate solution when computational resources are bounded. The basic
            # idea is to start with a small depth-limited search, and grow the depth
            # limit until the resource limit (usually search time) expires.
            for depth in range(1, depth_limit+1):
                self.queue.put(self.alpha_beta_search(state, depth))

    def alpha_beta_search(self, state, depth):
        """Return the move along a branch of the game tree that
        has the best possible value.  A move is a pair of coordinates
        in (column, row) order corresponding to a legal move for
        the searching player.

        You can ignore the special case of calling this function
        from a terminal state.
        """
        
        def min_value(state, alpha, beta, depth):
            """Return the minimum value over all legal child nodes.
            """
            if state.terminal_test():
                return state.utility(self.player_id)

            if depth <= 0:
                return self.score(state)

            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), alpha, beta, depth - 1))
                # if value <= alpha:
                #     return value
                beta = min(beta, value)
            return value

        def max_value(state, alpha, beta, depth):
            """Return the maximum value over all legal child nodes.
            """
            if state.terminal_test():
                return state.utility(self.player_id)

            if depth <= 0:
                return self.score(state)

            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), alpha, beta, depth - 1))
                # if value >= beta:
                #     return value
                alpha = max(alpha, value)
            return value

        alpha = float("-inf")
        beta = float("inf")
        best_score = float("-inf")
        best_move = None
        for action in state.actions():
            value = min_value(state.result(action), alpha, beta, depth - 1)
            alpha = max(alpha, value)
            if float(value) >= best_score:
                best_score = value
                best_move = action
        return best_move

    def score(self, state):
        """Return the heuristic value of a game state
        """
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_lib = state.liberties(own_loc)
        opp_lib = state.liberties(opp_loc)
        own_moves = len(own_lib)
        opp_moves = len(opp_lib)

        # Define heuristics
        # -----------------
        # 1 = Standard (own_moves - opp_moves) strategy
        # 2 = Offensive strategy
        # 3 = Defensive strategy
        # 4 = Dynamic offensive to defensive strategy
        heuristic = 4

        if heuristic == 1:
            # This is the standard baseline heuristic, which is the difference
            # between the number of moves available to the player and the number
            # of moves available to the opponent
            return own_moves - opp_moves

        elif heuristic == 2:
            # This offensive heuristic puts more weight on increasing its own
            # liberties than on limiting the opponent's liberties
            m = 0.25
        elif heuristic == 3:
            # This defensive heuristic puts more weight on limiting the
            # opponent's liberties than on increasing its own liberties
            m = 0.75
        elif heuristic == 4:
            # This dynamic heuristic gives a sense of time in the game by taking
            # the ratio of the number of moves played to the total number of
            # moves available on the board. This ratio is used to apply a smooth
            # transition from an offensive to a defensive strategy throughout
            # the game
            m = state.ply_count / state.board_size()
        else:
            raise ValueError("Invalid heuristic")

        return m * own_moves - (1 - m) * opp_moves

    def minimax(self, state, depth):

        def min_value(state, depth):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.minimax_score(state)
            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), depth - 1))
            return value

        def max_value(state, depth):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.minimax_score(state)
            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), depth - 1))
            return value

        return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1))

    def minimax_score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)
