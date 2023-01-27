"""
Encodes game logic for OneUp, and manages game for players.
"""

import numpy as np

SCORE_MAX = np.inf

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

# List of ([guess a, guess b], expected score)
tests = [
    ([5,5], 0),
    ([5,6], SCORE_MAX),
    ([0,1], SCORE_MAX),
    ([9,10], SCORE_MAX)
]



"""  """
SCORE_TOP = 10

# TODO perhaps impose a<=b for scoring?
# Or maybe do not need to
def score(a:int, b:int):
    assert (0 <= a and a <= 10), f'Score recieved guess a outside [0, 10]'
    assert (0 <= b and b <= 10), f'Score recieved guess b outside [0, 10]'
    diff = b-a 
    if diff == 0: return 0
    score = SCORE_TOP/diff 
    return score

for a in range(11):
    for b in range(11):
        print(f'({a},{b}):{score(a,b)}')
