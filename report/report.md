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

The first **baseline** heuristic function is the number of moves available to
the active player minus the number of moves available to the opponent. This is a
very simple that is simply a measure of the number of moves available to each
player, weighted equally.

$h_1 = p - o$

where:

- $p = $ number of moves available to active player
- $o = $ number of moves available to opponent

The **advanced** heuristic functions ($h2$, $h3$, and $h4$) are defined based on
a weighting scheme as follows:

$h_i = m \cdot p - (1 - m) \cdot o$

In the above equation, when $m\!\!=\!\!0$, the heuristic function is equivalent
to the number of moves available to the opponent. When $m\!\!=\!\!1$, the
heuristic function is equivalent to the number of moves available to the active
player. Note that the baseline heuristic is equivalent to $m\!\!=\!\!0.5$,
however, we do not explicitly define it as such. For the advanced heuristics
explored in this report, we use the following values for $m$:

| Label | Strategy | $m$ |
| -------- | -------- | -------- |
| h1 | Baseline Heuristic| n/a |
| h2 | Offensive Strategy | 0.25 |
| h3 | Defensive Strategy | 0.75 |
| h4 | Offensive to Defensive Strategy | Based on number of moves played

The advanced heuristics include a weighting scheme between the number of moves
available to each player. The $h_2$ and $h_3$ heuristic functions use a fixed
weighting that represent an offensive strategy and defensive strategy,
respectively. The last heuristic ($h_4$) provides a dynamic weighting that
changes based on the number of moves that have been played in the game so far.
This dynamic weighting provides a **smooth** means of transitioning from a more
offensive strategy (toward the beginning of the game) to a more defensive
strategy (toward the end of the game).

$h = m * own_lib - (1 - m) * opp_lib$