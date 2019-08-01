import sys
from Graphs.graph import Graph, Vertex, build_graph
from Graphs.read_file import read_file


def main(filename):

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "==============================="

    from_vertex = "1"
    to_vertex = "4"

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

    print(f'{seperator}DFS order traversal{seperator}')
    print((graph.dfs_recursive(from_vertex)))

    print(f'{seperator}DFS find path{seperator}')
    path = (graph.dfs_paths(from_vertex, to_vertex, set()))
    print(f"{bool(path)}")
    print(path[::-1])


if __name__ == "__main__":
    root_file = 'Graphs/'
    filename = root_file + sys.argv[1]
    main(filename)
