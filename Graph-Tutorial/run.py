from graph import Graph, Vertex

if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph(directed=False)

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
    print("Verticies:", list(g.get_vertices()))
    print("# Edges: ", g.num_edges)
    # Print edges
    print("The edges are: ")
    for edge in g.edge_list:
        print(f'({edge[0]}, {edge[1]}, {edge[0]})')
    
    # for v in g:
    #     for w in v.get_neighbors():
    #         print(f'({v.get_id()}, {w.get_id()}, {v.get_edge_weight(w)})')

    



# TODO:
# 1. consider how to print the graph edges if it is undericted
    # using .get_id() or edge_list property
