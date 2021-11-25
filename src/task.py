from dataclasses import dataclass, field

@dataclass
class task(object):
	id: int = field(random.randint(0, 1000))
	task_title: str = field(default="none")
	task_description: str = field(default="none")
	deadline: str = field(default="none")
	# urgency: int = (deadline - currentDate) / 100
