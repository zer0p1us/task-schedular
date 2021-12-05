from dataclasses import dataclass, field
import random
from datetime import datetime

@dataclass(init=True)
class task():
	title: str = field(default="none")
	description: str = field(default="none")
	deadline_timestamp: int = field(default="none")
	urgency: int = field(default=1)
	progress: str = field(default="in progress")
	deadline_date = None # will not be saved but compute
	save_attributes = ["title", "description", "deadline_timestamp", "urgency", "progress"] # stores attributes to be saved

	def __post_init__(self):
		# attribute sanitation

		# make sure urgency is not empty
		if not self.urgency:
			self.urgency = 1
		self.smart_urgency = self.smart_urgency_calc()

		# convert string types from save files to appropriate types
		try:
			self.deadline = int(self.deadline)
			self.urgency = int(self.urgency)
		except TypeError:
			print("incorrect data types have been set in ")

		# compute deadline date
		self.deadline_date = datetime.fromtimestamp(self.deadline)

	def __str__(self):
		"""return task data"""
		return f"\ntitle: {self.title} \ndescription: {self.description} \ndeadline: {datetime.fromtimestamp(self.deadline)} \nurgency: {self.urgency} \nsmart urgency: {self.smart_urgency_calc()} \nprogress: {self.progress}"

	def save_format(self):
		"""return dict of attributes for save format"""
		return {"title": self.title, "description": self.description, "deadline": self.deadline_timestamp, "urgency": self.urgency, "progress": self.progress}

	def smart_urgency_calc(self) -> int:
		"""calculates the urgency of a task based on time till deadline and urgency value"""
		try:
			return (int(self.urgency) * (int(self.deadline) / datetime.now().timestamp()))
		except:
			print("failed to calculate smart urgency")
			return 0
