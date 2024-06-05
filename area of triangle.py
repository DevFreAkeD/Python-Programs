# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Get user input for the base and height of the triangle
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = area_of_triangle(base, height)

# Display the result
print(f"The area of the triangle with base {base} and height {height} is: {area}")
