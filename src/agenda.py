from dataclasses import dataclass, field
from task import task
import csv
from util import *
import operator
class agenda():
	tasks = []

	def __init__(self, tasks=None):
		if tasks == None:
			self.tasks = list()
		else:
			self.tasks = tasks
		self.load_agenda()

	def add_task(self, task_values=[]):
		"""add new task to agenda"""
		if task_values != []:
			self.tasks.append(task(*task_values))
		else:
			# deadline = util.date_parcing()
			self.tasks.append(task(
				title = input("please enter a task title: "),
				description = input("please enter a task description: "),
				deadline_timestamp = util.date_parcing(),
				urgency = input("please enter a task urgency level (0-4), lower level is higher urgency: ")))
		self.order_tasks()

	def order_tasks(self):
		"""order task list according to smart_urgency of each task"""
		self.tasks = sorted(self.tasks, key=operator.attrgetter("smart_urgency"), reverse=True)

	def __str__(self):
		"""return tasks in agenda"""
		return [f.__str__() for f in self.tasks]

	def save_agenda(self, file_path="agenda.csv"):
		try:
			with open(file_path, "w")as csv_file:
				agenda_file = csv.DictWriter(csv_file, fieldnames=task.save_attributes, delimiter=',', lineterminator='\r')
				agenda_file.writeheader()
				agenda_file.writerows([f.save_format() for f in self.tasks])
				csv_file.close()
		except:
			print("could not write file for unknown reasons")

	def load_agenda(self, file_name="agenda.csv"):
		try:
			with open(file_name, "r") as csv_file:
				agenda_file = csv.DictReader(csv_file)
				for line in agenda_file:
					self.add_task(dict(line).values())
		except FileNotFoundError:
			print("not valid agenda.csv files were found, new agenda.csv file will be created with the new tasks")

	def table(self):
		print ("{:^8} {:^8} {:^20} {:^20} {:^10} {:^10}".format("index", "title", "description", "deadline", "urgency", "progress"))
		for index, task_attributes in enumerate(self.tasks):
			print (f"{index:^8} {task_attributes.title:^8} {task_attributes.description:^20} {task_attributes.deadline_date:^20} {task_attributes.urgency:^10} {task_attributes.progress:^10}")
			pass
