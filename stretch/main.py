import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from format_date import format_date

def main():
    date = format_date()
    print(date)

if __name__ == "__main__":
    main()