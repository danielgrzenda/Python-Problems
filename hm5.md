# Homework 4! No Prob LLamma
Very similar problems have appeared in programming competitions.  Try to solve each problem in ~1 to 2 hours.  Start by enrolling into git so you download testing files.  https://classroom.github.com/a/KLpCoBDy

# 1, Lazy cryptocurrency trader
Bud Liteconintius, the famous cryptocurrency trader, is having a lazy day at this pool, and between episodes of Breaking Bad she eating pizza. Foretelling the future is hard, but imagine if you could just go back in time and use your knowledge of cryptocurrency price history in order to maximize your profits!
Now Bud starts to wonder: if she were to go back in time a few days and bring a $100 with her, how much money could she make by just buying and selling Bitcoin (the most volatile cryptocurrency in existence) at the right times? Would she earn enough to retire comfortably in a mansion on Nashville, TN?

 Note that Bud can not buy fractional coins, she must buy whole coin in Bitcoin. The total number of coins in Bitcoin is 100 000, so Bud can not own more than 100 000 coins at any time. In Bud's daydream, the world is nice and simple: there are no fees for buying and selling coins, cryptocurrency prices change only once per day, and her trading does not influence the valuation of the stock.


## Input
The first line of input contains an integer `d(1 ≤ d ≤ 365)`, the number of days that Bud goes back in time in her daydream. Then follow d lines, the i’th of which contains an integer `pi(1 ≤ pi ≤ 500)` giving the price at which Bud can buy or sell Bitcoin on day i. Days are ordered from oldest to newest.

## Output
Output the maximum possible amount of money Gina can have on the last day. Note that the answer may exceed 2^32.

## Example

Input:

```
6
100
200
100
150
125
300
```

Output: `650`

## How to test
Run `lazy_crypto_test.py` from the directory, expected output:

```
[01-increasing.in]: PASS
[00-example.in]: PASS
```

Note, that program will be tested with more input files than in your repository :).

## 2, No More Games

The gaming company Sandstorm is developing an online two player game.
You have been asked to implement the ranking system.
All players have a rank determining their playing strength which gets updated after every game played.
There are `25` regular ranks, and an extra rank, `Legend`,
above that. The ranks are numbered in decreasing order, `25` being the
lowest rank, `1` the second highest rank, and Legend the highest rank.

Each rank has a certain number of `stars` that one needs to gain before advancing to the
next rank. If a player wins a game, she gains a star. If before the game the player was on rank `6`-`25`,
and this was the third or more consecutive win, she gains an additional bonus star for that win.
When she has all the stars for her rank (see list below) and gains another star, she
will instead gain one rank and have one star on the new rank.

For instance, if before a winning game the player had all the stars on her current rank,
she will after the game have gained one rank and have `1` or `2` stars (depending on whether she got a bonus star)
on the new rank. If on the other hand she had all stars except one on a rank, and won
a game that also gave her a bonus star, she would gain one rank and have `1` star on the new rank.

If a player on rank `1`-`20` loses a game, she loses a star. If a player has zero stars on a rank and loses a star, she will lose a rank and have all stars minus one on the rank below. However, one can never drop below rank `20` (losing a game at rank `20` with no stars will have no effect).

If a player reaches the Legend rank, she will stay legend no matter how many losses she incurs afterwards.

The number of stars on each rank are as follows:

* Rank `25`-`21`: `2` stars
* Rank `20`-`16`: `3` stars
* Rank `15`-`11`: `4` stars
* Rank `10`-`1`: `5` stars


A player starts at rank `25` with no stars. Given the match history of a
player, what is her rank at the end of the sequence of matches?

## Input

The input consists of a single line describing the sequence of matches. Each character corresponds to one game; `W` represents a win and `L` a loss. The length of the line is between `1` and `10,000` characters (inclusive).

## Output

Output a single line containing a rank after having played the given sequence of games; either an integer between `1` and `25` or `Legend`.


## Examples
* In `WW` out `25`
* In `WWW` out `24`
* In `WLWLWLWL` out `24`
* In `WWWWWWWWWLLWW` out `19`
* In `WWWWWWWWWLWWL` out `18`

## How to test
Run `ranking_test.py` from the directory, expected output:

```
->python ranking_test.py
[1.in]: PASS
[2.in]: PASS
[3.in]: PASS
[4.in]: PASS
[5.in]: PASS
[6.in]: PASS
[7.in]: PASS
```

Note, that program will be tested with more input files than in your repository :).

## Find your way home

You are to part of a team developing animated compass needle. The API is simple: the compass needle is currently in some direction (between~`0` and~`359` degrees, with north being~`0`, east being~`90`),
and is being animated by giving the degrees to spin it. If the needle is pointing north, and you give the compass an input of~`90`, it will spin clockwise (positive numbers mean clockwise direction) to stop at east, whereas an input of~`-45` would spin it counterclockwise to stop at north
west.

The compass gives the current direction the phone is pointing and Jonas'
task is to animate the needle taking the `shortest path` from the current needle direction to the correct direction.  Many `if`s, moduli, and even an arctan later, he is still not convinced his `minimumDistance` function is correct; he calls you on the phone.

## Input

The first line of input contains an integer `n_1 (0 ` &#x2264; `n_1` 	&#x2264; `359)`, the current direction of the needle.  The second line of input contains an integer `n_2` (`0` 	&#x2264; `n_2` 	&#x2264; `359`), the correct direction of the needle.

## Output
Output the change in direction that would make the needle spin the shortest distance from~`n_1`
to~`n_2`.  A positive change indicates spinning the needle clockwise, and a negative change indicates spinning the needle counter-clockwise.
If the two input numbers are diametrically opposed, the needle should travel clockwise.  I.e., in this case, output~`180` rather than~`-180`. % Simpler to evaluate!

## How to test
Run `compas_test.py` from the directory, expected output:

```
->python compas_test.py
[1.in]: PASS
[2.in]: PASS
[3.in]: PASS
```

## Examples

In:
```
315
45
```
Out `90`

In:
```
180
270
```
Out `90`

In:
```
45
270
```
Out `-135`

# Deliverables
1) File `lazy_crypto.py` with the implementation of problem 1, located in folder `lazy`.
2) File `ranking.py` with the implementation of problem 2, located in folder `ranking`.
2) File `compas.py` with the implementation of problem 2, located in folder `compas`.


# How to submit

Use the invitation link below to create the repo:
https://classroom.github.com/a/KLpCoBDy
