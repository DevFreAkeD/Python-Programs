# Function to find the ASCII value of a character
def find_ascii_value(character):
    return ord(character)

# Get user input for the character
character = input("Enter a character: ")

# Ensure the user input is a single character
if len(character) != 1:
    print("Please enter a single character.")
else:
    # Find and display the ASCII value
    ascii_value = find_ascii_value(character)
    print(f"The ASCII value of '{character}' is: {ascii_value}")
