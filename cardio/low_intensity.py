import random

def low_intensity_cardio():
    exercises = ['Walking', 'Light Jogging']
    return random.choice(exercises)


def duration():
    potential_durations = [10, 15, 20, 25, 30] # in minutes
    return random.choice(potential_durations)