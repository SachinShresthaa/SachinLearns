scores = [0.45, 0.92, 0.88, 0.65, 0.99, 0.71]

filteredScores = list(filter(lambda score: score > 0.80, scores))

print("Filtered confidence scores:", filteredScores)
