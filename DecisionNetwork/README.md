## This is an implementation of Decision Network with Decision Nodes, Chance Nodes, and Utility Nodes Algorithms in Python 2.7

An implementation to get probability of Decision node, or Utility Nodes. 

## Introduction:

A decision network (Chapter 16, AIMA) uses a Directed Acyclic Graph (DAG) to represent a set of random variables and 
their conditional dependencies within a probabilistic model, while a decision network extends the Bayesian network to include 
decision nodes and utility nodes. The implementation performs inference in Decision Networks of discrete variables.

## The task:

A given decision network may have several decision nodes, several chance nodes, and at most one utility node. 
The program will answer queries using the given network:
 * Calculate a specific joint, marginal, or conditional probability.
 * Calculate the expected utility of a particular decision, or determine the decision with the maximum expected utility.

### Pseudocode

AIMA  Figure 14.9, Section 16.5.2

## The implementation:

Click [** Here **](https://github.com/Cheng-Lin-Li/AI/blob/master/DecisionNetwork/DecisionNetwork.py) to read the source code.

#### Usage: python DecisionNetwork.py	

#### Input: A data file "input01.txt" in the same folder. The file contains the relevant records.

* Example 1:

You will be given a text file ending with a .txt extension. For example, the decision network would be represented by the following file, sample01.txt:

```text
( L )
  |
  V
( N )     ( I )
  |         |
  \         /
   > ( D ) <
```

(sample01.txt)
```text
P(N = +, I = -)
P(D = + | L = +, I = +)
******
L
0.4
***
N | L
0.8 +
0.3 -
***
I
0.5
***
D | N I
0.3 + +
0.6 + -
0.95 - +
0.05 - - 
```

* Example 2:
An example of a decision network having decision nodes and one utility node is given below, and it can be represented by sample 02.txt:

```text
( L )
  |
  V
( N )     ( I )
  |         |
  \         /
   > ( D ) <
       |
       V
   <Utility> 
```
(sample02.txt)
```text
P(D = + | L = -, I = +)
EU(I = +)
EU(I = + | L = +)
MEU(I)
MEU(I | L = +)
******
L
0.4
***
N | L
0.8 +
0.3 -
***
I
decision
***
D | N I
0.3 + +
0.6 + -
0.95 - +
0.05 - -
******
utility | D
100 +
-10 -
```

#### Output:

The result should be printed to console (or a file called output.txt by modify the global variable `OUTPUT_FILE = output.txt #COULD BE 'OUTPUT_FILE = None' for console or file name (e.g. 'OUTPUT_FILE = 'output.txt') for file.'`). Given the sample input above, the output content should be as follows:

(output01 for input sample01.txt)
```text
0.25
0.43
```

(output02 for input sample02.txt)
```text
0.76
59
37
+ 59
- 44
```

For each query in the input file, the program should generate a corresponding result (one result per line) as the output. The result may have three forms:

* “P” query: A decimal value between 0 and 1, rounded to two decimals (for example, we want 0.395 to be 0.40):
e.g.	0.40
1)	“EU” query: An integer value:
e.g.  	50
2)	“MEU” query: One sign(“+” or “-” ) for each decision node, followed by an integer value representing the maximum expected utility, all separated with a single whitespace:
e.g. 	+ 50

* When there are multiple decisions, the order of decisions should be the same as in the query.
e.g. 	Input:  MEU(I, L)
*	Output:  + - 50
*	The test cases will be designed so that there will always be one unique solution with MEU.
*	For EU and MEU queries, all calculations should be done in decimal number accuracy, but the output expected utility value should be rounded to the nearest integer (for example, we want 3.5 to be rounded to 4).


## Reference:
* Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach (AIMA). Prentice Hall, 3rd Edition. [http://aima.cs.berkeley.edu/](http://aima.cs.berkeley.edu/)
* AIMA reference code, aimacode/aima-python : https://github.com/aimacode/aima-python

## Notice:

This code is just for your reference of the implementation. The code does not give a guarantee of 100% correctness.
