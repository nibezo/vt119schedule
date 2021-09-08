import datetime
import logging
from vkwave.bots import (SimpleLongPollBot)
from vktoken import token

bot = SimpleLongPollBot(tokens=token, group_id=207028531)
logging.basicConfig(level="DEBUG")

# status of the week, if 0 - Знаменатель, if 1 - Числитель
dt = datetime.datetime.today()
status = datetime.date(dt.year, dt.month, dt.day).isocalendar()[1] % 2
status_z = "Знаменатель🔴\n\n"
status_c = "Числитель🟦\n\n"

# if today is weekend, change week status
weekday = datetime.datetime.today().weekday()
if weekday == 5 or weekday == 6:
	if status == 1:
		status = 0
	else:
		status = 1


@bot.message_handler(bot.text_contains_filter(["Start", "Начало", "Начать"]))
async def start(event: bot.SimpleBotEvent):
	await event.answer("Привет. Отправь мне день недели и я дам на него расписание согласно Ч/З недели. Если сегодня "
					   "выходной, то дам расписание согласно статусу след. недели.\n\nCode: github.com/nibezo/vt119schedule")


"""Shit code for the getting schedule"""


@bot.message_handler(bot.text_contains_filter(["Понедельник"]))
async def start(event: bot.SimpleBotEvent):
	if status != 1:
		await event.answer(
			f"{status_z}8:30-10:00: Экономика, лк, Г-3: Вахромеева М.П.\n\n10:20-11:50: ВСВП, лк, 404-2, "
			f"Буланкин В.Б")
	else:
		await event.answer(f"{status_c}1. 8:30-10:00: Физ-ра\n\n2. 10:20-11:50: ВСВП, лк, 404-2, Буланкин В.Б\n\n3. "
						   f"12:10-13:40: "
						   f"Электронные вычислительные средства машины, лк, 404-2, Шарафеддин М.А.\n\n4. 14:00-15:30: "
						   f"Экономика, пр, 411-2, Абдуллаев Н.В.")


@bot.message_handler(bot.text_contains_filter(["Вторник"]))
async def start(event: bot.SimpleBotEvent):
	if status != 1:
		await event.answer(
			f"{status_z}3. 12:10-13:40: ОАП, лк, 404-2, Ланцов В.Н.\n\n4. 14:00-15:30: ВСВП, пр, 424-2, "
			f"Буланкин В.Б")
	else:
		await event.answer(f"{status_c}3. 12:10-13:40: ОАП, лк, 404-2, Ланцов В.Н.\n\n4. 14:00-15:30: "
						   f" ОАП, пр, 404-2, Ланцов В.Н.")


@bot.message_handler(bot.text_contains_filter(["Среда"]))
async def start(event: bot.SimpleBotEvent):
	if status != 1:
		await event.answer(
			f"{status_z}1. 8:30-10:00: ОС, лб. работы, 416-2, Сущинина А.А. с 10-й недели.\n\n2. 10:20-11:50: ОС, "
			f"лб. работы, 416-2, Сущинина А.А. с 10-й недели.\n\n3. 12:10-13:40: Физ-ра\n\n4. 14:00-15:30: ОАП, лб, "
			f"412-2, Чемоданов М.И.\n\n5. 15:50-17:20: ОАП, лаб, 412-2, Чемоданов М.И.")
	else:
		await event.answer(f"{status_c}1. 8:30-10:00: ОС, лб. работы, 416-2, Сущинина А.А. с 10-й недели.\n\n2. "
						   f"10:20-11:50: ОС,  лб. работы, 416-2, Сущинина А.А. с 10-й недели.\n\n3. 12:10-13:40: "
						   f"Физ-ра\n\n4. 14:00-15:30: ОАП, лб, 412-2, Чемоданов М.И.\n\n5. 15:50-17:20: ОАП, лаб, "
						   f"412-2, Чемоданов М.И.")


@bot.message_handler(bot.text_contains_filter(["Четверг"]))
async def start(event: bot.SimpleBotEvent):
	if status != 1:
		await event.answer(
			f"{status_z}1. 8:30-10:00: СПО, лб, 401-2, Гондин Д.А. с 10-й недели\n\n2. 10:20-11:50: СПО, лб, 401-2, "
			f"Гондин Д.А. с 10-й недели\n\n3. СПО, лк, 404-2, Трофимов М.А.")
	else:
		await event.answer(
			f"{status_c}1. 8:30-10:00: ВСВП, лб, 424-2, Буланкин В.Б.\n\n2. 10:20-11:50: ВСВП, лб, 424-2, Буланкин "
			f"В.Б.\n\n3. ОС, лк, 404-2, Сущинина А.А.")


@bot.message_handler(bot.text_contains_filter(["Пятница"]))
async def start(event: bot.SimpleBotEvent):
	if status != 1:
		await event.answer(
			f"{status_z}1. 8:30-10:00: ТЭО, пр, 117-3, Васильев Д.Н.\n\n2. 10:20-11:50: Электронные вычислительные "
			f"машины, пр, 401-2, Шарафеддин М.А")
	else:
		await event.answer(
			f"{status_z}1. 8:30-10:00: ТЭО, лк, 433-3, Васильев Д.Н.\n\n2. 10:20-11:50: СПО, пр, 412-2, Гондин Д.А")

bot.run_forever()
