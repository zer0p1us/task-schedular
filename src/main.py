from types import NoneType
from task import task
from agenda import agenda
import random

def main():
    _agenda = agenda()
    while True:

        # to handle user input erros
        try:
            option = input("""
            options:

            0: Quit
            1: View tasks
            2: Add new entry to the schedule
            3: Update entry
            """)
            option = int(option) #do not touch, try&except needs option to initialise to sort error
        except ValueError:
            # input is empty
            if not option:
                print("Please select one of the options")
            # input is not integer
            else:
                print("Please enter an interger option")
            continue


        match option:
            case 0:
                break
            case 1:
                pass
            case 2:
                _agenda.add_task()
                print(_agenda.__str__())
            case 3:
                pass
            case _:
                print(f"option {option} is not available, please chose from the available menu")
    pass

if __name__ == "__main__":
    main()