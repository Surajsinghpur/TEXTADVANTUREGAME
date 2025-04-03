# Dictionary of rooms with descriptions and choices
rooms = {
    "village": {
        "description": "You stand in a bustling village in ancient India. The air smells of spices and cow dung. A merchant calls out, selling bangles, while children chase a stray dog. Your quest begins here—to find the lost Surya Mani, the Sun Jewel.",
        "choices": {
            "go north": "jungle",
            "go east": "riverbank"
        }
    },
    "jungle": {
        "description": "A thick jungle surrounds you. Tall bamboo sways in the breeze, and the distant roar of a tiger echoes. A narrow path winds deeper, while a faint chant drifts from the west.",
        "choices": {
            "go south": "village",
            "go west": "ashram",
            "go north": "mountain_path"
        }
    },
    "riverbank": {
        "description": "You reach the banks of a wide river, its waters shimmering under the sun. Fishermen cast nets, singing folk songs. Across the river, you see a faint outline of a town.",
        "choices": {
            "go west": "village",
            "go east": "town"
        }
    },
    "ashram": {
        "description": "A peaceful ashram sits nestled among banyan trees. A sadhu meditates by a small fire, his saffron robes glowing. He murmurs about a hidden temple to the east.",
        "choices": {
            "go east": "jungle",
            "go north": "mountain_path"
        }
    },
    "town": {
        "description": "A lively town buzzes with activity. Traders haggle over silk and turmeric, while a street performer juggles fire. A dusty road leads west, and a bridge heads south.",
        "choices": {
            "go west": "riverbank",
            "go south": "ruins"
        }
    },
    "mountain_path": {
        "description": "You climb a rocky mountain path. The wind howls, and vultures circle overhead. Below, the jungle sprawls, while a cave opening looms to the east.",
        "choices": {
            "go south": "jungle",
            "go east": "cave",
            "go west": "ashram"
        }
    },
    "ruins": {
        "description": "Ancient ruins rise from the earth, covered in vines. Broken statues of gods watch silently. A faint glow pulses from the west, hinting at something sacred.",
        "choices": {
            "go north": "town",
            "go west": "sun_temple"
        }
    },
    "cave": {
        "description": "A dark cave stretches before you. Water drips from stalactites, and bats flutter in the shadows. A narrow passage leads south, back toward the light.",
        "choices": {
            "go west": "mountain_path",
            "go south": "sun_temple"
        }
    },
    "sun_temple": {
        "description": "You step into the grand Temple of the Sun. Golden light floods the chamber, and at its center sits the Surya Mani, a radiant jewel pulsing with power. Your journey ends here.",
        "choices": {}  # No choices; game ends here
    }
}

def get_room(room_name):
    return rooms.get(room_name, rooms["village"])  # Default to village if invalid