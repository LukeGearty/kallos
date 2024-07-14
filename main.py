import format_date, reps_sets
import beginners as bgn
import intermediate as interm
import advanced as adv


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

    

def main():
    date = format_date.format_date()
    print(f"Welcome to the workout of {date}")
    print("Are you more of a beginner (1), intermediate (2), or advanced (3)?")
    choice = 0
    while True:
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
    


if __name__ == "__main__":
    main()