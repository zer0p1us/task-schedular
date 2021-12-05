from dataclasses import field
import dataclasses
from task import task
import csv
from util import *
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
			# map(lambda p: self.tasks.append(task(p, p, )), task_values)
			pass
		else:
		deadline = util.date_parcing()
		self.tasks.append(task(
			title = input("please enter a task title: "),
			description = input("please enter a task description: "),
			deadline = deadline,
				urgency = input("please enter a task urgency level (0-4), lower level is higher urgency: ")))
		pass


	def __str__(self):
		"""return tasks in agenda"""
		return [f.__str__() for f in self.tasks]

	def save_agenda(self, file_path="agenda.csv"):
		try:
		with open(file_path, "w")as csv_file:
			agenda_file = csv.DictWriter(csv_file, fieldnames=task.fields, delimiter=',', lineterminator='\r')
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
					print(dict(line).values())
					self.add_task(dict(line).values())
