## This is an implementation of Decision Network with Decision Nodes, Chance Nodes, and Utility Nodes Algorithms in Python 3

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

#### Input: A data file "input.txt" in the same folder. The file contains the relevant records.

You may redefine the input file name by changeig initial variable, INPUT_FILE = 'input.txt', in the code to any other file name you want.
Or just rename your input file to input.txt

#### Output:

A single line output `yes/no` to indicate whether the sentence is satisfiable or not. If the sentence can be satisfied, output `yes` in the first line, and then provide just one of the possible solutions. (Note that there may be more than one possible solution, but again, the task is to provide only one of them.) 

Each line after “yes” contains the assigned table for a specific guest for the solution. For example, in the sample output, line 2 represents guest 1 has been assigned at table 2 . Please note that the output lines for assigning tables to guests should be in ascending order of indices (1,2,3,..., M). Lastly, If the sentence can not be satisfied, output only a single line `no`.


## Example Test Case:

Sample Input 
```
4 2
1 2 F 
2 3 E
```

The first line contains two integers denoting the number of guests < M> and the number of tables < N> respectively. Each line following contains two integers representing the indices of a pair of guests and one character indicating whether they are Friends ( F) or Enemies ( E). The rest of the pairs are indifferent by default. For example, in the above sample input, there are 4 guests and 2 tables in total, and guest 1 and guest 2 are Friends, and guest 2 and guest 3 are Enemies.

Sample Output 
```
yes 
1 2
2 2 
3 1 
4 1
```

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
