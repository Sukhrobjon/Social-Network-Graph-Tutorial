import sys
from graph import Graph, Vertex, build_graph
from read_file import read_file


# def read_file(path):
#     """Read the txt file containg graph information and return them
#     in a list
#     """
#     with open(path, 'r') as f:
#         data = f.read().split('\n')
#     return data


# def build_graph(filename):
#     """Build a graph from given information"""

#     g = Graph()

#     data = read_file(filename)
#     # second line in the txt file is the vertices
#     vertices_list = data[1].split(',')
#     # add vertices
#     for vertex in vertices_list:
#         g.add_vertex(vertex)

#     # from third line in the data file all are the edges
#     edges = []
#     for edge in data[2:]:
#         # remove the parentheses and split by comma
#         # think about how to add 0 if weight not given
#         edge = tuple(edge.strip("()").split(','))
#         edges.append(edge)

#     # add edges
#     for edge in edges:
#         # unpack the edge tuple
#         g.add_edge(*edge)

    
#     return g, g.get_vertices(), g.get_edges()

def main(filename):

    graph, vertices, edges = read_file(filename)
    build_graph(graph, vertices, edges)

    seperator = "==============================="
    

    from_vertex = "1"
    to_vertex = "5"
    
    # grab the edges and vertices from graph object
    g_edges = graph.get_edges()
    g_vertices = graph.get_vertices()

    
    print(f'{seperator}Start{seperator}')

    print(f'Vertices: {g_vertices}')
    print(f'Number of Edges: {len(g_edges)}')
    print("The Edge List:")
    for edge in edges:
        print(edge)

    print(f'{seperator}BFS order{seperator}')
    bfs_order = graph.breadth_first_search_traversal(from_vertex)
    print(bfs_order[0])

    print(f'{seperator}Shortest Path{seperator}')
    shortest_path = graph.find_shortest_path(from_vertex, to_vertex)
    print(f"Verticies in shortest path: {shortest_path[0]}")
    print(f"Number of edges in shortest path: {shortest_path[1]}")

    print(f'{seperator}N level connections{seperator}')
    print(graph.n_level_bfs(from_vertex, 3))

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
    
# TODO:
# 1. consider how to print the graph edges if it is undericted
    # using .get_id() or edge_list property
