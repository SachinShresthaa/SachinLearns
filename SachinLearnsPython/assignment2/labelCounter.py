def countPositiveLabels(labels):
    count = 0
    for label in labels:
        if label == 1:
            count += 1
    return count

labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
positiveCount = countPositiveLabels(labels)

percentage = (positiveCount / len(labels)) * 100

print("Positive Labels:", positiveCount)
print("Percentage of Positive Labels:", percentage, "%")