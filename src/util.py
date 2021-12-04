from datetime import datetime

class util:


	@staticmethod
	def date_parcing() -> int:
		raw_date = input("please enter the date (dd/mm/yyyy): ")
		day, month, year = map(int, raw_date.split('/'))
		raw_hour = input("please enter the hour (hh:mm): ")
		if not raw_hour:
			return int(datetime(year=year, month=month, day=day).timestamp())
		else:
			hour, minute = map(int, raw_hour.split(':'))
			return int(datetime(year=year, month=month, day=day, hour=hour, minute=minute).timestamp())
