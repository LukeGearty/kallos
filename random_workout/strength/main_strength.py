import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from format_date import format_date
from strength_packages import reps_sets, beginners as bgn, intermediate as interm, advanced as adv

def print_workout(date, upper, lower, core):
    print(date)
    print(f"{upper} :  {reps_sets.set_calculator()} x {reps_sets.rep_calculator()}")
    print(f"{lower} :  {reps_sets.set_calculator()} x {reps_sets.rep_calculator()}")
    print(f"{core} :  {reps_sets.set_calculator()} x {reps_sets.rep_calculator()}")


def beginner(date):
    upper = bgn.beginner_upper_body()
    lower = bgn.beginner_lower_body()
    core = bgn.beginner_core_work()
    print_workout(date, upper,lower,core)
    

def intermediate(date):
    upper = interm.intermediate_upper_body()
    lower = interm.intermediate_lower_body()
    core = interm.intermediate_core()
    print_workout(date, upper,lower,core)


def advanced(date):
    upper = adv.advanced_upper_body()
    lower = adv.advanced_lower_body()
    core = adv.advanced_core_work()
    print_workout(date, upper,lower,core)

    

def choice():
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
        beginner(date)
    elif choice == 2:
        intermediate(date)
    elif choice == 3:
        advanced(date)