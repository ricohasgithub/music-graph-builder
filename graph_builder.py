
from music21 import *
from utils import *

class Music21Graph():
    
    def __init__(self, path_to_score):

        self.path_to_score = path_to_score
        
        # Load the MusicXML file
        self.score = converter.parse(self.path_to_score)

        # Graph building and storage
        self.graph = dict()
        self.nodes, self.notes = self.get_nodes()

        self.print_nodes()

    def get_nodes(self):
        
        # Find every note and store it as a new node
        nodes = []
        notes = []

        note_id = 0
        for part in self.score.parts:
            for measure in part.getElementsByClass('Measure'):
                for note_or_chord in measure.notesAndRests:
                    if isinstance(note_or_chord, note.Note):
                        notes.append((note_or_chord, note_id))
                        nodes.append((note_id,
                                      note_or_chord.nameWithOctave,
                                      measure.number,
                                      note_or_chord.duration,
                                      note_or_chord.beat,
                                      note_or_chord.quarterLength))
                        note_id += 1
                    elif isinstance(note_or_chord, chord.Chord):
                        for individual_note in note_or_chord.pitches:
                            notes.append((note_or_chord, note_id))
                            nodes.append((note_id,
                                        individual_note.nameWithOctave,
                                        measure.number,
                                        note_or_chord.duration,
                                        note_or_chord.beat,
                                        note_or_chord.quarterLength))
                            note_id += 1
                    elif isinstance(note_or_chord, note.Rest):
                        continue
        return nodes, notes

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
    
    def print_nodes(self):
        for node in self.nodes:
            print("Node: ", node[0], "Measure: ", node[2], "Note: ", node[1], "Duration: ", node[4])
    
if __name__ == "__main__":
    graph = Music21Graph("chopin.mxl")