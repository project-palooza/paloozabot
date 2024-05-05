import random

def pick_name():
    """pick a random adjective and noun from provided lists."""
    adjectives = ['distinguished','esteemed','respected','valued','revered','cherished','honored']
    nouns = ['homie','friend','analyst','member']
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"
