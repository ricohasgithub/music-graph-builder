
from music21 import *

def print_notes_and_chords(score):
    for part in score.parts:
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