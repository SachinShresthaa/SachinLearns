def calculate_cost(n):
    if n == 1:
        return 1
    return calculate_cost(n - 1) + n ** 2

layers = int(input("Enter number of layers: "))
total_cost = calculate_cost(layers)
print(f"Total computational cost for {layers} layers: {total_cost}")
