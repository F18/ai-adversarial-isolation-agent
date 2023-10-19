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

Pseudo code is shown in Figure \ref{fig:minimax}:

![MINIMAX Pseudo code \label{fig:minimax}](./figs/minimax.png)

## Isolation (5x5)

Watch this video link: [https://www.youtube.com/watch?v=n_ExdXeLNTk](https://www.youtube.com/watch?v=n_ExdXeLNTk)

We need to create a `GameState` calss with the ability to:

1. keep track of which cells are open and closed
2. identify which player has initiative (whose turn it is to move)
3. track the current position each player on the board



\newpage
\center{--- The End ---}