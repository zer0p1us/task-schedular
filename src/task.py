from dataclasses import dataclass, field
import random

@dataclass(init=True)
class task(object):
	id: int = field(default=random.randint(0, 1000))
	title: str = field(default="none")
	description: str = field(default="none")
	deadline: str = field(default="none")
	urgency: int = field(default=0)

	def __str__(self):
		"""return task data"""
		return f"id: {self.id} title: {self.title} description: {self.description}, deadline: {self.deadline}"

	def get_csv_format(self):
		return f"{self.id}, {self.title}, {self.description}, {self.deadline}"