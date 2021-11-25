from task import task
from agenda import agenda
import random

def main():
    _agenda = agenda()
    while True:
        option = int(input("""
        options:

		0: Quit
		1: View tasks
		2: Add new entry to the schedule
		3: Update entry
        """))

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