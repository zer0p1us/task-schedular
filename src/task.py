from dataclasses import dataclass, field

@dataclass
class task():
	id: int
	task_title: str = field(default="none")
	task_description: str = field(default="none")
	deadline: str = field(default="none")
	# urgency: int = (deadline - currentDate) / 100
