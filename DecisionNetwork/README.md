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

The result should be printed to a file called output.txt. Given the sample input above, the output content should be as follows:

(output01 for input sample01.txt)
0.25
0.43

(output02 for input sample02.txt)
0.76
59
37
+ 59
- 44

For each query in the input file, your program should generate a corresponding result (one result per line) as the output. The result may have three forms:

●	“P” query: A decimal value between 0 and 1, rounded to two decimals (for example, we want 0.395 to be 0.40):
e.g.	0.40
1)	“EU” query: An integer value:
e.g.  	50
2)	“MEU” query: One sign(“+” or “-” ) for each decision node, followed by an integer value representing the maximum expected utility, all separated with a single whitespace:
e.g. 	+ 50

●	When there are multiple decisions, the order of decisions should be the same as in the query.
e.g. 	Input:  MEU(I, L)
●		Output:  + - 50
●	The test cases will be designed so that there will always be one unique solution with MEU.
●	For EU and MEU queries, all calculations should be done in decimal number accuracy, but the output expected utility value should be rounded to the nearest integer (for example, we want 3.5 to be rounded to 4).
●	Don’t print additional whitespace after the value, or extra line break in the end.

## Program structure:

It defines classes_and_methods below:
```python
Propositional_Logic: A propositional logic operation class in CNF with DPLL and WalkSAT algorithm.

    Operators include: AND, OR, NOT can be defined in global variable

    The CNF sentence '(A OR B) AND (NOT C)' can be represented as below data structure:

        sentence[clause1{Literal1, Literal2}, clause2{~Literal3}]

            1. sentence is a list to contain sets.

            2. Clause is a set with Literals.

            3. Literal presents by string.

    The sentence should be in CNF, which equal to 

        1. every set in list should be associated with AND, and 

        2. every literal in set should be associated with OR

    

    Major Functions:

    1. is_satisfiable(KB, algorithm = 'DPLL'): This implementation include DPLL and PL_Resolution algorithm to verify the satisfiability of the sentence. You can switch the global variable, ALGORITHM = 'DPLL' # or 'PL_Resolution', to change it.

        You can choose either 'DPLL' or 'PL_Resolution' to switch the algorithm.

    2. DPLL: This algorithm is used for checking satisfiability of a CNF sentence in propositional logic.

        The method will also store the satisfiable model into the 'model' variable in class.

    3. WalkSAT: Inference methods which are implemented to provide one of models in CNF sentence of propositional logic.

    4. PL_Resolution: A structure only class. Need to be completed in the future.

        The class will check a propositional logic sentence is satisfy or not.
```

```python
Prop_KB: A knowledge base can be Ask, Tell in propositional logic by CNF.

    Major Functions:

        tell(clauses): input CNF clauses.

        ask(CNF_query) will not implement in this case.

        get_sentence(): will present the KB in a CNF sentence.        
```
    
```python
Wedding: A wedding arrangement class to solve a the question.

    1. According to given rule to generate CNF sentence.

    2. Input the sentence to KB.

    3. Verifing the KB is satisfiable or not.

    4. If the KB is satisfiable, then get a model/solution by WalkSAT.

    5. Printing the results.
```

```python
    def getWeddingRules(self):
        # Every clause is 'OR' connect with each other clause, every sentence is 'AND' connect with each other sentence.
        # atomic = [guest, table]
        # CNF: (AvB) ^ (~C) = [{'A','B'}, {'~C'}]
        #The outer list is a conjunction of clauses. Each inner list is a clause, i.e. a disjunction of literals.
```

## Global Variables:
* You can switch the global variable, `ALGORITHM = 'DPLL' # or 'PL_Resolution'`, to change it.
* Logic operation define as below:

```python
AND = '^'
OR = 'v'
NOT = '~'
```
* The implement add one more constraint. All tasks have to be done in 2 minutes. Below parameters can help you to define the resource (time/seconds) for each process. According to the default setting below, if the DPLL cannot find a confirmation in 70 seconds, the program will try WalkSAt to get a solution in 49 seconds.
```
RESOURCE_DPLL = 70
RESOURCE_WALKSAT = 49
```

## Reference:
* Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach (AIMA). Prentice Hall, 3rd Edition. [http://aima.cs.berkeley.edu/](http://aima.cs.berkeley.edu/)
* AIMA reference code, aimacode/aima-python : https://github.com/aimacode/aima-python
* MIT Open Course Ware. [Resolution Theorem Proving: Propositional Logic](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-825-techniques-in-artificial-intelligence-sma-5504-fall-2002/lecture-notes/Lecture7FinalPart1.pdf)

## Notice:

This code is just for your reference of the implementation. The code does not give a guarantee of 100% correctness.
