#ML pipeline as dunctions
def load_data(filepath):
    """Load dataset from file."""
    data = []
    with open (filepath)as f:
        for line in f:
            data.append(line.strip().split(","))
    return data

def normalise(values):
    """Min-max noralisation - standart ML step>"""
    mn, mx = min (values), max(values)
    return [(v-mn)/(mx-mn) for v in values]

def accuracy(prediction, labels):
    """Compute classification accuracy."""
    correct = sum(p==l for p, l in zip(prediction,labels))
    return round (correct/len(labels)*100,2)