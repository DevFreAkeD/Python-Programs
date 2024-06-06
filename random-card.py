import random

# Function to generate a random card from a deck of cards
def select_random_card():
    # Define the suits and ranks of the cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Choose a random suit and rank
    random_suit = random.choice(suits)
    random_rank = random.choice(ranks)

    # Return the randomly chosen card
    return f"{random_rank} of {random_suit}"

# Generate and print a random card
random_card = select_random_card()
print("Randomly chosen card:", random_card)
