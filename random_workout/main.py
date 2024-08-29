import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cardio import main_cardio
from strength import main_strength
from stretch import main_stretch

def main():
    # main_cardio.choice()
    #main_strength.choice()
    main_stretch.choice()


if __name__=="__main__":
    main()
