import random

# List of India-inspired random events
event_list = [
    "A monkey swings down and snatches your lunch!",
    "A sadhu blesses you with a cryptic riddle.",
    "A peacock struts by, its feathers dazzling in the sun.",
    "A sudden monsoon rain drenches you to the bone.",
    "You hear the distant beat of a dhol drum from a festival.",
    "A cow blocks your path, chewing cud lazily.",
    "A street vendor offers you a spicy vada pav.",
    "The scent of jasmine flowers fills the air."
]

def generate_event():
    return random.choice(event_list)