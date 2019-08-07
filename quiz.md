# Quiz Study Guide

## Quiz Format
Quizzes will be given in class either using on online format, paper format, or on interview / code interaction.


1. [General Instructions](#general-instructions)
1. [Quiz 1](#quiz-1)
1. [Quiz 2](#quiz-2)
1. [Quiz 3](#quiz-3)
1. [Quiz 4](#quiz-4)


## Quiz 1
### Graph Properties
- Model problems with graphs and graph properties
- Define several graph properties and identify them on a sample graph.


## Quiz 2
 ### Graph Traversal
- Implement Breadth-first search/ traversal on an unweighted graph or digraph.
- Implement Recursive Depth-first search on an unweighted graph or digraph.
- Generate a spanning tree from DFS or BFS.
- Write pseudocode for BFS, Iterative DFS or Recursive DFS
- Model solutions to applications using BFS or DFS such as:
  - How should I get home? (Shortest path with BFS)
  - Is there a way to send data to all the computers on the network? (Connected graph with DFS))


## Quiz 3
 ### Greedy Algorithms on Weighted Graphs: Prim's Algorithm, Dijkstra's Algorithm
 - Describe greedy algorithms.
 - Give an example of a greedy algorithm (existing or one you make up) that doesn't give the optimal result.
  - Debug code that implements Dijkstra's algorithm.
  - Explain how Prim's algorithm  works, implement by hand, debug code.
  - Discuss how a priority queue speeds up Dijkstra's algorithm.


 ## Quiz 4
  ### Dynamic Programming
 - Explain the 5 steps of Dynamic Programming.
    1. Identify the subproblems - breaking it down until base case. or what would be the smallest version of the problem.
    1. Guess first choice - arbitrarily choose the first best choice
    1. Recursively define the value of an optimal solution - see the pattern and call the function recursively
    1. Compute the value of an optimal solution (recurse and memoize) - memoize or store the already calculated values and have it ready if it is repeated. 
    1. Solve original problem - reconstruct from the sub-problems - reconstruct the problem from bottom-up 

 - Find a recurrence relation from a sub problem definition. - e.g. fib(3) -> fib(2) + fib(1)
    fib(2) -> fib(1) + fib(1). the occurance is F sub n = (F sub n-1) + (F sub n-1)
 - Draw a recursion tree from a recursive implementation of a dynamic programming problem.
    
 - Define memoization and how it speeds up a Dynamic Programming solution.
    - Memoization is optimization technique used by storing the function calls(results) in a cached storage in dictionaries for example. It speeds up the program because when the same call or calculation(input) occur. 

