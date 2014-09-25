Prim_algorithm
==============
Graph G is used as the primary parameter in the functions which represents the graph in threes cases. 
Dict inside Dict structure is used to store data G[u][v] = weight where u and v is the vertex of the edge, weight is the cost of the edge.


Prim.py is the file to implement Prim’s algorithm. 
Function prim(G) takes G graph as input and returns weight of MST. O(mlogn)

pqdict.py is the code from github to implement priority queue in Prim’s algorithm,
which provides insert and update functions of values in priority queue
