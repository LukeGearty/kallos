import random

def medium_intensity_cardio():
    exercises = ['Running']
    return random.choice(exercises)


def duration():
    potential_durations = [30, 45, 60] #in minutes
    return random.choice(potential_durations)