# Graphs.graph
Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.

## Vertex
```python
Vertex(self, data)
```

### add_neighbor
```python
Vertex.add_neighbor(self, vertex, weight=0)
```
Add a neighbor along a weighted edge.
### get_neighbors
```python
Vertex.get_neighbors(self)
```
Return the neighbors of this(self) vertex.
### get_id
```python
Vertex.get_id(self)
```
Return the data of this vertex.
### get_edge_weight
```python
Vertex.get_edge_weight(self, vertex)
```
Return the weight of this edge.
## Graph
```python
Graph(self, directed=False)
```
Graph Class A class demonstrating the essential
facts and functionalities of graphs.

### add_vertex
```python
Graph.add_vertex(self, key)
```
Add a new vertex object to the graph with the given key and
return the vertex.
### get_vertex
```python
Graph.get_vertex(self, key)
```
Return the vertex if it exists
### get_neighbors_of
```python
Graph.get_neighbors_of(self, vertex)
```
Grabs all the neighbors of the current vertex

Args:
    vertex (str): a given vertex

Returns:
    vertex (Vertex): Vertex object if found

### get_vertices
```python
Graph.get_vertices(self)
```
Return all the vertices in the graph
### get_edges
```python
Graph.get_edges(self)
```
Return number of all edges in the graph
### find_shortest_path
```python
Graph.find_shortest_path(self, from_vertex, to_vertex)
```
Search for the shortest path from vertex a to b using Breadth first search

Args:
    from_vertex (str) : starting point on the graph
    to_vertex (str) : the distanation or end of the path

Returns:
    shortest path (tuple): List of vertices in the path and len
                            Empty list if path does not exist

### breadth_first_search_traversal
```python
Graph.breadth_first_search_traversal(self, from_vertex)
```
Traversing entire grapgh using breadth first search algorithm.
The algorithm adapted from:
https://en.wikipedia.org/wiki/Breadth-first_search

Args:
    vertex (str): given vertex to find its all neighors
Returns:
    vertices(tuple): first item is all vertices in a bfs order
                    second item is levels of other vertices from starting vertex

### n_level_bfs
```python
Graph.n_level_bfs(self, from_vertex, n_level)
```
Find all nth level connections of

Args:
    vertex (str): given vertex to find its all neighors
    n_level (int): certain connection level away from vertex

Returns:
    all nodes (list): all nodes found at the nth level
                      if there is no given level of connections raises value error

### dfs_recursive
```python
Graph.dfs_recursive(self, from_vertex, visited=None, order=None)
```
Traverse the graph and get all vertices using DFS algorithm

### clique
```python
Graph.clique(self)
```
Finds a clique in a graph that cannot have any other vertices added
to it (note this is called a maximal clique)
FULL CREDIT: Vincenzo Marcella
https://github.com/C3NZ/CS22-tutorial/tree/master/tutorial

Returns:
    clique (set): set of cliques, else empty set

## build_graph
```python
build_graph(graph: Graphs.graph.Graph, vertices, edges)
```
Creates a graph with vertices and edges

Args:
    graph(Graph): Graph object
    vertices(list): list of vertices passed to build graph
    edges(list): list of edges passed to build graph

Returns:
    graph(Graph): Graph object with its edges and vertices added

