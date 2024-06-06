# Function to count the number of vowels in a word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count

# Get user input for the word
word = input("Enter a word: ")

# Count and display the number of vowels
num_vowels = count_vowels(word)
print(f"The number of vowels in '{word}' is: {num_vowels}")
