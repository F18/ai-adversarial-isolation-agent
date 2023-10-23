---
 title: "Notes: Adversarial Search and Game Play"
 author: Ramy Rashad
 numbersections: true
 geometry: margin=1.00in

---

# Adversarial Search

Adversarial search is a type of search algorithm used in game theory to find the
optimal move for a player in a game where the outcome depends on the moves of
multiple players. In adversarial search, the algorithm considers the possible
moves of both players and tries to find the best move for the current player
while assuming that the opponent will make the best possible move for
themselves.

Adversarial search algorithms are commonly used in games such as chess,
checkers, and Go, where the outcome of the game depends on the moves of both
players. These algorithms use heuristics to evaluate the utility of a game state
and search through the game tree to find the optimal move.

## Main Topics

1. Advesarial Search
2. Minimax Algorithm
3. Alpha-Beta Pruning
4. Evaluation Functions
5. Isolation Game Player
6. Multiplayer, Probabilstic Games

## Lesson Outline

- The MINMAX algorithm
- Isolation
- MIN and MAX levels
- Propagating values up the tree
- Computing MIN MAX values
- Choosing the best branch
- Max number of nodes
- The branching factor

## The MINIMAX Algorithm

The minimax algorithm is a recursive algorithm. It explores the game tree by
recursively evaluating the utility values of different game states.

The algorithm starts at the root node and considers all possible moves that the
active player can make. For each possible move, it recursively calls itself to
evaluate the utility values of the resulting game states. This process continues
until it reaches a terminal state, where the game is over and a utility value
can be assigned.

During the recursive process, the algorithm alternates between the "Max" and
"Min" players, maximizing and minimizing the utility values, respectively. The
algorithm assumes that both players will make optimal moves to maximize or
minimize the utility value, depending on their role.

By evaluating the utility values of different game states and propagating them
up the tree, the minimax algorithm determines the best move for the active
player at the root node.

## Pseudo code

The psuedo code for minimax is shown in Figure \ref{fig:minimax}:

![MINIMAX Pseudo code \label{fig:minimax}](./figs/minimax.png)

## A Python Implementation

Note that this is a recursive algorithm. The `minimax_decision` function calls
the `min_value` and `max_value` functions, which in turn call each other. Also
note in the min_value and max_value functions, the `gameState.result(a)` is
passed as an argument to the `min_value` and `max_value` functions. This is how
the algorithm traverses the game tree.

In the `minimax_decision` function we are checking all possible moves/actions
and returning the one with the highest value. This is the move that the active
player should make. Note that you pass the result of the action,
`gameState.result(a)`, to the `min_value` function to get the value of each
move. Here we are just using a mapping function (using the lambda function) to
get the value of each move.


        def minimax_decision(gameState):
            """ Return the move along a branch of the game tree that
            has the best possible value.  A move is a pair of coordinates
            in (column, row) order corresponding to a legal move for
            the searching player.
            
            You can ignore the special case of calling this function
            from a terminal state.
            """
            # The built in `max()` function can be used as argmax!
            return max(gameState.actions(),
                       key=lambda m: min_value(gameState.result(m)))

        def min_value(gameState):
            """ Return the game state utility if the game is over,
            otherwise return the minimum value over all legal successors
            """
            if gameState.terminal_test():
                return gameState.utility(0)
            v = float("inf")
            for a in gameState.actions():
                v = min(v, max_value(gameState.result(a)))
            return v
    
    
        def max_value(gameState):
            """ Return the game state utility if the game is over,
            otherwise return the maximum value over all legal successors
            """
            if gameState.terminal_test():
                return gameState.utility(0)
            v = float("-inf")
            for a in gameState.actions():
                v = max(v, min_value(gameState.result(a)))
            return v

## Isolation (5x5)

Watch this video link: [https://www.youtube.com/watch?v=n_ExdXeLNTk](https://www.youtube.com/watch?v=n_ExdXeLNTk)

We need to create a `GameState` class with the ability to:

1. keep track of which cells are open and closed
2. identify which player has initiative (whose turn it is to move)
3. track the current position of each player on the board

## Propagating Values Up the Tree

The minimax algorithm propagates the utility values up the tree by alternating between the "Max" and "Min" players. The algorithm assumes that both players will make optimal moves to maximize or minimize the utility value, depending on their role.

The Figure \ref{fig:propagate} shows the propagation of values up the tree:

![Propagating Values Up the Tree \label{fig:propagate}](./figs/minimax-propagate.png)

Notes:

- an "Up" arrow indicates a MAX node
- a "Down" arrow indicates a MIN node
- To begin with, boxes E, F, G, H, I, and J have just one child. As such, they
  simply take the value of their child.
- Box C is a minimizer node, and hence chooses the minimum of boxes F, and G
  which is G's value of -1.
- Box A is a maximizing node, and chooses the maximum of boxes B, C, and D which
  is D's value of +1.

## Number of nodes

The number of nodes that need to be explored is exponential with depth of the
tree. The average branching factor is the number of children each node has on
average over the course of the game. In other words, it represents have many
possible moves there are at each turn.

The number of nodes that need to be explored is the branching factor raised to
the power of the depth of the tree. If $b$ is the average branching factor and
$d$ is the depth of the tree, then the number of nodes that need to be explored
is $b^d$.

For a `5x5` Queens isolation game you have an average branching factor of around
8 and a depth of 25. This means that the number of nodes that need to be
explored is $8^{25}$ which is around $10^{22}$. Given a processor that could
compute $10^{9}$ calculations per second, we would need to wait around 1.2
million years to get our answer.

\newpage
\center{--- The End ---}