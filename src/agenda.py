from task import task
class agenda():
    tasks = []

    def __init__(self, tasks=None):
        if tasks == None:
            self.tasks = list()
        else:
            self.tasks = tasks

    def add_task(self):
        self.tasks.append(task(
            input("please enter a task title: "),
            input("please enter a task description: "),
            input("please enter a task deadline (dd/mm/yyyy, hh:mm): "),
            input("please enter a task urgency level (0-4), lower level is higher urgency: ")))
        pass

    def get_tasks(self):
        return self.tasks

    def __str__(self):
        # f = lambda task : task.__str__()
        return [f.__str__() for f in self.tasks]