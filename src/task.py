from dataclass import dataclass

@dataclass
class task():
	id: int
	task_title: str = "none"
	task_description: str = "none"
	deadline: str = "none"
	# urgency: int = (deadline - currentDate) / 100
