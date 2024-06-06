import cmath

# Get user input for coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Calculate the solutions
solution1 = (-b + discriminant) / (2*a)
solution2 = (-b - discriminant) / (2*a)

# Display the solutions
print(f"Solutions: \n{solution1} \n{solution2}")
