from dataclasses import field
from os import terminal_size
from task import task
import csv
class agenda():
    tasks = []

    def __init__(self, tasks=None):
        if tasks == None:
            self.tasks = list()
        else:
            self.tasks = tasks

    def add_task(self):
        """add new task to agenda"""
        self.tasks.append(task(
            input("please enter a task title: "),
            input("please enter a task description: "),
            input("please enter a task deadline (dd/mm/yyyy, hh:mm): "),
            input("please enter a task urgency level (0-4), lower level is higher urgency: ")))
        pass

    def get_tasks(self):
        """return tasks array"""
        return self.tasks

    def __str__(self):
        """return tasks in agenda"""
        return [f.__str__() for f in self.tasks]

    def save_agenda(self, file_path="agenda.csv"):
        fields = ["id", "title", "description", "deadline", "urgency"]
        with open(file_path, "w")as csv_file:
            # agenda_file = csv.writer(csv_file, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
            agenda_file = csv.DictWriter(csv_file, fieldnames=fields, delimiter=',', lineterminator='\r')
            agenda_file.writeheader()
            agenda_file.writerows([f.save_format() for f in self.tasks])
            csv_file.close()

    def load_agenda(self, file_name):
        file = open(file_name)
        return file
