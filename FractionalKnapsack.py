# Define a class to store details of an item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    # Calculate value-to-weight ratio
    def value_to_weight_ratio(self):
        return self.value / self.weight

# Function to calculate maximum value in the knapsack
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value_to_weight_ratio(), reverse=True)

    total_value = 0  # Total value in the knapsack
    for item in items:
        if capacity >= item.weight:
            # Take the entire item if it fits
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item that fits
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is now full
            break

    return total_value

# Example usage
items = [
    Item(60, 10),  # Value = 60, Weight = 10
    Item(100, 20), # Value = 100, Weight = 20
    Item(120, 30)  # Value = 120, Weight = 30
]

capacity = 50
max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in the knapsack: {max_value}")
