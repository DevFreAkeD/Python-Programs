# Function to find the sum of natural numbers up to n
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

# Get user input for the value of n
n = int(input("Enter a positive integer (n): "))

# Check if n is a positive integer
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Calculate and display the sum of natural numbers up to n
    result = sum_of_natural_numbers(n)
    print(f"The sum of natural numbers up to {n} is: {result}")
