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

    print("# Vertices: ", len(g.get_vertices()))
    print("# Edges: ", g.num_edges)
    print("The Edge List: ")
    for edge in g.get_edges():
        print(edge)

    # shortest_path = g.find_shortest_path(from_vertex, to_vertex)

    # print("Verticies in shortest path:", *shortest_path[0])
    # print(f"Number of edges in shortest path: {shortest_path[1]}")


if __name__ == "__main__":
    filename = sys.argv[1]
    # from_vertex = sys.argv[2]
    # to_vertex = sys.argv[3]

    data = read_file(filename)
    build_graph(filename)


# TODO:
# 1. consider how to print the graph edges if it is undericted
    # using .get_id() or edge_list property
