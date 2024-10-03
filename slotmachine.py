import concurrent.futures
import time
import random

stop_loop = False
slotarray = [0, 0, 0]  

def wait_for_enter():
    global stop_loop
    input("Press Enter to stop...\n")
    stop_loop = True

def spin_slots():
    global stop_loop
    
    while not stop_loop:
        # Generate random numbers for each slot
        for j in range(len(slotarray)):
            slotarray[j] = random.randint(0, 9)  # Random number between 0 and 9
        print(f"Slots: {slotarray[0]} {slotarray[1]} {slotarray[2]}")

        time.sleep(0.2)  

    print(f"Final Slots: {slotarray[0]} {slotarray[1]} {slotarray[2]}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Start the input waiting in a separate thread
    future = executor.submit(wait_for_enter)
    
    # Run the slot machine simulation
    spin_slots()

# Check if the slot array shows a winner
if slotarray[0] == slotarray[1] == slotarray[2]:
    print("Winner!")
else:
    print("Loser!")
