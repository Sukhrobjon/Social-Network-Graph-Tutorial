import sys
from graph import Graph


def read_file(path):
    """Read the txt file containg graph information and return them
    in a list
    """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def build_graph(filename):
    """Build a graph from given information"""

    g = Graph()

    data = read_file(filename)
    # second line in the txt file is the vertices
    vertices_list = data[1].split(',')
    # add vertices
    for vertex in vertices_list:
        g.add_vertex(vertex)

    # from third line in the data file all are the edges
    edges = []
    for edge in data[2:]:
        # remove the parentheses and split by comma
        # think about how to add 0 if weight not given
        edge = tuple(edge.strip("()").split(','))
        edges.append(edge)

    # add edges
    for edge in edges:
        # unpack the edge tuple
        g.add_edge(*edge)

    
    return g, g.get_vertices(), g.get_edges()

if __name__ == "__main__":
    
    seperator = "==============================="
    filename = sys.argv[1]
    
    from_vertex = "Sukhrob"
    to_vertex = "A"

    data = read_file(filename)
    g, vertices, edges = build_graph(filename)
    print(f'{seperator}Start{seperator}')
    
    print("# Vertices: ", list(vertices))
    print("# Edges: ", len(edges))
    print("The Edge List: ")
    for edge in edges:
        print(edge)
    
    print(f'{seperator}BFS order{seperator}')
    bfs_order = g.breadth_first_search_traversal(from_vertex) 
    print(bfs_order[0])
    
    print(f'{seperator}Shortest Path{seperator}', '\n')
    
    print(g.find_shortest_path(from_vertex, to_vertex))
    
    print(f'{seperator}N level connections{seperator}')
    print(g.n_level_bfs(from_vertex, 3))
# TODO:
# 1. consider how to print the graph edges if it is undericted
    # using .get_id() or edge_list property
