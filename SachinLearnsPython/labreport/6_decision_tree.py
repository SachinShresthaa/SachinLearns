# Decision Tree (ID3) without using any external library
import math
from collections import Counter

ATTRIBUTES = ['Outlook', 'Temperature', 'Humidity', 'Wind']
TARGET = 'PlayTennis'

DATASET = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rainy', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rainy', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
]


def entropy(data):
    total = len(data)
    counts = Counter(row[TARGET] for row in data)

    result = 0
    for count in counts.values():
        probability = count / total
        result -= probability * math.log2(probability)

    return result


def split_by_attribute(data, attribute):
    groups = {}
    for row in data:
        groups.setdefault(row[attribute], []).append(row)
    return groups


def information_gain(data, attribute):
    total_entropy = entropy(data)

    weighted_entropy = 0
    for group in split_by_attribute(data, attribute).values():
        weighted_entropy += (len(group) / len(data)) * entropy(group)

    return total_entropy - weighted_entropy


def majority_label(data):
    return Counter(row[TARGET] for row in data).most_common(1)[0][0]


def build_tree(data, attributes):
    labels = [row[TARGET] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not attributes:
        return majority_label(data)

    gains = {attr: information_gain(data, attr) for attr in attributes}
    best_attribute = max(gains, key=gains.get)

    tree = {best_attribute: {}}
    remaining_attributes = [a for a in attributes if a != best_attribute]

    for value, subset in split_by_attribute(data, best_attribute).items():
        tree[best_attribute][value] = build_tree(subset, remaining_attributes)

    return tree


def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "-> " + tree)
        return

    attribute = next(iter(tree))
    for value, subtree in tree[attribute].items():
        print(f"{indent}{attribute} = {value}")
        print_tree(subtree, indent + "  ")


def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    attribute = next(iter(tree))
    branch = tree[attribute].get(sample.get(attribute))

    if branch is None:
        return None

    return predict(branch, sample)


if __name__ == "__main__":
    print("Decision Tree")
    print("----------------")
    print("Entropy of dataset:", entropy(DATASET))
    print()

    tree = build_tree(DATASET, ATTRIBUTES)
    print_tree(tree)

    sample = {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'}
    print(f"\nPrediction for {sample}: {predict(tree, sample)}")
