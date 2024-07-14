import random


def set_calculator():
    return random.randint(3, 5)


def rep_calculator():
    potential_reps = [8, 10, 12, 15]
    return random.choice(potential_reps)
