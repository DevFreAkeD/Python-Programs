import random

# Get user input for the range
lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))

# Generate a random integer within the specified range
random_number = random.randint(lower_limit, upper_limit)

print(f"Generated random number: {random_number}")
