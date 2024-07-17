import random


def circuit_training():
    circuit_training = ['Jumping Jacks', 'High Knees', 'Burpees', 'Mountain Climbers', 'Squats', 'Push Ups', 'Russian Twists', 'Jump Squats', 'Lunges', 'Planks']
    first = random.choice(circuit_training)
    second = random.choice(circuit_training)

    while second == first:
        second = random.choice(circuit_training)
    
    third = random.choice(circuit_training)

    while third == second or third == first:
        third = random.choice(circuit_training)
    
    return [first, second, third]

