import random

# Define card values and suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_values = {rank: index + 2 for index, rank in enumerate(ranks)}

# Create a deck of cards
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

# Deal cards to player and dealer
def deal_cards(deck):
    player_hand = [deck.pop(random.randint(0, len(deck) - 1)) for _ in range(2)]
    dealer_hand = [deck.pop(random.randint(0, len(deck) - 1)) for _ in range(2)]
    return player_hand, dealer_hand

# Calculate the total hand value
def calculate_hand_value(hand, community_cards):
    all_cards = hand + community_cards
    values = sorted([card_values[card[0]] for card in all_cards], reverse=True)
    return values

# Determine the winner
def determine_winner(player_hand, dealer_hand, community_cards):
    player_total = calculate_hand_value(player_hand, community_cards)
    dealer_total = calculate_hand_value(dealer_hand, community_cards)
    
    print(f"Player's best hand: {player_total}")
    print(f"Dealer's best hand: {dealer_total}")

    if player_total > dealer_total:
        return "Player wins!"
    elif dealer_total > player_total:
        return "Dealer wins!"
    else:
        return "It's a draw!"

# Main game function
def texas_holdem():
    print("Welcome to Texas Hold'em!")
    balance = 100
    print(f"You start with a balance of ${balance}.")

    while balance > 0:
        bet = 0
        while bet <= 0 or bet > balance:
            try:
                bet = int(input(f"Enter your bet (Balance: ${balance}): "))
            except ValueError:
                print("Please enter a valid number.")
        
        deck = create_deck()
        random.shuffle(deck)
        player_hand, dealer_hand = deal_cards(deck)

        # Community cards: first three cards (the flop)
        community_cards = [deck.pop(random.randint(0, len(deck) - 1)) for _ in range(3)]
        print(f"Community Cards (Flop): {community_cards}")
        
        # Show player's hand
        print(f"Player's Hand: {player_hand}")

        # Player's turn
        action = input("Do you want to [c]heck or [b]et? ").lower()
        if action == 'b':
            additional_bet = int(input("Enter additional bet: "))
            bet += additional_bet

        # Reveal dealer's hand and the rest of the community cards
        print(f"Dealer's Hand: {dealer_hand}")
        
        # Add turn and river
        community_cards.append(deck.pop(random.randint(0, len(deck) - 1)))  # Turn
        print(f"Community Cards (Turn): {community_cards}")
        community_cards.append(deck.pop(random.randint(0, len(deck) - 1)))  # River
        print(f"Community Cards (River): {community_cards}")

        # Determine the winner
        result = determine_winner(player_hand, dealer_hand, community_cards)
        print(result)

        # Update balance based on the outcome
        if "Player wins" in result:
            balance += bet
        elif "Dealer wins" in result:
            balance -= bet

        print(f"Your balance is now: ${balance}")

        if balance <= 0:
            print("You're out of money! Game over.")
            break

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print(f"You're leaving with a balance of ${balance}.")
            break

# Run the game
if __name__ == "__main__":
    texas_holdem()
