#!/usr/bin/env python

from copy import deepcopy
import numpy as np

XLIM, YLIM = 3, 2  # board dimensions

# The eight movement directions possible for a chess queen
RAYS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
        and a coordinate system where [0][0] is the top-
        left corner, and x increases to the right while
        y increases going down (this is an arbitrary
        convention choice -- there are many other options
        that are just as good)

    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player two

    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player one is at (0, 0) and player two is at (1, 0)
    """

    def __init__(self):
        # single-underscore prefix on attribute names means
        # that the attribute is "private" (Python doesn't truly
        # support public/private members, so this is only a
        # convention)
        self.board = [[0] * YLIM for _ in range(XLIM)]
        self.board[-1][-1] = 1  # block lower-right corner
        self.parity = 0
        self.player_locations = [None, None]
        print("board layout:")
        print(self.board)

    def opponent(self):
        """Returns the inactive player (the opposite of parity)"""
        return 1 if self.parity == 0 else 0

    def actions(self):
        """Return a list of legal actions for the active player

        You are free to choose any convention to represent actions,
        but one option is to represent actions by the (row, column)
        of the endpoint for the token. For example, if your token is
        in (0, 0), and your opponent is in (1, 0) then the legal
        actions could be encoded as (0, 1) and (0, 2).

        """
        return self.liberties(self.player_locations[self.parity])

    def player(self):
        """Return the id of the active player

        Hint: return 0 for the first player, and 1 for the second player
        """
        return 0 if self.parity == 0 else 1

    def result(self, action):
        """Return a new state that results from applying the given
        action in the current state

        Hint: Check out the deepcopy module--do NOT modify the
        objects internal state in place
        """
        result = deepcopy(self)
        result.board[action[0]][action[1]] = 1
        return result

    def _has_liberties(self, player_id):
        """Return True if the player has any legal moves in the given state"""
        return any(self.liberties(self.player_locations[self.parity]))

    def terminal_test(self):
        """return True if the current state is terminal,
        and False otherwise

        Hint: an Isolation state is terminal if _either_
        player has no remaining liberties (even if the
        player is not active in the current state)
        """
        return any(_has_liberties(player_id) for player_id in [0, 1])

    def liberties(self, loc=None):
        """Return a list of all open cells in the
        neighborhood of the specified location.  The list
        should include all open spaces in a straight line
        along any row, column or diagonal from the current
        position. (Tokens CANNOT move through obstacles
        or blocked squares in queens Isolation.)

        Note: if loc is None, then return all empty cells
        on the board
        """
        liberties = list()
        # If loc is None, then return all empty cells on board
        if loc is None:
            for i in range(0, XLIM):
                for j in range(0, YLIM):
                    if self.board[i][j] == 0:
                        liberties.append((i, j))
            return liberties

        for i in range(0, XLIM):
            for j in range(0, YLIM):
                i_p = int(loc[0])
                j_p = int(loc[1])
                if i == i_p and j == j_p:
                    break
                try:
                    direction = np.abs((i - i_p) / (j - j_p))
                except ZeroDivisionError:
                    direction = -1
                if direction == 0 or direction == 1 or direction == -1:
                    if self.board[i][j] == 0:
                        liberties.append((i, j))

        return liberties


game = GameState()
game.actions()
liberties = game.liberties((0, 1))
print("liberties:")
print(liberties)
