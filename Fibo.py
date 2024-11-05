# Define the number of terms (replace input with a fixed value)
n_terms = 10  # You can change this number to however many terms you want

# Function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Display the Fibonacci series
print(f"Fibonacci series up to {n_terms} terms: {fibonacci_series(n_terms)}")


# recursive


# Recursive function to get the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to generate Fibonacci series up to n terms
def fibonacci_series(n_terms):
    series = [fibonacci(i) for i in range(n_terms)]
    return series

# Example usage
n_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci series up to {n_terms} terms: {fibonacci_series(n_terms)}")


