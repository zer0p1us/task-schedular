from datetime import datetime

class util:


	@staticmethod
	def date_parcing() -> int:
		"""take user input and return timestamp"""
		try:
			raw_date = input("please enter the date (dd/mm/yyyy): ")
			day, month, year = map(int, raw_date.split('/'))
			raw_hour = input("please enter the hour (hh:mm): ")
		except ValueError:
			print("Error: the date entered is invalid, the deadline will be provisionally set to current time, please update in duetime")
			return datetime.now().timestamp()
		if not raw_hour:
			return int(datetime(year=year, month=month, day=day).timestamp())
		else:
			hour, minute = map(int, raw_hour.split(':'))
			return int(datetime(year=year, month=month, day=day, hour=hour, minute=minute).timestamp())
