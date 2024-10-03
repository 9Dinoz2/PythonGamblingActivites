import random

# Constants for Yahtzee scoring
YAHTZEE_SCORE = 50
UPPER_SECTION_BONUS = 35

# Function to roll dice
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# Function to calculate scores for various categories
def calculate_scores(dice):
    score_card = {
        "Ones": sum(d for d in dice if d == 1),
        "Twos": sum(d for d in dice if d == 2),
        "Threes": sum(d for d in dice if d == 3),
        "Fours": sum(d for d in dice if d == 4),
        "Fives": sum(d for d in dice if d == 5),
        "Sixes": sum(d for d in dice if d == 6),
        "Three of a Kind": 0,
        "Four of a Kind": 0,
        "Full House": 0,
        "Small Straight": 0,
        "Large Straight": 0,
        "Yahtzee": 0,
        "Chance": sum(dice),
    }

    # Check for Three of a Kind and Four of a Kind
    for number in range(1, 7):
        count = dice.count(number)
        if count >= 3:
            score_card["Three of a Kind"] = max(score_card["Three of a Kind"], sum(dice))
        if count >= 4:
            score_card["Four of a Kind"] = max(score_card["Four of a Kind"], sum(dice))
    
    # Check for Full House
    if 2 in [dice.count(num) for num in set(dice)] and 3 in [dice.count(num) for num in set(dice)]:
        score_card["Full House"] = 25

    # Check for Straights
    unique_dice = set(dice)
    if len(unique_dice) >= 4:
        if {1, 2, 3, 4} <= unique_dice or {2, 3, 4, 5} <= unique_dice or {3, 4, 5, 6} <= unique_dice:
            score_card["Small Straight"] = 30
    if len(unique_dice) == 5:
        if {1, 2, 3, 4, 5} <= unique_dice or {2, 3, 4, 5, 6} <= unique_dice:
            score_card["Large Straight"] = 40

    # Check for Yahtzee
    if any(dice.count(num) == 5 for num in set(dice)):
        score_card["Yahtzee"] = YAHTZEE_SCORE

    return score_card

# Function to allow players to choose which dice to keep
def choose_dice_to_keep(dice):
    while True:
        keep = input(f"Choose which dice to keep (e.g., '1 2' to keep the first and second die) or press enter to keep none: ").strip()
        if keep == "":
            return []  # Keep none
        try:
            keep_indices = list(map(int, keep.split()))
            if all(1 <= idx <= 5 for idx in keep_indices):
                return [dice[idx - 1] for idx in keep_indices]
            else:
                print("Invalid input. Please enter numbers between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Main game function
def yahtzee():
    print("Welcome to Yahtzee!")

    # Get number of players
    num_players = 0
    while num_players < 2 or num_players > 4:
        try:
            num_players = int(input("Enter number of players (2-4): "))
        except ValueError:
            print("Please enter a valid number.")

    # Get player names
    players = []
    scores = {f"Player {i + 1}": {"name": input(f"Enter name for Player {i + 1}: "), "score": 0, "balance": 100} for i in range(num_players)}

    # Game loop for 13 rounds (Yahtzee rounds)
    for round_number in range(1, 14):
        for player_key in scores.keys():
            player = scores[player_key]
            print(f"\n{player['name']}'s turn (Balance: ${player['balance']})")
            bet = 0
            while bet <= 0 or bet > player['balance']:
                try:
                    bet = int(input(f"Place your bet (Balance: ${player['balance']}): "))
                except ValueError:
                    print("Please enter a valid number.")

            # First roll
            dice = roll_dice()
            print(f"You rolled: {dice}")

            # Allow up to 2 re-rolls
            re_rolls = 2
            kept_dice = []
            for _ in range(3):  # Up to 3 rolls
                if _ > 0:  # Not the first roll
                    # Allow players to choose which dice to keep
                    kept_dice = choose_dice_to_keep(dice)
                    dice = kept_dice + roll_dice()[:5 - len(kept_dice)]
                    print(f"You rolled: {dice}")

                # Check if player wants to re-roll
                if _ < 2:  # Only allow re-rolls for the first two rolls
                    if kept_dice:
                        if input("Do you want to re-roll the remaining dice? (y/n): ").lower() != 'y':
                            break
                    else:
                        if input("Do you want to re-roll all the dice? (y/n): ").lower() != 'y':
                            break
            
            # Calculate scores based on the rolled dice
            score_card = calculate_scores(dice)
            print("Score Card:")
            for category, score in score_card.items():
                print(f"{category}: {score}")

            # Choose a category to score in
            category = ""
            while category not in score_card or score_card[category] == 0:
                category = input(f"Choose a category to score in: {', '.join(score_card.keys())}: ").strip()
                if category not in score_card:
                    print("Invalid category. Please choose again.")
                elif score_card[category] == 0:
                    print("Category already scored. Please choose another.")

            player['score'] += score_card[category]
            player['balance'] += bet  # Player earns their bet back
            print(f"{player['name']} scores {score_card[category]} in {category}!")

            # Offer to raise after scoring
            raise_bet = input("Do you want to raise your bet? (y/n): ").lower()
            if raise_bet == 'y':
                additional_bet = 0
                while additional_bet <= 0 or additional_bet > player['balance']:
                    try:
                        additional_bet = int(input(f"How much would you like to raise your bet by? (Current balance: ${player['balance']}): "))
                    except ValueError:
                        print("Please enter a valid number.")
                player['balance'] -= additional_bet  # Deduct the raised amount

    # Determine the winner
    winner = max(scores.values(), key=lambda x: x['score'])
    print(f"\nGame Over! {winner['name']} wins with a score of {winner['score']} and a balance of ${winner['balance']}!")

# Run the game
if __name__ == "__main__":
    yahtzee()
