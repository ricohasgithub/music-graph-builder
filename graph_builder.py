
from music21 import *

class Music21Graph():
    
    def __init__(self, path_to_score):

        self.path_to_score = path_to_score
        
        # Load the MusicXML file
        self.score = converter.parse(self.path_to_score)

    # Converts an adjacency list representation into tables of nodes, directed and undirected edges
    def convert_graph_to_tables(self, graph):
        nodes = list(graph.keys())
        directed_edges = []
        undirected_edges = []

        for node, neighbors in graph.items():
            for neighbor in neighbors:
                directed_edges.append((node, neighbor))
                if (neighbor, node) not in directed_edges and (node, neighbor) not in undirected_edges:
                    undirected_edges.append((node, neighbor))

        return nodes, directed_edges, undirected_edges