import random


def advanced_upper_body():
    upper_exercise_list = ['Muscle Ups', 'Handstand Push Ups', 
                           'Front Levers', 'Back Levers']
    return random.choice(upper_exercise_list)


def advanced_lower_body():
    lower_exercise_list = ['Nordic Curls', 'Sissy Squats']
    return random.choice(lower_exercise_list)


def advanced_core_work():
    advanced_core_list = ['V Sits', 'Human Flag', 'Dragon Flag']
    return random.choice(advanced_core_list)