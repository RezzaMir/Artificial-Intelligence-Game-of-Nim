# AI Game of Nim
Artificial Intelligence

Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object.

Two players take turns removing objects from distinct heaps or rows
1) Matches, cards, pebbles, …
2) On each turn, a player must remove at least one object from the same row
3) Goal is to avoid taking the last object

![1](https://user-images.githubusercontent.com/102126445/164950901-5e5e16b2-16cd-4f10-9f3c-f78b4648c067.png)

# How the code works?

Add these 2 files to your code:

Games.py : https://github.com/aimacode/aima-python/blob/master/games.py

Utils.py : https://github.com/aimacode/aima-python/blob/master/utils.py

Players: Max, min

Board: A tuple of integers, each integer is the number of matchsticks in that row (1,3,5,7)

An action: A pair (n, m): remove m matchsticks from row n

actions(s): set of valid actions in state s
{(0,1), (1,1), (1,2), (1,3),(2,1), (2,2), …}

Note: Python uses 0-based indexing: indexes start from 0

result(s, a): new state when action a is made in state s

terminal_test(s): has the game ended?
MAX (0,0,0,0): True
MAX (0,0,2,2): False
utility(s): if game has ended, how good is state s (for Max player)?
MAX (0,0,0,0): +100

Stage 1

![Picture1](https://user-images.githubusercontent.com/102126445/164950896-818eae4e-c3f3-4724-bb27-7414677d79ab.png)

Gameplay

![Picture3](https://user-images.githubusercontent.com/102126445/164951124-c29e1e47-097e-42c7-94ed-5ac1e4cc6baa.png)



