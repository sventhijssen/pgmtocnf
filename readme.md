# PGMtoCNF

PGMtoCNF converts a probabilistic graphical model (PGM) to a Bayesian network in conjunctive normal form (CNF) with according weights.

## Getting Started

### Prerequisites

- Make sure your working directory is set to the root of the project

## How to use
- Nodes are represented by a name and the possible values:  
  ```Node(name, [values])```
- Edges are directed edges. The first node is the start node, the second node is the end node:  
```Edge(start, end)```
- Weights are either non-conditional or conditional:  
```Weight((node, value), probability)```  
```Weight((node, value), probability, ([(node, value)]))```

## Examples
Examples are given in the ```examples``` folder
