from datetime import date
import calendar
import random


#formating the date
def format_date():
    today = date.today()
    day = calendar.day_name[today.weekday()]
    month = today.strftime("%B")
    day_of_month = date.today().day
    return f"{day}, {month} {day_of_month}"


#stretching functions
def gentle_stretch():
    stretches = ['Downward Facing Dog', 'Cat Cow', 'Standing Calf Raise', 'Shoulder Rolls', 'Shoulder Reaches']
    return random.choice(stretches)


def intermediate_stretches():
    stretches = ['Standing Forward Fold', 'Lying Forward Fold','Deep Squat', 'Deep Lunges', 'Bridge', 'Supine Spinal Twists', 'Pigeon Pose']
    return random.choice(stretches)


def advanced_stretch():
    stretches = ['Origami Stretch', 'Twisting Pec Stretch', 'Forward Fold', 'Triangle Stretch', 'Heart Opener', 'Lunge with Spinal Twist', 'Piriformis Stretch']
    return random.choice(stretches)


def print_stretches(stretches: list):
    for stretch in stretches:
        print(stretch)
    print("Hold each pose for 30 seconds")


def generate_stretches(stretch_function, count=3):
    stretches = []
    while len(stretches) < count:
        current_stretch = stretch_function()
        while current_stretch in stretches:
            current_stretch = stretch_function()
        stretches.append(current_stretch)
    return stretches


def gentle_stretching():
    stretches = generate_stretches(gentle_stretch)
    print_stretches(stretches)


def challenging_stretching():
    stretches = generate_stretches(intermediate_stretches)
    print_stretches(stretches)



def advanced_stretching():
    stretches = generate_stretches(advanced_stretch)
    print_stretches(stretches)



def stretch_choice():
    date = format_date()
    print(f"Welcome to the stretching session of {date}")
    print("Do you want this stretching to be (1) Gentle, (2) Challenging, (3) Intense?")
    choice = 0
    while choice not in [1, 2, 3]:
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                print("Please select one of the following options: ")
                print("1. Gentle")
                print("2. Challenging")
                print("3. Intense")
                choice = int(input())
            else:
                break
        except ValueError:
            print("Please Enter an integer as your selection")
    
    if choice == 1:
        gentle_stretching()
    elif choice == 2:
        challenging_stretching()
    elif choice == 3:
        advanced_stretching()


#strength training functions

def set_calculator():
    return random.randint(3, 5)


def rep_calculator():
    potential_reps = [8, 10, 12, 15]
    return random.choice(potential_reps)


def beginner_upper_body():
    upper_body_exercises = ['Push Ups', 'Body Weight Rows', 'Pike Push Ups']
    return random.choice(upper_body_exercises)


def beginner_lower_body():
    lower_body_exercises = ['Squats', 'Lunges']
    return random.choice(lower_body_exercises)


def beginner_core_work():
    core_exercises = ['Sit Ups', 'Knee Raises', 'Dead Bugs']
    return random.choice(core_exercises)


def intermediate_upper_body():
    upper_exercise_list = ['Diamond Push Ups', 'Dips', 'Pull Ups']
    return random.choice(upper_exercise_list)


def intermediate_lower_body():
    lower_exercise_list = ['Pistol Squats']
    return random.choice(lower_exercise_list)


def intermediate_core():
    core_exercise_list = ['Leg Raises']
    return random.choice(core_exercise_list)


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


def print_workout(date, upper, lower, core):
    print(date)
    print(f"{upper} :  {set_calculator()} x {rep_calculator()}")
    print(f"{lower} :  {set_calculator()} x {rep_calculator()}")
    print(f"{core} :  {set_calculator()} x {rep_calculator()}")


def beginner_strength(date):
    upper = beginner_upper_body()
    lower = beginner_lower_body()
    core = beginner_core_work()
    print_workout(date, upper,lower,core)
    

def intermediate_strength(date):
    upper = intermediate_upper_body()
    lower = intermediate_lower_body()
    core = intermediate_core()
    print_workout(date, upper,lower,core)


def advanced_strength(date):
    upper = advanced_upper_body()
    lower = advanced_lower_body()
    core = advanced_core_work()
    print_workout(date, upper,lower,core)



def strength_choice():
    date = format_date()
    print(f"Welcome to the workout of {date}")
    print("Are you more of a beginner (1), intermediate (2), or advanced (3)?")
    choice = 0
    while choice not in [1, 2, 3]:
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                print("Please select one of the following options")
                print("1: Beginner")
                print("2: Intermediate")
                print("3: Advanced")
                choice = int(input())
            else:
                break
        except ValueError:
            print("Please Enter an integer as your selection")

    if choice == 1:
        beginner_strength(date)
    elif choice == 2:
        intermediate_strength(date)
    elif choice == 3:
        advanced_strength(date)



#cardio functions
def low_intensity_cardio():
    exercises = ['Walking', 'Light Jogging']
    return random.choice(exercises)


def low_intensity_duration():
    potential_durations = [10, 15, 20, 25, 30] # in minutes
    return random.choice(potential_durations)


def medium_intensity_cardio():
    exercises = ['Running']
    return random.choice(exercises)


def medium_duration():
    potential_durations = [30, 45, 60] #in minutes
    return random.choice(potential_durations)


def high_intensity_training():
    circuit_training = ['Jumping Jacks', 'High Knees', 'Burpees', 'Mountain Climbers', 'Squats', 'Push Ups', 'Russian Twists', 'Jump Squats', 'Lunges', 'Planks']
    first = random.choice(circuit_training)
    second = random.choice(circuit_training)

    while second == first:
        second = random.choice(circuit_training)
    
    third = random.choice(circuit_training)

    while third == second or third == first:
        third = random.choice(circuit_training)
    
    return [first, second, third]


def print_cardio_workout(date, exercise, duration):
    print(date)
    print(f"You are going to do some {exercise} for {duration} minutes today")



def low_intensity(date):
    exercise = low_intensity_cardio()
    duration = low_intensity_duration()
    print_cardio_workout(date, exercise, duration)


def medium_intensity(date):
    exercise = medium_intensity_cardio()
    duration = medium_duration()
    print_cardio_workout(date, exercise, duration)


def high_intensity(date):
    choice = random.choice([1, 2])
    num_rounds = random.choice([3,4,5])
    if choice == 1:
        workout = high_intensity_training()
        print(date)
        for exercises in workout:
            print(exercises)
        print(f"30 seconds on, 10 second break for {num_rounds} rounds")
    else:
        print(date)
        print(f"30 second sprints for {num_rounds} rounds")



def cardio_choice():
    date = format_date()
    choice = 0
    print(f"Welcome to the cardio workout of {date}")
    print("What is the level of intensity you're looking for?")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    while choice not in [1, 2, 3]:
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                print("Please select from one of the following: ")
                print("1. Low")
                print("2. Medium")
                print("3. High")
            else:
                break
        except ValueError:
            print("Please enter an integer as your selection")
    

    if choice == 1:
        low_intensity(date)
    elif choice == 2:
        medium_intensity(date)
    elif choice == 3:
        high_intensity(date)
