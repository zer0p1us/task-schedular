from dataclasses import dataclass, field, fields
import random
from datetime import datetime

@dataclass(init=True)
class task():
	title: str = field(default="none")
	description: str = field(default="none")
	deadline: int = field(default="none")
	urgency: int = field(default=0)
	progress: str = field(default="in progress")
	fields = ["title", "description", "deadline", "urgency", "smart_urgency"]


	def __str__(self):
		"""return task data"""
		return f"\ntitle: {self.title} \ndescription: {self.description} \ndeadline: {self.deadline} \nurgency: {self.urgency} \nsmart urgency: {self.smart_urgency_calc()}"

	def save_format(self):
		"""return dict of attributes for save format"""
		return {"title": self.title, "description": self.description, "deadline": self.deadline, "urgency": self.urgency, "smart_urgency": self.smart_urgency_calc()}

	def smart_urgency_calc(self) -> int:
		"""calculates the urgency of a task based on time till deadline and urgency value"""
		try:
			return (int(self.urgency) * (int(self.deadline) / datetime.now().timestamp()))
		except:
			print("failed to calculate smart urgency")
			return 0
