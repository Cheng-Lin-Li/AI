## This is an implementation of Propositional Logic Resolution, WalkSAT, and Propositional Knowledge Base Algorithms in Python 3
## The task:

This implementation wants to arrange the wedding seating for a certain number of guests in a hall. The hall has a certain number of tables for seating. 

### Rules of the Wedding
* Some pairs of guests are couples or close Friends (F) and want to sit together at the same table. 
* Some other pairs of guests are Enemies (E) and must be separated into different tables. 
* The rest of the pairs are Indifferent (I) to each other and do not mind sitting together or not. 
* However, each pair of guests can have only one relationship, (F), (E) or (I). 

The program must find a seating arrangement that satisfies all the constraints.

### SAT Encoding

To decompose the arrangement task, there are three constraints the program has to satisfy: 
```text
(a) Each guest should be seated at one and only one table. 
(b) For any two guests who are Friends (F), you should seat them at the same table. 
(c) For any two guests who are Enemies (E), you should seat them at different tables. 
```

Note that, for simplicity, you do NOT need to consider the capacity constraint of a table. This means the size of each table is assumed to be large enough to seat all the guests.

The arrangement task can be encoded as a Boolean satisfaction problem. We introduce Boolean variables X mn to represent whether each guest m will be seated at a specific table n.
The program constructs clauses and generate CNF sentence for each instance of the seating arrangement. 

Suppose there are < M > guests in total, and there are < N > tables in the hall. 
The implementation assumes each table has an unlimited capacity.
The program has to express each of the above-mentioned constraints as clauses in CNF format.

### Programming Task: SAT Solver

The program has to generate CNF sentences for an input instance of wedding seating arrangements. 
The inputs include the number of guests < M>, the number of tables < N >, and a sparse representation of the relationship matrix R with elements Rij= 1 , -1 or 0 to represent whether guests i and j are Friends (F), Enemies (E) or Indifferent (I). 

The internal representation of CNF sentences are free format. The program will NOT input or output sentences for the user for this assignment. 

In general, it is a good idea to use the most efficient representation possible, given the NP-complete nature of SAT. For instance, in Python, the program represent a CNF sentence as a list of clauses, and represent each clause as a list of literals.

The program implements a SAT solver to find a satisfying assignment for any given CNF sentences. 

In this assignment, the program implement a modified version of the PL-Resolution algorithm ( AIMA Figure 7.12 ). Modifications are necessary because it is using the algorithmfor a slightly different purpose than is explained in AIMA. 

Here, the program is not looking to prove entailment of a particular query. Rather, it hopes to prove satisfiability. Thus, there is no need to add negated query clauses to the input clauses. In other words, the only input to the algorithm is the set of clauses that comprise a randomly generated sentence. As an additional consequence of the purpose, the outputs will be reversed compared to the outputs listed in AIMA’s pseudo code. That is to say, if the empty clause is derived at any point from the clauses of the input sentence, then the sentence is unsatisfiable. In this case, the function should return `false` and not `true` as the book specifies for this situation. In the opposite situation where the empty clause is never derived, the algorithm should return `true`, indicating that the sentence is satisfiable.

The program implement the WalkSAT algorithm ( AIMA Figure 7.18 ) to search for a solution for an instance of wedding. There are many variants of this algorithm that exist, but this program implements an identical algorithm that described in AIMA. There are two open parameters associated with WalkSAT: <p> and <max_flips>.

PL-Resolution is a sound and complete algorithm that can be used to determine satisfiability and unsatisfiability with certainty. On the other hand, WalkSAT can determine satisfiability (if it finds a model), but it cannot absolutely determine unsatisfiability. If the PL-Resolution determines the sentence is satisfiable, then you have to run your WalkSAT, and tune the parameters to find at least one solution.


## The implementation:

Click [** Here **](https://github.com/Cheng-Lin-Li/AI/blob/master/Propositional_Logic/PL_Resolution_WalkSAT.py) to read the source code.

#### Usage: python PL_Resolution_WalkSAT.py	

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

## Reference:
* Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach (AIMA). Prentice Hall, 3rd Edition. [http://aima.cs.berkeley.edu/](http://aima.cs.berkeley.edu/)
* AIMA reference code, aimacode/aima-python : https://github.com/aimacode/aima-python
* MIT open Course. [Resolution Theorem Proving: Propositional Logic](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-825-techniques-in-artificial-intelligence-sma-5504-fall-2002/lecture-notes/Lecture7FinalPart1.pdf)

## Notice:

This code is just for your reference of the implementation. The code does not give a guarantee of 100% correctness.
