
from music21 import *
from utils import *

class Music21Graph():
    
    def __init__(self, path_to_score):

        self.path_to_score = path_to_score
        
        # Load the MusicXML file
        self.score = converter.parse(self.path_to_score)

        # Graph building and storage
        self.graph = dict()
        self.nodes = self.get_nodes()

    def get_nodes(self):
        # Find every note and store it as a new node
        nodes = []
        for part in self.score.parts:
            print("\nPart:", part.partName)
            for measure in part.getElementsByClass('Measure'):
                print("\nMeasure:", measure.number)
                for note_or_chord in measure.notesAndRests:
                    if isinstance(note_or_chord, note.Note):
                        print("Note:", note_or_chord.nameWithOctave)
                    elif isinstance(note_or_chord, chord.Chord):
                        chord_notes = ' '.join(n.nameWithOctave for n in note_or_chord.pitches)
                        print("Chord:", chord_notes)
                    elif isinstance(note_or_chord, note.Rest):
                        print("Rest")

    # Converts an adjacency list representation into tables of nodes, directed and undirected edges
    def convert_graph_to_tables(self):
        nodes = list(self.graph.keys())
        directed_edges = []
        undirected_edges = []

        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                directed_edges.append((node, neighbor))
                if (neighbor, node) not in directed_edges and (node, neighbor) not in undirected_edges:
                    undirected_edges.append((node, neighbor))

        return nodes, directed_edges, undirected_edges
    
if __name__ == "__main__":
    graph = Music21Graph("chopin.mxl")