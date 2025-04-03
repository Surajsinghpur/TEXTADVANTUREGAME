import time
import rooms
import events
import save_game

def normalize_direction(action):
    """Convert 'north' to 'go north', etc., for flexibility."""
    directions = ["north", "south", "east", "west"]
    action = action.lower().strip()
    if action in directions:
        return f"go {action}"
    return action

def game_loop():
    print("Welcome to the Quest for the Surya Mani!")
    print("Type 'quit' to exit, 'save' to save, or 'load' to load a game.\n")
    
    # Initial player state
    player = {"location": "village", "inventory": []}
    
    while True:
        # Get current room
        current_room = rooms.get_room(player["location"])
        print(f"\n{current_room['description']}")
        
        # Random event
        event = events.generate_event()
        print(f"Event: {event}")
        
        # Show choices
        print("Choices:", ", ".join(current_room["choices"].keys()))
        action = input("What do you do? ")
        action = normalize_direction(action)  # Handle "north" as "go north"
        
        # Handle special commands
        if action == "quit":
            print("Thanks for playing!")
            break
        elif action == "save":
            save_game.save_game(player)
            print("Game saved!")
            continue
        elif action == "load":
            loaded_player = save_game.load_game()
            if loaded_player:
                player = loaded_player
                print("Game loaded!")
            continue
        
        # Handle room choices
        if action in current_room["choices"]:
            player["location"] = current_room["choices"][action]
            time.sleep(1)  # Dramatic pause
            # Check for winning condition
            if player["location"] == "sun_temple":
                print("\nCongratulations! You’ve reached the Temple of the Sun and claimed the Surya Mani!")
                print("Your name will be sung in legends across the land!")
                break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    game_loop()