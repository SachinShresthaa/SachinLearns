def train_model(epochs):
    for i in range(1, epochs + 1):
        print(f"Epoch {i} completed")
    print("Training Finished")

epochs = int(input("Enter numbers of epochs: "))
train_model(epochs)
