import sys
from graph import Graph, Vertex, build_graph
from read_file import read_file


def main(filename):

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "==============================="
    

    from_vertex = "2"
    to_vertex = "7"
    
    # grab the edges and vertices from graph object
    g_edges = graph.edge_list
    g_vertices = graph.get_vertices()

    
    print(f'{seperator}Start{seperator}')

    print(f'Vertices: {g_vertices}')
    print(f'Number of Edges: {len(g_edges)}')
    print("The Edge List:")
    for edge in g_edges:
        print(edge)

    print(f'{seperator}BFS order{seperator}')
    bfs_order = graph.breadth_first_search_traversal(from_vertex)
    print(bfs_order[0])

    print(f'{seperator}Shortest Path{seperator}')
    shortest_path = graph.find_shortest_path(from_vertex, to_vertex)
    print(f"Verticies in shortest path: {shortest_path[0]}")
    print(f"Number of edges in shortest path: {shortest_path[1]}")

    print(f'{seperator}N level connections{seperator}')
    print(graph.n_level_bfs(from_vertex, 1))

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
    
# TODO:
# 1. consider how to print the graph edges if it is undericted
    # using .get_id() or edge_list property

# store the weights int