scores = [0.45, 0.92, 0.88, 0.65, 0.99, 0.71]

filtered_scores = list(filter(lambda score: score > 0.80, scores))

print("Filtered confidence scores (> 0.80):", filtered_scores)
