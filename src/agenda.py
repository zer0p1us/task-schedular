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

	def add_task(self):
		"""add new task to agenda"""
		deadline = util.date_parcing()
		self.tasks.append(task(
			title = input("please enter a task title: "),
			description = input("please enter a task description: "),
			deadline = deadline,
			urgency = int(input("please enter a task urgency level (0-4), lower level is higher urgency: "))))
		pass


	def __str__(self):
		"""return tasks in agenda"""
		return [f.__str__() for f in self.tasks]

	def save_agenda(self, file_path="agenda.csv"):
		with open(file_path, "w")as csv_file:
			agenda_file = csv.DictWriter(csv_file, fieldnames=task.fields, delimiter=',', lineterminator='\r')
			agenda_file.writeheader()
			agenda_file.writerows([f.save_format() for f in self.tasks])
			csv_file.close()

	def load_agenda(self, file_name):
		file = open(file_name)
		return file
