
# Converts an adjacency list representation into tables of nodes, directed and undirected edges
def convert_to_tables(graph):
    nodes = list(graph.keys())
    directed_edges = []
    undirected_edges = []

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            directed_edges.append((node, neighbor))
            if (neighbor, node) not in directed_edges and (node, neighbor) not in undirected_edges:
                undirected_edges.append((node, neighbor))

    return nodes, directed_edges, undirected_edges