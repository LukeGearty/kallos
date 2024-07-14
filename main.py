import format_date, reps_sets
import beginners as bgn
import intermediate as interm
import advanced as adv


def print_workout(upper, lower, core):
    print(f"{upper} :  {reps_sets.set_calculator()} x {reps_sets.rep_calculator()}")
    print(f"{lower} :  {reps_sets.set_calculator()} x {reps_sets.rep_calculator()}")
    print(f"{core} :  {reps_sets.set_calculator()} x {reps_sets.rep_calculator()}")


def beginner():
    upper = bgn.beginner_upper_body()
    lower = bgn.beginner_lower_body()
    core = bgn.beginner_core_work()

    print_workout(upper,lower,core)
    

def intermediate():
    upper = interm.intermediate_upper_body()
    lower = interm.intermediate_lower_body()
    core = interm.intermediate_core()

    print_workout(upper,lower,core)


def advanced():
    upper = adv.advanced_upper_body()
    lower = adv.advanced_lower_body()
    core = adv.advanced_core_work()

    print_workout(upper,lower,core)


def main():
    print(f"Welcome to the workout of {format_date.format_date()}")
    print("Are you more of a beginner (1), intermediate (2), or advanced (3)?")
    choice = int(input())

    if choice == 1:
        beginner()
    elif choice == 2:
        intermediate()
    elif choice == 3:
        advanced()
  

if __name__ == "__main__":
    main()