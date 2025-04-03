import json
import os

SAVE_FILE = "game_data/save_data.json"

def save_game(player):
    # Ensure game_data folder exists
    os.makedirs("game_data", exist_ok=True)
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f)

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No saved game found.")
        return None