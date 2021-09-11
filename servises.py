import datetime


def get_status():
	# status of the week, if 0 - Знаменатель, if 1 - Числитель
	dt = datetime.datetime.today()
	status = datetime.date(dt.year, dt.month, dt.day).isocalendar()[1] % 2

	# if today is weekend, change week status
	weekday = datetime.datetime.today().weekday()
	if weekday == 5 or weekday == 6:
		if status == 1:
			status = 0
		else:
			status = 1
	return status
