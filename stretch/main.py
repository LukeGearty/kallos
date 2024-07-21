import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from format_date import format_date
import inflexbile as inflx
import challenging_stretch as chln


def gentle_stretching():
    stretches = []
    for i in range(1, 4):
        current_stretch = inflx.gentle_stretch()
        while current_stretch in stretches:
            current_stretch = inflx.gentle_stretch()
        stretches.append(current_stretch)
    
    for stretch in stretches:
        print(stretch)
    print("Hold each pose for 30 seconds")


def challenging():
    for i in range(1, 4):
        print(chln.intermediate_stretches())


def main():
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
        challenging()


if __name__ == "__main__":
    main()