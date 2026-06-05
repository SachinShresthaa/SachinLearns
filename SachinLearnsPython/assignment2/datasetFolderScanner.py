def count_images(dataset):
    total = 0
    for value in dataset.values():
        if isinstance(value, dict):
            total += count_images(value)
        else:
            total += value
    return total

dataset = {
    "train": {
        "cats": 500,
        "dogs": 450
    },
    "test": {
        "cats": 120,
        "dogs": 130
    }
}

totalImages = count_images(dataset)
print("Total number of images:", totalImages)
