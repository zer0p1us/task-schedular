from task import task
class Agenda():
    tasks = list(task)

    def __init__(self, tasks=None):
        self.tasks = tasks

    def add_task(self, task):
        tasks.append(task)
        pass

    def get_tasks(self):
        return tasks