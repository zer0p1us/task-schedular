from task import task
import random

def main():
    while True:
        option = int(input("""
        options:

		0: Quit
		1: View tasks
		2: Add new entry to the schedule
		3: Update entry
        0"""))

        match option:
            case 0:
                break
            case 1:

            case 2:
                new_task = task()

            case 3:

            case _:
                print(f"option {option} is not available, please chose from the available menu")
    pass

if __name__ == "__main__":
    main()