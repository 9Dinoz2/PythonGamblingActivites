import concurrent.futures
import time
import random

# Game settings
cost_to_play = 10
initial_balance = 100

# Reward combinations
reward_combinations = {
    "0 0 0": "Jackpot! You win $100!",
    "1 1 1": "You win $50!",
    "2 2 2": "You win $20!",
    "0 1 2": "You win $10!",
    "3 3 3": "You win $15!",
    "4 4 4": "You win $25!",
    "5 5 5": "You win $30!",
    "6 6 6": "You win $35!",
    "7 7 7": "You win $40!",
    "8 8 8": "You win $45!",
    "9 9 9": "You win $10!",
    "0 0 1": "You win $5!",
    "0 1 1": "You win $5!",
    "1 1 0": "You win $5!",
}

def wait_for_enter(prompt):
    input(prompt)

def spin_slots():
    global stop_loop
    while not stop_loop:
        # Generate random numbers for each slot
        for j in range(len(slotarray)):
            slotarray[j] = random.randint(0, 9)  # Random number between 0 and 9
        print(f"Slots: {slotarray[0]} {slotarray[1]} {slotarray[2]}")
        time.sleep(0.2)

    print(f"Final Slots: {slotarray[0]} {slotarray[1]} {slotarray[2]}")

# Main game loop
balance = initial_balance
first_spin = True  # Track if it's the first spin
while balance >= cost_to_play:
    # Display current balance and cost to play
    print(f"\nYou have ${balance}. It costs ${cost_to_play} to play.")
    
    # On the first spin, display the jackpot information and rewards
    if first_spin:
        print("You need a 0 0 0 to win the jackpot! Press Enter to start spinning!")
        print("Possible combinations and rewards:")
        for combination, reward in reward_combinations.items():
            print(f" - {combination}: {reward}")
        first_spin = False  # Set to False after first display

    # Deduct the cost to play
    balance -= cost_to_play

    slotarray = [0, 0, 0]  # Reset slot array for each game

    # Wait for the player to start the spinning
    wait_for_enter("Press Enter to start spinning...")

    stop_loop = False  # Reset stop loop for the spin

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Start the spinning in a separate thread
        future = executor.submit(spin_slots)

        # Wait for the player to stop the spinning
        wait_for_enter("Press Enter to stop spinning...")

        # Stop the spinning
        stop_loop = True

    # Check if the slot array shows a winner
    result = f"{slotarray[0]} {slotarray[1]} {slotarray[2]}"
    if result in reward_combinations:
        print(reward_combinations[result])
        # Optional: Add winnings to balance here
        if result == "0 0 0":
            balance += 100  # Example: Jackpot
        else:
            balance += 10  # Example: Small win
    else:
        print("Loser!")

# Game over message
print("You're out of money! Game over.")
