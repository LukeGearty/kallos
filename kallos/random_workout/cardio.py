import random

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


def high_intensity_training(num_rounds):
    circuit_training = ['Jumping Jacks', 'High Knees', 'Burpees', 'Mountain Climbers', 'Squats', 'Push Ups', 'Russian Twists', 'Jump Squats', 'Lunges', 'Planks']
    first = random.choice(circuit_training)
    second = random.choice(circuit_training)

    while second == first:
        second = random.choice(circuit_training)
    
    third = random.choice(circuit_training)

    while third == second or third == first:
        third = random.choice(circuit_training)
    
    return f"{first}, {second}, {third}, 30 seconds on, 10 seconds off, for {num_rounds} rounds"


##only for low and medium intensity
def generate_cardio_workout(cardio_function, duration_function):
    return f"You are going to do some {cardio_function()} for {duration_function()} minutes today"


## for high intensity
def generate_high_intensity():
    choice = random.choice([1, 2])
    num_rounds = random.choice([3,4,5])
    if choice == 1:
        return high_intensity_training(num_rounds)
    else:
        return f"30 second sprints for {num_rounds} rounds"


def cardio_choice(choice: int):
    if choice == 1:
        return generate_cardio_workout(low_intensity_cardio, low_intensity_duration)
    elif choice == 2:
        return generate_cardio_workout(medium_intensity_cardio, medium_duration)
    else:
        return generate_high_intensity()