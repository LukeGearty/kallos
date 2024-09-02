import random
#reps and set calculator

def reps_set_calculator():
    return random.randint(3, 5)


def rep_calculator():
    potential_reps = [8, 10, 12, 15]
    return random.choice(potential_reps)


#beginner workouts
def beginner_upper_body():
    upper_body_exercises = ['Push Ups', 'Body Weight Rows', 'Pike Push Ups']
    return random.choice(upper_body_exercises)


def beginner_lower_body():
    lower_body_exercises = ['Squats', 'Lunges']
    return random.choice(lower_body_exercises)


def beginner_core_work():
    core_exercises = ['Sit Ups', 'Knee Raises', 'Dead Bugs']
    return random.choice(core_exercises)


#intermediate workout
def intermediate_upper_body():
    upper_exercise_list = ['Diamond Push Ups', 'Dips', 'Pull Ups']
    return random.choice(upper_exercise_list)


def intermediate_lower_body():
    lower_exercise_list = ['Pistol Squats']
    return random.choice(lower_exercise_list)


def intermediate_core():
    core_exercise_list = ['Leg Raises']
    return random.choice(core_exercise_list)


#advanced
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
