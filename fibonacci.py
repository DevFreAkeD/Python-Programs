# Function to generate Fibonacci series
def fibonacci_series(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

# Get user input for the number of terms
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate and print the Fibonacci series
result = fibonacci_series(num_terms)
print(f"Fibonacci series up to {num_terms} terms: {result}")
