# Get user input for the base and exponent
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Compute and display the result using pow() function
result = pow(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
