import random

# Define global variables
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        value += card_values[rank]
        if rank == 'Ace':
            num_aces += 1
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop(0)

# Function to display a hand
def display_hand(hand):
    for card in hand:
        print(f"{card[0]} of {card[1]}")

# Function to check if a hand busts
def is_bust(hand_value):
    return hand_value > 21

# Function to play a round of Blackjack
def play_blackjack():
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print("Player's Hand:")
    display_hand(player_hand)
    print("\nDealer's Hand:")
    print(f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")
    
    # Player's turn
    while True:
        choice = input("\nDo you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
            print("\nPlayer's Hand:")
            display_hand(player_hand)
            if is_bust(calculate_hand_value(player_hand)):
                print("\nPlayer busts! Dealer wins.")
                return
        elif choice == 's':
            break
    
    # Dealer's turn
    print("\nDealer's Hand:")
    display_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        print("\nDealer hits:")
        display_hand(dealer_hand)
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print("\nPlayer's Hand Value:", player_value)
    print("Dealer's Hand Value:", dealer_value)
    
    # Determine the winner
    if is_bust(player_value):
        print("\nDealer wins! Player busts.")
    elif is_bust(dealer_value) or player_value > dealer_value:
        print("\nPlayer wins!")
    elif dealer_value > player_value:
        print("\nDealer wins!")
    else:
        print("\nIt's a tie!")

# Play the game
play_blackjack()
