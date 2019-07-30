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
        self.edge_list = [] # unique edge_list
        self.num_vertices = 0
        self.num_edges = 0
        self.DEFAULT_WEIGHT = 0
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
    def add_edge_modified(self, from_vertex, to_vertex, weight=None):
        
        if from_vertex == to_vertex:
            print(f'You cant add the vertex to itself!')
            return

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise ValueError("One of the vertex doesn't exist!")
        
        # assigning the weight
        if weight is None:
            weight = self.DEFAULT_WEIGHT
        else:
            weight = int(weight)
        
        edge = (from_vertex, to_vertex, weight)
        # handling duplicated edges in input file 
        if edge in self.get_edges():
            raise ValueError("You can't add duplicated edges!")
        
        
        from_vert_obj = self.vert_dict[from_vertex]
        to_vert_obj = self.vert_dict[to_vertex]

        if self.directed: # directed graph
            from_vert_obj.add_neighbor(to_vert_obj, weight)
        else: 
            # connect the edges in both ways
            from_vert_obj.add_neighbor(to_vert_obj, weight)
            to_vert_obj.add_neighbor(from_vert_obj, weight)
        
        
        # add edges to unique edge_list
        
        self.edge_list.append(edge)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return list(self.vert_dict.keys())

    def get_edges(self):
        """Return number of all edges in the graph"""
        edges = []
        for v in self.vert_dict.values():
            for w in v.neighbors:
                edges.append((v.data, w.data, v.get_edge_weight(w)))
        return edges

    

    def find_shortest_path(self, from_vertex, to_vertex):
        """Search for the shortest path from vertex a to b using Breadth first search
        
        Args:
            from_vertex (str) : starting point on the graph
            to_vertex (str) : the distanation or end of the path

        Returns:
            shortest path (tuple): List of vertices in the path and len
                                    Empty list if path does not exist
        """
    
        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise KeyError("One of the given vertices does not exist in graph!")

        # check if you are at the location
        if from_vertex == to_vertex:
            vert_obj = self.vert_dict[from_vertex]
            return ([vert_obj.data], 0)

        # grab the start location from graph
        current_vertex = self.vert_dict[from_vertex]
    
        # initialize the queue, visited nodes set, a dictionary to keep track of parent 
        queue = Queue(maxsize=len(self.get_vertices()))
        seen_vertex = set()
        parent_pointers = {}

        # start the traversal
        queue.put(current_vertex)
        seen_vertex.add(current_vertex.data)

        path = []
        path_found = False
        parent = None
        current_vertex.parent = parent
        # alternative way of storing the references to parent  pointers
        parent_pointers[current_vertex.data] = None

        while not queue.empty():
            # dequeue the front element
            current_vertex = queue.get()
            path.append(current_vertex)

            # check if we are at destination
            if current_vertex.data == to_vertex:
                path_found = True # found the goal 
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

            return (path[::-1], len(path) - 1)
        # if there is no path from source to destination return -1
        return ([], -1)

    def breadth_first_search_traversal(self, from_vertex):
        '''Traversing entire grapgh using breadth first search algorithm.
        The algorithm adapted from: https://en.wikipedia.org/wiki/Breadth-first_search
        
        Args:
            vertex (str): given vertex to find its all neighors 
            

        Returns:
            bfs order (tuple): first item is all vertices in a bfs order
                               second item is levels of other vertices from starting vertex
        '''
        # check if starter node is in the graph
        if from_vertex not in self.vert_dict:
            raise KeyError(f"The vertex {from_vertex}, you entered doesn't exist in graph!")

        # we need a queue, set, and parent_pointer dict
        queue = Queue(maxsize=len(self.get_vertices()))
        visited_nodes = set()
        parent_pointers = {}
        bfs_order = []
        level_reference = {}
        
        # enqueue the starter node, visit and add to the parent_pointer 
        current_vertex = self.vert_dict[from_vertex]
        queue.put(current_vertex)
        visited_nodes.add(current_vertex.data)
        # set the parent node as none 
        parent_pointers[current_vertex.data] = None
        # to store how far from the starter node
        level_reference[current_vertex.data] = 0
        

        # start traversing
        level_counter = 0
        while not queue.empty():
            # dequeue the current node
            current_vertex = queue.get()
            bfs_order.append(current_vertex.data)
            level_counter += 1

            for neighbor in current_vertex.neighbors:
                # check if the neighbor is visited 
                if neighbor.data not in visited_nodes:
                    
                    queue.put(neighbor)
                    visited_nodes.add(neighbor.data)
                    parent_pointers[neighbor.data] = current_vertex.data
                    level_reference[neighbor.data] = level_reference[current_vertex.data] + 1
        
        return (bfs_order, level_reference)

    def n_level_bfs(self, from_vertex, n_level):
        """Find all nth level connections of 
        
        Args:
            vertex (str): given vertex to find its all neighors 
            n_level (int): certain connection level away from vertex

        Returns:
            all nodes (list): all nodes found at the nth level
                              if there is no given level of connections raises value error
        """
        
        vertices = self.breadth_first_search_traversal(from_vertex)[1]
        n_level_connections = []
        max_level = max(vertices.values())
        
        # check if vertex has given depth level of connections
        if n_level > max_level:
            raise ValueError(f"Current vertex has maximum level of {max_level} connections!")
        
        for vertex in vertices:
            if vertices[vertex] == n_level:
                n_level_connections.append(vertex)

        return n_level_connections


def build_graph(graph: Graph, vertices, edges):
        
        # add the vertices
        for vertex in vertices:
            graph.add_vertex(vertex)

        # add the edges
        for edge in edges:
            # unpack the edge, because it could be len of 2 or 3
            print(f"current edge: {edge}")
            graph.add_edge_modified(*edge)

        return graph
