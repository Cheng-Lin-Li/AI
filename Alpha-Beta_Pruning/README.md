## This is an implementation of Alpha Beta Pruning Algorithm in Python 2.7
## The task:

In this implementation, the program determines the minimax value for given positions of the Reversi game, using the Alpha-Beta pruning algorithm with positional weight evaluation functions.

### Rules of the Game
* The rules of the Reversi game can be found at [http://en.wikipedia.org/wiki/Reversi](http://en.wikipedia.org/wiki/Reversi) and 
interactive examples can be found at [http://www.samsoft.org.uk/reversi/](http://www.samsoft.org.uk/reversi/). 
In the Othello version of this game, the game begins with four pieces (two black, two white) placed right in the middle of an 8x8 grid, 
with the same-colored pieces on a diagonal with each other (see the left side of Figure 1). 
A move of a player can be either a valid move or pass move.

* The Alpha-Beta algorithm (Figure 5.7, AIMA 3 rd edition) determines the depth-bounded minimax values of given game positions. 
the program will take the input from the file input.txt, and print out its output to the file output.txt. 
Each input of your program contains a game position (including the board state and the player to move) and a search cut-off depth D, 
and the program should output the corresponding information after running an Alpha-Beta search of depth D. 
That is, the leaf nodes of the corresponding game tree should be either a game position after exactly D moves 
(alternating between Black and White) or an end-game position after less than D moves. 
A leaf node is evaluated by the following evaluation function:

### Evaluation function: positional weights 

In this evaluation function, each cell i of the board has a certain strategic value Wi. 
For example, the corners have higher strategic values than other cells. The map of the cell values is shown below.

```text
|  | a | b | c | d | e | f | g | h |
|1 | 99| -8|  8|  6|  6|  8| -8| 99|
|2 | -8|-24| -4| -3| -3| -4|-24| -8|
|3 |  8| -4|  7|  4|  4|  7| -4|  8|
|4 |  6| -3|  4|  0|  0|  4| -3|  6|
|5 |  6| -3|  4|  0|  0|  4| -3|  6|
|6 |  8| -4|  7|  4|  4|  7| -4|  8|
|7 | -8|-24| -4| -3| -3| -4|-24| -8|
|8 | 99| -8|  8|  6|  6|  8| -8| 99|
```

Given these “weights”, the evaluation function of a given game position s (with respects to a specific player) 
can be computed by

E(s) = Sum Wi - Sum Wj, where i belongs to player's cells and j belongs to opponent's cells

For example, the game position in the right side of Figure 4 is evaluated, with respect to Black, as E(s) = (4+0+0+0) - (0) = 4; while it is evaluated with respect to White as E(s) = (0) - (4+0+0+0) = -4.

Note: The leaf-node values are always calculated by this evaluation function, even though it is an end-game position. Although this may not be a good estimation for the end-game nodes (and is a deviation from the “official” Reversi rules), you should comply with this rule for simplicity (so that you do not need to worry about possible ordering complications between terminal utility values and evaluation values at non-terminal nodes).

### Tie breaking and expansion order

Ties between the legal moves are broken by handling the moves in positional order, that is, first favor cells in upper rows, and in the same row favoring cells in the left side. 


## The implementation:

Click [** Here **](https://github.com/Cheng-Lin-Li/AI/blob/master/Alpha-Beta_Pruning/Alpha-Beta_Pruning.py) to read the source code.

#### Usage: python Alpha-Beta_Pruning.py	

#### Input: A data file "input.txt" in the same folder. The file contains the relevant records.

You may redefine the input file name by changeig initial variable, INPUT_FILE = 'input.txt', in the code to any other file name you want.
Or just rename your input file to input.txt

#### Output:

<next state> <traverse log> where the traverse log requires 5 columns. Each column is separated by “,”. The fivecolumns are node, depth, minimax value, alpha, beta.


## Example Test Case:

As an example, the following input instance asks to compute a depth-2 alpha-beta search from the starting game position: 
```text
X 

2

******** 
******** 
******** 
***OX*** 
***XO*** 
******** 
******** 
********
```

and the corresponding output should be: 

```text
******** 
******** 
***X**** 
***XX*** 
***XO*** 
******** 
******** 
********
Node,Depth,Value,Alpha,Beta 
root,0,-Infinity,-Infinity,Infinity 
d3,1,Infinity,-Infinity,Infinity 
c3,2,-3,-Infinity,Infinity 
d3,1,-3,-Infinity,-3 
e3,2,0,-Infinity,-3 
d3,1,-3,-Infinity,-3 
c5,2,0.0,-Infinity,-3 
d3,1,-3,-Infinity,-3 
root,0,-3,-3,Infinity 
c4,1,Infinity,-3,Infinity 
c3,2,-3,-3,Infinity 
c4,1,-3,-3,-3
root,0,-3,-3,Infinity 
f5,1,Infinity,-3,Infinity
f4,2,0,-3,Infinity 
f5,1,0,-3,0 
d6,2,0,-3,0 
f5,1,0,-3,0 
f6,2,-3,-3,0 
f5,1,-3,-3,-3
root,0,-3,-3,Infinity 
e6,1,Infinity,-3,Infinity 
f4,2,0,-3,Infinity 
e6,1,0,-3,0 
d6,2,0,-3,0 
e6,1,0,-3,0 
f6,2,-3,-3,0 
e6,1,-3,-3,-3
root,0,-3,-3,Infinity
```

## Notice:

This code is just for your reference of the implementation. The code does not give a guarantee of 100% correctness.
