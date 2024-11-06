# Function to solve the 0/1 Knapsack problem using dynamic programming
def knapsack_0_1_dp(values, weights, capacity):
    n = len(values)
    
    # Create a 2D DP array where dp[i][w] represents the maximum value
    # that can be attained with the first i items and a knapsack capacity of w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the DP array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option to include the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Can't include the item, so take the value without it
                dp[i][w] = dp[i - 1][w]

    # The maximum value for the given capacity and items
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]   # Values of the items
weights = [20, 30, 40]    # Weights of the items
capacity = 50             # Maximum capacity of the knapsack

max_value = knapsack_0_1_dp(values, weights, capacity)
print(f"Maximum value in the knapsack: {max_value}")
