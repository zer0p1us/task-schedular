from task import task
from agenda import agenda

def main():
	_agenda = agenda()
	_agenda.table() if len(_agenda.tasks) != 0 else print("no tasks present")
	while True:

		# to handle user input error
		try:
			option = input(
			"option:\n"+
			"\t0: Quit\n"+
			"\t1: View tasks\n"+
			"\t2: Add new entry to the schedule\n"+
			"\t3: Update entry\n")
			option = int(option) #do not touch, try&except needs option to initialise to sort error
		except ValueError:
			# input is empty
			if not option:
				print("Please select one of the options")
			# input is not integer
			else:
				print("Please select an integer option")
			continue


		if option == 0:
			_agenda.save_agenda()
			break
		elif option == 1:
			_agenda.table() if len(_agenda.tasks) != 0 else print("no tasks present")
		elif option == 2:
			_agenda.add_task()
		elif option == 3:
			_agenda.table() if len(_agenda.tasks) != 0 else print("no tasks present")
			try:
				_agenda.update_task(int(input("please select the index of the task to update: ")))
			except ValueError:
				print("the index entered is invalid")
		else:
			print(f"option {option} is not available, please chose from the available menu")
	pass

if __name__ == "__main__":
	main()