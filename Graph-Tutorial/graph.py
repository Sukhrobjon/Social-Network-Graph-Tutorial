#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from queue import Queue


class Vertex(object):

    def __init__(self, data):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""

        self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.data} adjacent to {[x.data for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors.keys()

    def get_id(self):
        """Return the data of this vertex."""
        return self.data

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # vertex to the given vertex.
        return self.neighbors[vertex] if vertex in self.neighbors else None


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

# NOTE: id is the key and vertecies are the values


class Graph:
    def __init__(self, directed=False):
        """Initialize a graph object with an empty dictionary."""
        self.vert_dict = {}
        self.edge_list = []
        self.num_vertices = 0
        self.num_edges = 0
        self.directed = directed

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_dict.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""

        if key in self.vert_dict:
            print(f'Vertex {key} already exists')
            return

        # create a new vertex
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        self.num_vertices += 1

        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vert_dict.keys():
            return key
        return None

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""

        if from_vertex == to_vertex:
            print(f'You cant add the vertex to itself!')
            return

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            # add it - or return an error (choice is up to you).
            raise ValueError("One of the key doesn't exist!")

        # to handle the duplicate edges in undirected graph
        reversed_edges = (to_vertex, from_vertex, weight)

        if reversed_edges in self.edge_list and self.directed is True:
            return
        from_vert_obj = self.vert_dict[from_vertex]
        to_vert_obj = self.vert_dict[to_vertex]
        # add the to_vertex as a neighbor of from_vertex
        from_vert_obj.add_neighbor(to_vert_obj, weight)
        self.edge_list.append((from_vertex, to_vertex, weight))
        self.num_edges += 1

        # add the edges in both ways to be accessible if graph is undirected
        if self.directed == False:
            to_vert_obj.add_neighbor(from_vert_obj, weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return self.vert_dict.keys()

    def get_edges(self):
        """Return number of all edges in the graph"""
        return self.edge_list

    def shortest_path(self, from_vertex, to_vertex):
        """Search for the shortest path from vertex a to b using Breadth first search
        
        Args:
            from_vertex (str) : starting point on the graph
            to_vertex (str) : the distanation or end of the path

        Returns:
            shortest path (int) : the shortest number of edges between two vertices
        """
        #

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise KeyError(
                "One of the given vertices does not exist in graph!")

        # check if you are at the location
        if from_vertex == to_vertex:
            vert_obj = self.vert_dict[from_vertex]
            return [vert_obj.data], 0

        # grab the start location from graph
        current_vertex = self.vert_dict[from_vertex]
        seen_vertex = set()
        parent_pointers = {}
        # initialize the queue with size of number of verticies in the graph
        queue = Queue(maxsize=len(self.get_vertices()))

        # start the traversal
        queue.put(current_vertex)
        seen_vertex.add(current_vertex.data)

        path = []
        path_found = False
        parent = None
        current_vertex.parent = parent
        # alternative way of storing the references to parent  pointers
        parent_pointers[current_vertex.data] = None

        while queue:
            # dequeue the front element
            current_vertex = queue.get()
            path.append(current_vertex)

            # check if destination found
            if current_vertex.data == to_vertex:
                path_found = True
                break
            # otherwise
            for neighbor in current_vertex.neighbors:

                if neighbor.data not in seen_vertex:
                    queue.put(neighbor)
                    seen_vertex.add(neighbor.data)
                    neighbor.parent = current_vertex
                    parent_pointers[neighbor.data] = current_vertex.data
        if path_found:
            path = []

            while current_vertex is not None:
                path.append(current_vertex.data)
                current_vertex = current_vertex.parent

            # print(f'parent pointers: {parent_pointers}')
            return path[::-1], len(path) - 1
        # if there is no path from source to destination return -1
        return [], -1


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f'({v.get_id()}, {w.get_id()}, {v.get_edge_weight(w)})')

    print("edges: ", g.get_all_edges())
