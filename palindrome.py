# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_s = ''.join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]

# Get user input for the string
string_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string_input):
    print(f"{string_input} is a palindrome.")
else:
    print(f"{string_input} is not a palindrome.")
