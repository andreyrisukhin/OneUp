# OneUp
OneUp is a game I created. Two players guess numbers in [0,9]. Scores are greatest when a player guesses one greater than their opponent.

## Details
Integers are transitive, which would be a problem for OneUp: players could guess greater and greater values to earn points. If we restrict the domain to [0,9], the degenerate strategy is for both players to guess 9, the maximum value.

To avoid this, we map all integers into the interval [0, 9] by applying modulus_10 to each guess. This is similar to transforming the linear number line into a spiral, and then looking at the spiral head-on. 

Now, players can guess any number and see it mapped to [0,9]. The winning player has a guess "closer and above" the other player. Imagine two hands on a clock, representing guess A and guess B. Rotate both so that guess A is at 0. The smaller angle between them defines who earns the points, A or B.

A function takes the difference between the greater and lesser guess, and outputs the score. The output score is maximal when greater guess - lesser guess = 1, hence the name of the game "OneUp". The score approaches 0 as the difference in guesses approaches a half rotation (multiple of 5 in this case).

## TODO

* Add visuals and improve the description
* Support more than 2 players (arbitrarily many)
* Take console input, the usual boilerplate for a game utility
