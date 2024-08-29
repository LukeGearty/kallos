import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cardio import main_cardio
from strength import main_strength
from stretch import main_stretch

def main():
    print("What are you training today?")
    print("1. Strength")
    print("2. Cardio")
    print("3. Flexibility")
    choice = int(input())

    if choice == 1:
        main_strength.choice()
    elif choice == 2:
        main_cardio.choice()
    elif choice == 3:
        main_stretch.choice()


if __name__=="__main__":
    main()
