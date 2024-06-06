# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main function to run the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("\nEnter choice (1/2/3/4): ")

        # Check if choice is one of the valid options
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

            # Ask if the user wants another calculation
            next_calculation = input("\nDo you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input. Please enter a valid choice.")

# Run the calculator
calculator()
