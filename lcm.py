# Function to calculate the Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the Least Common Multiple (LCM)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the LCM
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
