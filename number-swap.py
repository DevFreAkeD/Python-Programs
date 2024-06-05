# Function to swap two variables
def swap_variables(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2

# Get user input for two variables
var1 = input("Enter the value of variable 1: ")
var2 = input("Enter the value of variable 2: ")

# Display the values before swapping
print(f"Before swapping: Variable 1 = {var1}, Variable 2 = {var2}")

# Swap the variables
var1, var2 = swap_variables(var1, var2)

# Display the values after swapping
print(f"After swapping: Variable 1 = {var1}, Variable 2 = {var2}")
