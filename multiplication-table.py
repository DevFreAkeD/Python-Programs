# Function to print the multiplication table of a number up to 10
def print_multiplication_table(number):
    print(f"Multiplication Table of {number} up to 10:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Get user input for the number
number = int(input("Enter a number: "))

# Print the multiplication table up to 10
print_multiplication_table(number)
