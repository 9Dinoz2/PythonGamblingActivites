import random

# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': None  # A's value will be set when dealt
}

# Define suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Deck creation
def create_deck():
    return [(rank, suit) for rank in card_values.keys() for suit in suits]

# Deal a card and reshuffle deck if needed
def deal_card(deck):
    if len(deck) < 10:  # If fewer than 10 cards, reshuffle with a new deck
        print("Deck is low, adding a new deck and reshuffling...")
        deck.extend(create_deck())
        random.shuffle(deck)
    return deck.pop(random.randint(0, len(deck) - 1))

# Ask player to decide Ace value after seeing their hand
def choose_ace_value(other_card):
    while True:
        choice = input(f"You have an Ace and a {other_card}. Do you want the Ace to count as 1 or 11? (1/11): ").strip()
        if choice == '1':
            return 1
        elif choice == '11':
            return 11
        else:
            print("Invalid choice, please enter 1 or 11.")

# Calculate the total hand value
def calculate_total(hand):
    total = 0
    for card in hand:
        rank = card[0]
        if rank == 'A':
            if card_values[rank] is None:  # If Ace value has not been set yet
                card_values[rank] = choose_ace_value(hand[0][0] if hand[0][0] != 'A' else hand[1][0])  # Show the other card
            total += card_values[rank]
        else:
            total += card_values[rank]
    return total

# Display the hand, either hidden or open
def display_hand(name, hand, hidden=False):
    if hidden:
        print(f"{name}'s hand: [{hand[0]}, Hidden]")
    else:
        print(f"{name}'s hand: {hand}, Total: {calculate_total(hand)}")

# BlackJack Game Function
def blackjack():
    deck = create_deck()
    random.shuffle(deck)

    balance = 100
    print("Welcome to Blackjack!")
    print(f"You start with a balance of ${balance}.")

    while balance > 0:
        # Place a bet
        bet = 0
        while bet <= 0 or bet > balance:
            try:
                bet = int(input(f"Place your bet (Balance: ${balance}): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

        original_bet = bet  # Store the original bet for later
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        # Show initial hands
        display_hand("Dealer", dealer_hand, hidden=True)
        display_hand("Player", player_hand)

        # Handle Ace values after seeing player hand
        for card in player_hand:
            if card[0] == 'A' and card_values[card[0]] is None:
                card_values[card[0]] = choose_ace_value(card[1] if card != player_hand[0] else player_hand[1])  # Show the other card

        # Player's turn
        while True:
            move = input("Do you want to [h]it, [s]tand, or [r]aise your bet?: ").lower()

            if move == 'h':
                player_hand.append(deal_card(deck))
                # Handle Ace values after hitting
                for card in player_hand:
                    if card[0] == 'A' and card_values[card[0]] is None:
                        card_values[card[0]] = choose_ace_value(card[1] if card != player_hand[0] else player_hand[1])  # Show the other card
                display_hand("Player", player_hand)  # Show updated player hand with total
                # Check if player's total exceeds 21
                if calculate_total(player_hand) > 21:
                    print("Bust! You've exceeded 21.")
                    break
            
            elif move == 's':
                break

            elif move == 'r':
                # Allow the player to raise their bet
                extra_bet = 0
                while extra_bet <= 0 or bet + extra_bet > balance:
                    try:
                        extra_bet = int(input(f"How much would you like to raise your bet by? (Current bet: ${bet}, Balance: ${balance}): "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                bet += extra_bet
                print(f"Your bet is now ${bet}.")

            else:
                print("Invalid choice, please enter 'h' to hit, 's' to stand, or 'r' to raise your bet.")

        # Dealer's turn
        display_hand("Dealer", dealer_hand, hidden=False)
        while calculate_total(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
            display_hand("Dealer", dealer_hand)

        dealer_total = calculate_total(dealer_hand)
        player_total = calculate_total(player_hand)

        # Determine results
        if player_total > 21:
            print(f"Dealer wins! You lost ${bet}.")
            balance -= bet
        elif dealer_total > 21 or player_total > dealer_total:
            print(f"You win! You won ${bet}.")
            balance += bet
        elif player_total == dealer_total:
            print(f"It's a draw! Your bet is returned.")
        else:
            print(f"Dealer wins! You lost ${bet}.")
            balance -= bet

        # Check if player wants to continue
        if balance <= 0:
            print("You're out of money! Game over.")
            break

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print(f"You're leaving with a balance of ${balance}.")
            break

# Run the game
if __name__ == "__main__":
    blackjack()
