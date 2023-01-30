"""
Encodes game logic for OneUp, and manages game for players.
"""
SCORE_TOP = 10

# List of ([guess a, guess b], expected score)
tests = [
    ([5,5], (0,0)),
    ([5,6], (0,SCORE_TOP)),
    ([0,1], (0,SCORE_TOP)),
    ([9,10], (0,SCORE_TOP))
]

def score(a:int, b:int):
    """
    Project the guesses a, b onto a clock face.
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