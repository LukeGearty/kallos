import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from format_date import format_date
import low_intensity as low
import med_intensity as med
import high_intensity as high


def print_workout(date, exercise, duration):
    print(date)
    print(f"You are going to do some {exercise} for {duration} minutes today")


def low_intensity(date):
    exercise = low.low_intensity_cardio()
    duration = low.duration()
    print_workout(date, exercise, duration)


def medium_intensity(date):
    exercise = med.medium_intensity_cardio()
    duration = med.duration()
    print_workout(date, exercise, duration)


def high_intensity(date):
    choice = random.choice([1, 2])
    num_rounds = random.choice([3,4,5])
    if choice == 1:
        workout = high.circuit_training()
        print(date)
        for exercises in workout:
            print(exercises)
        print(f"30 seconds on, 10 second break for {num_rounds} rounds")
    else:
        print(date)
        print(f"30 second sprints for {num_rounds} rounds")

def main():
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
        


if __name__ == "__main__":
    main()