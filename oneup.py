"""
Encodes game logic for OneUp, and manages game for players.
"""

# import numpy as np
# SCORE_MAX = np.inf

"""
Scoring for the greater guess: Map, difference to score
0:0
1:max
2:max/2
3:max/4
4:0
5:-1
6:
7:
8:
9:
10:-max

Interpret the (-) scores as instead being (+) going to the other player

Hmm, actually simpler than I thought at first
"""

# # Map difference to score
# scores = {
#     0:0,
#     1:10,
#     2:5,
#     3:2,
#     4:1
# }



# Hmm, perhaps scoring should be nontransitive? Imagine a clock, sawtooth wave score, 0 at noon and 6?
# Alternatively, asymmetric game? Not as preferable
# Mod() each guess, and mod() the difference
# Some +/- to get the noon and 6'oclock relationship
"""  """
SCORE_TOP = 10

# List of ([guess a, guess b], expected score)
tests = [
    ([5,5], (0,0)),
    ([5,6], (0,SCORE_TOP)),
    ([0,1], (0,SCORE_TOP)),
    ([9,10], (0,SCORE_TOP))
]

# TODO perhaps impose a<=b for scoring?
# Or maybe do not need to
def score(a:int, b:int):
#     assert (0 <= a and a <= 10), f'Score recieved guess a outside [0, 10]'
#     assert (0 <= b and b <= 10), f'Score recieved guess b outside [0, 10]'
#     diff = b-a 
#     if diff == 0: return 0
#     score = SCORE_TOP/diff 
#     return score

# for a in range(11):
#     for b in range(11):
#         print(f'({a},{b}):{score(a,b)}')

    """
    Copy theta idea from journal, position a always at noon and compare b
    
    Project guesses a, b onto a clock face.
    a_arrow -> 0, b_arrow -> (b-a) % 12
    Score piecewise, define angle t [t = (b_arrow-a_arrow) / 12]:
    > If t = 0 or t = 6, score is 0
    > If 0 < t < 6, b earns score that decreases from max to 0 as t increases
    > If 6 < t < 12, a earns same score function, with input t-6
    """

    """
    Return tuple of (a_score_change, b_score_change)
    """

    CLOCK_SIZE = 10 # Even integer
    SCORES_HAND = { # Integers only when guessing (keys) mapped to points earned
        0:0,
        1:10,
        2:7,
        3:4,
        4:2,
        5:1
    }
    a_arrow = 0
    b_arrow = (b - a) % CLOCK_SIZE
    t = (b_arrow-a_arrow) 

    # Scoring
    assert (t < CLOCK_SIZE and 0 <= t), f't out of bounds.'
    if t < CLOCK_SIZE/2:
        return (0, SCORES_HAND[t])
    else:
        return (SCORES_HAND[t-(CLOCK_SIZE/2)], 0)


# Testing!
for (guesses, expect) in tests:
    s = score(guesses[0], guesses[1])
    assert expect == s, f'Expected {expect} but calculated {s} for guesses {guesses}'

# TODO clean the data structure storing score

# The logic checks out! (-inf, inf) interval mapped to clock face, and score max for being 1up opponent.
s = score(2,3)
print(s)

""" Game is only interesting with nonrandom players, each tuning the other's prior """