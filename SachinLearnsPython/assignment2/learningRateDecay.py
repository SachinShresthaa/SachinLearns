def learning_rate_decay(current_rate, n):
    if n <= 0:
        return current_rate
    return learning_rate_decay(current_rate * 0.9, n - 1)

initialRate = float(input("Enter initial learning rate: "))
iterations = int(input("Enter number of iterations: "))

if iterations > 900:
    print("Please enter a smaller number of iterations (900 max) -- this uses recursion, which has a call-depth limit.")
else:
    finalRate = learning_rate_decay(initialRate, iterations)
    print(f"Final learning rate after {iterations} iterations: {finalRate:.6f}")
