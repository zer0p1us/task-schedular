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
	smart_urgency: int = field(init=False) # will not be saved but compute as it changes
	save_attributes = ["title", "description", "deadline_timestamp", "urgency", "progress"] # stores attributes to be saved

	def __post_init__(self):
		# attribute sanitation

		# make sure urgency is not empty
		if not self.urgency:
			self.urgency = 1
		self.smart_urgency = self.smart_urgency_calc()

		# convert string types from save files to appropriate types
		try:
			self.deadline_timestamp = int(self.deadline_timestamp)
			self.urgency = int(self.urgency)
		except TypeError:
			print("incorrect data types have been set in ")

		# compute deadline date
		self.deadline_date = datetime.fromtimestamp(self.deadline_timestamp)

	def __str__(self):
		"""return task data"""
		return f"\ntitle: {self.title} \ndescription: {self.description} \ndeadline: {self.deadline_date} \nurgency: {self.urgency} \nsmart urgency: {self.smart_urgency_calc()} \nprogress: {self.progress}"

	def save_format(self):
		"""return dict of attributes for save format"""
		return {"title": self.title, "description": self.description, "deadline_timestamp": self.deadline_timestamp, "urgency": self.urgency, "progress": self.progress}

	def smart_urgency_calc(self) -> int:
		"""calculates the urgency of a task based on time till deadline and urgency value"""
		try:
			self.smart_urgency = (int(self.urgency) * (int(self.deadline_timestamp) / datetime.now().timestamp()))
		except:
			print("failed to calculate smart urgency")
