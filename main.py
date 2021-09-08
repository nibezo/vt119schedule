import datetime

# status of the week, if 0 - Знаменатель, if 1 - Числитель
dt = datetime.datetime.today()
status = datetime.date(dt.year, dt.month, dt.day).isocalendar()[1] % 2
