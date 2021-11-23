from task import task
import random

def main():
    task_1 = task(random.randint(0, 100), str(input("please enter task title: ")))
    print(task_1.__str__())
    task_2 = task(task_title=input("please enter task title: "))
    pass

if __name__ == "__main__":
    main()