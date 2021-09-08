import datetime
from vkwave.bots import (SimpleLongPollBot)
from vktoken import token
bot = SimpleLongPollBot(tokens=token, group_id=207028531)

# status of the week, if 0 - Знаменатель, if 1 - Числитель
dt = datetime.datetime.today()
status = datetime.date(dt.year, dt.month, dt.day).isocalendar()[1] % 2

bot.run_forever()
