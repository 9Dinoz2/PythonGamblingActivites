import random
import time

# List of horse names with predefined "Chance to go up" values
horse_data = {
    "Thunder": 30,
    "Lightning": 45,
    "Storm": 50,
    "Blaze": 60,
    "Shadow": 20,
    "Comet": 55,
    "Tornado": 35,
    "Cyclone": 40,
    "Fury": 70,
    "Blizzard": 25,
    "Whirlwind": 65,
    "Hurricane": 55,
    "Nebula": 50,
    "Galaxy": 60,
    "Meteor": 40,
    "Fireball": 30,
    "Phoenix": 45,
    "Rocket": 55,
    "Echo": 50,
    "Racer": 60,
    "Dynamo": 40,
    "Bolt": 45,
    "Sonic": 55,
    "Gale": 30,
    "Tempest": 25,
    "Starlight": 35,
    "Asriel Dreamer": 100,
    "Prowler": 20,
    "Striker": 45,
    "Falcon": 55,
    "Jaguar": 30,
    "Cheetah": 40,
    "Panther": 60,
    "Eagle": 50,
    "Hawk": 35,
    "Vortex": 55,
    "Tsunami": 45,
    "Avalanche": 50,
    "Earthquake": 35,
    "Seismic": 60,
    "Titan": 40,
    "Inferno": 50,
    "Frost": 65,
    "Whisper": 45,
    "Serenade": 50,
    "Harmony": 30,
    "Spirit": 40,
    "Noble": 55,
    "Valor": 60,
    "Majesty": 25,
    "Epic": 35,
    "Challenger": 50,
    "Legend": 55,
    "Brave": 60,
    "Guardian": 30,
    "Quest": 50,
    "Mystic": 45,
    "Wanderer": 55,
    "Knight": 40,
    "Dusk": 60,
    "Dawn": 30,
    "Sunrise": 25,
    "Sunset": 35,
    "Crimson": 45,
    "Ivory": 50,
    "Jade": 40,
    "Amber": 55,
    "Onyx": 60,
    "Quartz": 35,
    "Sapphire": 45,
    "Emerald": 50,
    "Ruby": 60,
    "Topaz": 35,
    "Opal": 50,
    "Diamond": 45,
    "Copper": 40,
    "Steel": 55,
    "Iron": 30,
    "Platinum": 60,
    "Gold": 45,
    "Silver": 50,
    "Bronze": 35,
    "Charcoal": 40,
    "Slate": 30,
    "Coral": 50,
    "Rose": 55,
    "Violet": 45,
    "Clover": 30,
    "Daisy": 50,
    "Fern": 45,
    "Thistle": 30,
    "Maple": 40,
    "Cypress": 55,
    "Willow": 50,
    "Birch": 60,
    "Pine": 45,
    "Cedar": 50,
    "Spruce": 35,
    "Magnolia": 40,
    "Orchid": 30,
    "Lily": 55,
    "Dahlia": 50,
    "Tulip": 60,
    "Sunflower": 45,
    "Buttercup": 35,
    "Petunia": 50,
    "Iris": 40,
    "Hyacinth": 55,
    "Poppy": 45,
    "Lilac": 30,
    "Wisteria": 35,
    "Heather": 50,
    "Aster": 45,
    "Chrysanthemum": 30,
    "Narcissus": 40,
}

# Function to simulate horse racing
def horse_race():
    print("Welcome to the Horse Racing Game!")
    
    # Get number of players
    num_players = 0
    while num_players < 1 or num_players > 4:
        try:
            num_players = int(input("Enter the number of players (1-4): "))
        except ValueError:
            print("Please enter a valid number between 1 and 4.")

    players = []
    for i in range(num_players):
        name = input(f"Enter the name for Player {i + 1}: ")
        players.append({'name': name, 'balance': 100})

    while True:
        # Randomly select a number of horses between 5 and 10
        num_horses = random.randint(5, 10)
        horses = random.sample(list(horse_data.keys()), num_horses)

        print("\nAvailable Horses:")
        for index, horse in enumerate(horses):
            print(f"{index + 1}. {horse}")

        # Players place their bets
        for player in players:
            bet = 0
            while bet <= 0 or bet > player['balance']:
                try:
                    bet = int(input(f"{player['name']}, enter your bet (Balance: ${player['balance']}): "))
                except ValueError:
                    print("Please enter a valid number.")
            
            horse_choice = 0
            while horse_choice < 1 or horse_choice > len(horses):
                try:
                    horse_choice = int(input(f"{player['name']}, pick a horse to bet on (1-{len(horses)}): "))
                    if horse_choice < 1 or horse_choice > len(horses):
                        print("Invalid option, pick another.")
                except ValueError:
                    print("Invalid option, pick another.")

            player['bet'] = bet
            player['horse_choice'] = horse_choice - 1  # Store the index of the chosen horse

        # Simulate the race
        print("\nThe race is on!")

        # Initialize horse positions
        positions = list(range(1, len(horses) + 1))  # Positions from 1 to num_horses
        random.shuffle(positions)  # Shuffle to randomize starting positions
        chances = {horse: horse_data[horse] for horse in horses}  # Store chances

        total_updates = random.randint(5, 15)  # Random number of updates
        special_race = random.random() < 0.001  # 0.1% chance for a special race with 100 updates
        updates = 0

        # Update race positions
        while updates < (100 if special_race else total_updates):
            time.sleep(random.uniform(0.2, 2))  # Random wait time between updates
            
            # Update positions of each horse
            for i in range(len(horses)):
                chance_to_go_up = random.randint(chances[horses[i]] - 5, chances[horses[i]] + 5)  # Chance to go up with some variability
                if i > 0:  # Check if there's a horse ahead
                    if chance_to_go_up > chances[horses[i - 1]]:
                        positions[i], positions[i - 1] = positions[i - 1], positions[i]  # Swap positions

            # Display current positions
            print("\nCurrent Positions:")
            for pos in sorted(positions):
                horse_index = positions.index(pos)
                print(f"{horses[horse_index]}: Position {pos}")

            print("\n\n")  # Two line gap

            # Second-to-last update
            if updates == (total_updates - 2):  
                # Randomly increase "Chance to go up" for a random amount of horses
                num_increased = random.randint(1, len(horses))
                for _ in range(num_increased):
                    horse_to_increase = random.choice(horses)
                    chances[horse_to_increase] += random.randint(5, 20)  # Increase chance by random amount
                    print(f"{horse_to_increase} gets a boost of energy!")

            updates += 1

        # Determine race outcome
        winning_horse_index = positions.index(1)

        # Announce winners and update balances
        for player in players:
            if player['horse_choice'] == winning_horse_index:
                print(f"Congratulations, {player['name']}! Your horse, {horses[player['horse_choice']]}, won!")
                player['balance'] += player['bet']
            else:
                print(f"Sorry, {player['name']}! Your horse, {horses[player['horse_choice']]}, did not win.")
                player['balance'] -= player['bet']

        # Show players' current balances
        for player in players:
            print(f"{player['name']}'s balance is now: ${player['balance']}")

        # Check if any player is out of money
        for player in players:
            if player['balance'] <= 0:
                print(f"{player['name']} is out of money! Game over.")
                return

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            for player in players:
                print(f"{player['name']} is leaving with a balance of ${player['balance']}.")
            break

# Run the game
if __name__ == "__main__":
    horse_race()
