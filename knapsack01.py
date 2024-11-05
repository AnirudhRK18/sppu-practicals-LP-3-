# Define a class to store details of an item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

# Greedy approach for 0/1 Knapsack problem
def knapsack_0_1_greedy(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0  # Total value of items included in the knapsack
    total_weight = 0  # Total weight of items included

    for item in items:
        if total_weight + item.weight <= capacity:
            # If the item fits, take it fully
            total_weight += item.weight
            total_value += item.value
        else:
            # If the item doesn't fit, skip it (no fractions allowed in 0/1 Knapsack)
            continue

    return total_value

# Example usage
items = [
    Item(60, 20),  # Value = 60, Weight = 20
    Item(100, 30), # Value = 100, Weight = 30
    Item(120, 40)  # Value = 120, Weight = 40
]

capacity = 50
max_value = knapsack_0_1_greedy(items, capacity)
print(f"Approximate maximum value in the knapsack: {max_value}")
