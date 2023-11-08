---
 title: "Project Report: Adversarial Search Agent"
 author: Ramy Rashad
 numbersections: true
 geometry: margin=0.75in
---

In this project, we implement and study an adversarial search agent in an
attempt to win the game of Knights Isolation. We explore various advanced
heuristic functions using both iterative deepening and alpha-beta pruning.

# Definition of Heuristics

## Baseline Heuristic

The first **baseline** heuristic function is the number of moves available to
the active player minus the number of moves available to the opponent. This is a
very simple that is simply a measure of the number of moves available to each
player, weighted equally.

$$h_1 = p - o \tag{1}$$

where:

- $p$ = number of moves available to active player
- $o$ = number of moves available to opponent

**Note:** The baseline heuristic is functionally and strategically equivalent to
$m\!\!=\!\!0.5$ in the advanced heuristics described below.

## Advanced Heuristics

The **advanced** heuristic functions ($h2$, $h3$, and $h4$) are defined based on
a weighting scheme between the number of moves available to each player.

$$h_i = m \cdot p - (1 - m) \cdot o \tag{2}$$

Where the weights, $m$, are provided in Table \ref{weights}.

| Label | Strategy | $m$ |
| -------- | -------- | -------- |
| h1 | Baseline Heuristic|  n/a |
| h2 | Offensive Strategy | 0.25 |
| h3 | Defensive Strategy | 0.75 |
| h4 | Offensive to Defensive Strategy | varying |
Table: Heuristic Strategies and Weights \label{weights}

In Equation (2), when $m\!\!=\!\!0$, the heuristic function is equivalent to the
number of moves available to the opponent. When $m\!\!=\!\!1$, the heuristic
function is equivalent to the number of moves available to the active player.
Note that the baseline heuristic is equivalent to $m\!\!=\!\!0.5$, however, we
do not explicitly define it as such. 

The $h_2$ and $h_3$ heuristic functions use a fixed weighting that represent an
**offensive strategy** and **defensive strategy**, respectively. The last
heuristic ($h_4$) is an **offensive to defensive strategy** provided by dynamic
weighting that changes throughout the game based on the ratio of the number of
moves played so far (`state.ply_count`) to the board size (`state.board_size()`),
as follows.

$$m_4 = \frac{\mathrm{current move}} {\mathrm{board size}} \tag{3}$$

This dynamic weighting provides a **smooth** means of transitioning from a more
offensive strategy (toward the beginning of the game) to a more defensive
strategy (toward the end of the game).

**Note:** The function `state.board_size()` is a new function that was added to
return the number of squares on the board, corresponding to the `_SIZE` variable in
`isolation.py`.

# Results

The Knights Isolation game was played in two modes, with and without fairplay.
For each mode, the game was played with each of the four heuristic functions and
a depth limit of 5, for a total of 20 rounds. The results of the
games are presented in Table \ref{results} in the form of a win percentage against the Minimax Agent.

| Heuristic Title | Win % w/out Fairplay | Win % w/ Fairplay |
|:---------------:|:--------------------:|:-----------------:|
| h1              | 57.5                 | 62.5              |
| h2              | 55.0                 | 63.8              |
| h3              | 65.0                 | 67.5              |
| h4              | 70.0                 | 73.8              |
Table: Results of Knights Isolation Game \label{results}
