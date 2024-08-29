import random


def intermediate_upper_body():
    upper_exercise_list = ['Diamond Push Ups', 'Dips', 'Pull Ups']
    return random.choice(upper_exercise_list)


def intermediate_lower_body():
    lower_exercise_list = ['Pistol Squats']
    return random.choice(lower_exercise_list)


def intermediate_core():
    core_exercise_list = ['Leg Raises']
    return random.choice(core_exercise_list)
