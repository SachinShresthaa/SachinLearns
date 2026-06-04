def learning_rate_decay(current_rate, n):
    if n == 0:
        return current_rate
    return learning_rate_decay(current_rate * 0.9, n - 1)

initial_rate = float(input("Enter initial learning rate: "))
iterations = int(input("Enter number of iterations: "))

final_rate = learning_rate_decay(initial_rate, iterations)
print(f"Final learning rate after {iterations} iterations: {final_rate:.6f}")
