import random


def upper_body():
    upper_body_exercises = ['Push Ups', 'Body Weight Rows', 'Pike Push Ups']
    return random.choice(upper_body_exercises)


def lower_body():
    lower_body_exercises = ['Squats', 'Lunges']
    return random.choice(lower_body_exercises)


def core_work():
    core_exercises = ['Sit Ups', 'Knee Raises', 'Dead Bugs']
    return random.choice(core_exercises)
