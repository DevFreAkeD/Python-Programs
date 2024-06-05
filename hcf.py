# Function to find the HCF/GCD of two numbers using Euclidean algorithm
def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Get user input for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and display the HCF/GCD
hcf = find_hcf(num1, num2)
print(f"The HCF/GCD of {num1} and {num2} is: {hcf}")
