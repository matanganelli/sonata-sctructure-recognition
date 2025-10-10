from music21 import converter, note, chord, interval

print("🚀 Iniciando extração de notas...")

# Carregar o arquivo MIDI
score = converter.parse('/Users/mariatanganelli/sonata-sctructure-recognition/data/midi/dussek_sonata3.mid')

# Extrair notas e acordes
sequence = []

for element in score.flatten().notes:
    if isinstance(element, note.Note):
        sequence.append({
            'type': 'note',
            'name': element.nameWithOctave,
            'duration': element.quarterLength
        })
    elif isinstance(element, chord.Chord):
        chord_name = '.'.join(n.nameWithOctave for n in element.notes)
        sequence.append({
            'type': 'chord',
            'name': chord_name,
            'duration': element.quarterLength
        })

# Calcular intervalos entre notas consecutivas
intervals = []

for i in range(len(sequence)-1):
    current = sequence[i]
    next_ = sequence[i+1]
    if current['type'] == 'note' and next_['type'] == 'note':
        n1 = note.Note(current['name'])
        n2 = note.Note(next_['name'])
        iv = interval.Interval(n1, n2)
        intervals.append(iv.name)

print("✅ Extração concluída com sucesso!")
print(f"Total de eventos: {len(sequence)}")
print("Primeiras notas extraídas:")
for e in sequence[:10]:
    print(e)

print("\nIntervalos entre notas consecutivas:")
print(intervals[:20])

print("✅ Extração concluída!")
