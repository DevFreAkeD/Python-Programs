# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get user input for the number
number = int(input("Enter a number: "))

# Check if the number is odd or even
result = check_odd_even(number)

# Display the result
print(f"The number {number} is {result}.")
