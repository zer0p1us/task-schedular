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
		return f"\nid: {self.id} \ntitle: {self.title} \ndescription: {self.description} \ndeadline: {self.deadline}"

	def save_format(self):
		return {"id" : self.id, "title": self.title, "description": self.description, "deadline": self.deadline}
