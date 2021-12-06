from datetime import datetime

class util:


	@staticmethod
	def date_parcing() -> int:
		"""take user input and return timestamp"""
		try:
			day, month, year = map(int, input("please enter the date (dd/mm/yyyy): ").split('/'))
		except ValueError:
			print("Error: the date entered is invalid, the deadline will be provisionally set to current time, please update in duetime")
			return datetime.now().timestamp()
		raw_hour = input("please enter the hour (hh:mm): ")
		if not raw_hour:
			return int(datetime(year=year, month=month, day=day).timestamp())
		else:
			hour, minute = map(int, raw_hour.split(':'))
			return int(datetime(year=year, month=month, day=day, hour=hour, minute=minute).timestamp())

	@staticmethod
	def get_task_input(original_value, input_text, date_func=None):
		"""take input from user, if user input is null original_value will be returned"""
		if not date_func:
			new_text = input(input_text)
			return original_value if not new_text else new_text
		else:
			try:
				update_deadline = input("Would you like to update the deadline (y/n): ")
				if update_deadline == 'y':
					return date_func()
				elif update_deadline == 'n':
					return original_value
			except TypeError:
				print("invalid option, deadline will remain unchained")
				return original_value