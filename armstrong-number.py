# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number

# Get user input for the number
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
