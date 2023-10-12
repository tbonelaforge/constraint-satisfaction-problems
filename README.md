## Constraint Satisfaction Problems ##

This project represents some independent study I did when learning about Constraint Satisfaction Problems in AI. This code was written to help understand and demonstrate the following optimization techniques, which are used with the basic backtracking algorithm.
 
 1. "Minimum Remaining Values" (with maximal degree heuristic) for variable ordering
 
 2. "Least Constraining Value" for value ordering.

### What are all these files for? ###

* backtracking_search.py - Different versions of basic backtracking search function from chapter 6 in the [Russel and Norvig AI textbook](https://www.pearson.com/en-us/subject-catalog/p/artificial-intelligence-a-modern-approach/P200000003500/9780134610993?utm_source=google&utm_medium=cpc&utm_campaign=pla_pearson_print_manual&gclid=Cj0KCQjwsp6pBhCfARIsAD3GZubqgdCug6aPolYBkH4x9w9QD0Ym_99kyA7rkc6hV3HoJgaXNb9Rjd8aAk65EALw_wcB&gclsrc=aw.ds "Artificial Intelligence textbook: Artificial Intelligence A Modern Approach (Fourth Edition)"). This file includes some specific tests of both graph coloring and n-queens problem instances. 

* combos.py - Used to find specific examples of graph-coloring problems which cause backtracking.  Basically enumerates all graphs on a given set of nodes, and then determines the chromatic number using repeated applications of backtracking search. Outputs only the problem instances which actually trigger backtracking. These used as test cases for subsequent optimizations

* graph_coloring_csp.py - First version of CSP class encapsulating a graph coloring problem.  Basically just provides a `get_neighbors` function, and uses it to check a proposed color assignment for constraint violation i.e adjacent colors.

* graph_coloring_csp2.py - Second version of CSP class for graph coloring.  Allows variable ordering and value ordering optimizations, by maintaining "taken counts" for each node and color. The value of  `taken_counts[node][color]` corresponds to how many neighbors of that node have taken that color so far.


* n_queens_csp.py - Flat-footed CSP class representing N-queens problem.  Works with simple dictionary representing assignment of row positions to each column, and only provides the `is_consistent` method to be checked at each proposed assignment.


* n_queens_assignment.py - Data structure used in the first version of optimizing N-queens problems. Handles recording the "attack counts" for each possible square on the board, similar to the "taken counts" of the `GraphColoringCSP2` class above. When considering a given row and column, The value of `attack_counts[row][column]` is how many previously-assigned queens can attack that square.

* n_queens2.csp.py - First version of optimizing for N-queens problems. Allows variable ordering during backtracking search, using only the "Minimum remaining values" method (no max-degree heuristic). Depends on the `NQueensAssignment` class above.