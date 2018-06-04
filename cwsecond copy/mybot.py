from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
from telethon.tl.types import InputPeerUser
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.types import UpdateShortMessage
from telethon import utils
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon.tl.functions.messages import SendInlineBotResultRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from time import sleep
from flask import Flask
from telethon.tl.functions.channels import JoinChannelRequest
import os
import sched, time
import random
import string
from threading import Timer
from datetime import timezone
from datetime import datetime
from multiprocessing import Pool
import pytz
import asyncio
import threading
import psutil
from threading import Thread
from multiprocessing import Process
from multiprocessing.dummy import Pool as ThreadPool
from flask import send_from_directory
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon import events
import sys

# print(sys.path)
app = Flask(__name__)
boss = 365685129

back = "Назад"

quest = {
	"les": "Лес",
	"peshera": "Пещера",
	"corovan": "КОРОВАНЫ",
	"coast": "Побережье"
}

arena = {
	"cancel": "Отменить поиск",
	"search": "Поиск соперника"
}

arena_hits = ["голову", "корпусу", "ногам"]
arena_defs = ["головы", "корпуса", "ног"]

lvl_up = {
	"def": "Защита",
	"atk": "Атака",
	"off": "free"
}

my_bots = [
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 442717241, "session_name": "session_seri_one", "forest_minute": 7, "client": TelegramClient("session_seri_one", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 516424242, "session_name": "session_seri_two", "forest_minute": 7, "client": TelegramClient("session_seri_two", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 544701365, "session_name": "session_seri_three", "forest_minute": 7, "client": TelegramClient("session_seri_three", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 492892382, "session_name": "session_seri_four", "forest_minute": 7, "client": TelegramClient("session_seri_four", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 469691513, "session_name": "session_seri_five", "forest_minute": 7, "client": TelegramClient("session_seri_five", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 516816403, "session_name": "session_seri_six", "forest_minute": 7, "client": TelegramClient("session_seri_six", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 488785396, "session_name": "session_seri_seven", "forest_minute": 7, "client": TelegramClient("session_seri_seven", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 520222003, "session_name": "session_seri_eight", "forest_minute": 7, "client": TelegramClient("session_seri_eight", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	{'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_nine", "forest_minute": 7, "client": TelegramClient("session_seri_nine", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_ten", "forest_minute": 7, "client": TelegramClient("session_seri_ten", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_eleven", "forest_minute": 7, "client": TelegramClient("session_seri_eleven", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_twelve", "forest_minute": 7, "client": TelegramClient("session_seri_twelve", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_thirteen", "forest_minute": 7, "client": TelegramClient("session_seri_thirteen", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_fourteen", "forest_minute": 7, "client": TelegramClient("session_seri_fourteen", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_fifteen", "forest_minute": 7, "client": TelegramClient("session_seri_fifteen", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_ovoshodin", "forest_minute": 7, "client": TelegramClient("session_seri_ovoshodin", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'twink', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_ovoshdva", "forest_minute": 7, "client": TelegramClient("session_seri_ovoshdva", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
	# {'type': 'guest', "trade_list": [], "trade_status": "off", "lvl_up": "atk", "castle": "", "nick_name": "", "trade_process": 0, "stock_to": "", "tasks": ["Лес"], "energy_left": 0, "money_left": 0, "current_task": {"time_interval": 0, "task_title": "free"}, "do_queue": [], "forest_time": {"minute": random.randint(5, 51), "hour": random.randint(0, 3), "last_hr": 25}, "boss_id": 117372556, "boss_nick": "@vo4tap", "main_group": 1126101739, 'api_id': 193978, 'api_hash': '3a20d69f0e8b06a9052dc78f34caa82f', "account": 451694200, "session_name": "session_seri_osnova", "forest_minute": 7, "client": TelegramClient("session_seri_osnova", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False)},
]

def main(api_id, api_hash, boss_id, session_name, bot_index):
	global my_bots
	global quest
	
	last_pin = "🇮🇲"

	# print(bot_index)

	client = TelegramClient(session_name, api_id, api_hash, update_workers = 1, spawn_read_thread=False)
	client.start()
	client.updates.workers = 1


	# print(client.is_user_authorized())
	# print(client.get_me().stringify() + my_bots[bot_index]["session_name"])

	# my_bots[bot_index]["client"] = client

	otryad = PeerChannel(1086576415)
	botID = PeerUser(587303845)
	cwBot = 587303845
	RCBot = PeerUser(333856432)
	reportID = PeerChannel(1090201075)
	oratorID = 309299682
	trade_bot_id = 278525885
	trade_bot = "ChatWarsTradeBot"
	market_id = 1112398751
	enot_id = 402544905
	bot = "ChatWarsClassicBot"

	client.send_message(bot, "/hero")

	# if boss_id == 365685129:
	# client(JoinChannelRequest(client.get_entity("t.me/ChatWarsMarket")))

	# if boss_id == 365685129:
	# 	client.send_message("enotobot", "/setmain_365685129")
	#lol

	repairComands = ["/repair_wall", "/repair_hq"]

	local_tz = pytz.timezone('Europe/Moscow')
	def utc_to_local(utc_dt):
		local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
		return local_tz.normalize(local_dt)

	@client.on(events.NewMessage)
	def attack(update):
		if update.message.from_id == oratorID and update.message.to_id == otryad:
			theMessage = update.message.message
			if "📊Куда вы ушли?" in theMessage or "⛳️Сводки с полей" in theMessage or "🏆Рейтинг дня🏆" in theMessage or "Отозвались помочь:" in theMessage or "запрашивает поддержку" in theMessage or "🚧Рейтинг отрядов за день [вчера]" in theMessage or "⚔️Участие в битвах понедельно" in theMessage:
				print("wheredyougo")
			else:
				print(update)
				if "🇨🇾" in theMessage:
					# last_pin = "🇨🇾"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇨🇾"]).start()
				elif "🇻🇦" in theMessage:
					# last_pin = "🇻🇦"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇻🇦"]).start()
				elif "🇲🇴" in theMessage:
					# last_pin = "🇲🇴"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇲🇴"]).start()
				elif "🇰🇮" in theMessage:
					# last_pin = "🇰🇮"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇰🇮"]).start()
				elif "🇪🇺" in theMessage:
					# last_pin = "🇪🇺"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇪🇺"]).start()
				elif "🇬🇵" in theMessage:
					# last_pin = "🇬🇵"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇬🇵"]).start()
				elif "🌲" in theMessage:
					# last_pin = "🌲Лесной форт"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🌲Лесной форт"]).start()
				elif "⛰" in theMessage:
					# last_pin = "⛰Горный форт"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["⛰Горный форт"]).start()
				elif "⚓" in theMessage:
					# last_pin = "⚓Морской форт"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["⚓Морской форт"]).start()
				elif "🇮🇲" in theMessage:
					# last_pin = "🇮🇲"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇮🇲"]).start()
					

		if update.message.to_id == reportID and "Сводки с полей" in update.message.message:
			sleep(random.randint(10, 15))
			client.send_message(bot, "/report")
			# threading.Timer(15, addReport).start()
			# threading.Timer(5, update_profile).start()
			# threading.Timer(13800, prepairAttack).start()
			# threading.Timer(13803.6, sendPin, [last_pin]).start()

		if update.message.from_id == 265204902:
			# bot_buttons = []
			# for this_row in update.message.reply_markup.rows:
			# 	for this_button in this_row.buttons:
			# 		bot_buttons.append(this_button.text)
			# print(bot_buttons)
			if "/go" in update.message.message:
				sleep(random.randint(1, 4))	
				client.send_message(bot, "/go")
			if "результаты в бою" in update.message.message or "одержал победу над" in update.message.message:
				client(ForwardMessagesRequest(from_peer=client.get_entity(botID), id=[update.message.id], to_peer= client.get_entity(RCBot)))
			if "выбери точку атаки и точку защиты" in update.message.message:
				bot_button = ""
				chosen_button = arena_hits[random.randint(0, 2)]
				for this_row in update.message.reply_markup.rows:
					for this_button in this_row.buttons:
						if chosen_button in this_button.text:
							bot_button = this_button.text
				sleep(random.randint(1, 4))			
				client.send_message(bot, bot_button)
				# threading.Timer(1, send, [bot_button]).start()
			if "Осталось определиться с защитой!" in update.message.message:
				bot_button = ""
				chosen_button = arena_defs[random.randint(0, 2)]
				for this_row in update.message.reply_markup.rows:
					for this_button in this_row.buttons:
						if chosen_button in this_button.text:
							bot_button = this_button.text
				sleep(random.randint(1, 4))			
				client.send_message(bot, bot_button)
				# threading.Timer(1, send, [bot_button]).start()
		if update.message.to_id.channel_id == 1193729236 or update.message.to_id.channel_id == 1126101739:
			if "Ты встретил злого лепрекона" in update.message.message:
				fight_message = update.message.message.split()
				client.send_message(bot, fight_message[-1])

		# if "Готов(а) к битве?" in theMessage or "Готовность к битве" in theMessage:
		# 	if not "Готовы - " in theMessage and not "Да - " in theMessage:
		# 		print("Gotov")

	def send(update):
		client.send_message(bot, update)

	def prepairAttack(pin):
		try:
			client.send_message(bot, "⚔Атака")
			threading.Timer(3.6, sendPin, [pin]).start()
			# for this_bot in my_bots:
			# 	temp = TelegramClient(this_bot["session_name"], this_bot["api_id"], this_bot["api_hash"], spawn_read_thread=False)
			# 	temp.start()
			# 	threading.Timer(0.1, sendPin, ["⚔Атака", temp]).start()
			# 	threading.Timer(6, sendPin, [pin, temp]).start()
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise

	def sendPin(pin):
		try:
			# for this_bot in my_bots:
			# 	temp = this_bot["client"]
			# 	temp.start()
			client.send_message(bot, pin)
			client.send_message(1126101739, pin)
			client.send_message(1193729236, pin)
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise
		
	def addReport():
		client.send_message(bot, "/report")
		# threading.Timer(1, addGo, [5, 7]).start()

	client.idle()
	# client.disconnect()

def bot_method(api_id, api_hash, boss_id, session_name, bot_index):
	global my_bots
	global quest
	
	last_pin = "🇮🇲"
	# client = TelegramClient(session_name, api_id, api_hash, spawn_read_thread=False)
	# client.disconnect()
	# client.start()
	# client.connect()
	# if bot_index == 2:
	# 	phone_number = '+7 (968) 872-21-78'
	# 	client.send_code_request(phone_number)
	# 	myself = client.sign_in(phone_number, input('Enter code: '))
	# my_bots[bot_index]["client"].start()
	# try:
	my_bots[bot_index]["client"].connect()
	if not my_bots[bot_index]["client"].is_user_authorized():
		print(bot_index, session_name, my_bots[bot_index]["client"].is_user_authorized())
		# print(bot_index, my_bots[bot_index]["client"].connect(), my_bots[bot_index]["client"].is_user_authorized())
		phone_number = input('Enter number: ')
		my_bots[bot_index]["client"].send_code_request(phone_number)
		me = my_bots[bot_index]["client"].sign_in(phone_number, input('Enter code: '))
	print(my_bots[bot_index]["client"].get_me().first_name)
	# except IOError:
	# 	print(my_bots[bot_index]["session_name"])
	# except ValueError:
	# 	print(my_bots[bot_index]["session_name"])
	# except:
	# 	print(my_bots[bot_index]["session_name"])
		# raise
	my_bots[bot_index]["client"].updates.workers = 1

	# my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Боевой дроид " + my_bots[bot_index]["session_name"] + " готов к бою!")
	# print(client.get_me().stringify() + my_bots[bot_index]["session_name"])

	# my_bots[bot_index]["client"] = client

	otryad = PeerChannel(1086576415)
	botID = PeerUser(587303845)
	cwBot = 587303845
	RCBot = PeerUser(333856432)
	reportID = PeerChannel(1090201075)
	oratorID = 309299682
	trade_bot_id = 278525885
	trade_bot = "ChatWarsTradeBot"
	market_id = 1112398751
	enot_id = 402544905
	bot = "ChatWarsClassicBot"

	# if boss_id == 365685129:
	# client(JoinChannelRequest(client.get_entity("t.me/ChatWarsMarket")))

	# if boss_id == 365685129:
	# 	client.send_message("enotobot", "/setmain_365685129")
	#lol

	repairComands = ["/repair_wall", "/repair_hq"]

	local_tz = pytz.timezone('Europe/Moscow')
	def utc_to_local(utc_dt):
		local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
		return local_tz.normalize(local_dt)

	clientt = my_bots[bot_index]["client"]
	# my_bots[bot_index]["client"].send_message(bot, "/start")
	@clientt.on(events.NewMessage)
	def twink(update):
		# if bot_index == 1:
			# print(update)
		try:
			if update.from_id == boss_id:
				if "#do" in update.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.split()
					task_command = current_task[1]
					if len(current_task) == 4:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task) - 2):
							task_command = task_command + " " + current_task[x]
					task_repeats = int(current_task[len(current_task) - 2])
					time_interval = int(current_task[len(current_task) - 1])
					my_bots[bot_index]["client"].send_message(boss_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " пошел делать " + task_command + ", " + str(task_repeats) + " раз(а) с интервалом в " + str(time_interval) + " минут")
					taskCame(task_command, task_repeats, my_bots[bot_index]["client"].get_me().id, time_interval)
				elif "#quest" in update.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.split()
					task_repeats = int(current_task[1])
					time_interval = int(current_task[2])
					my_bots[bot_index]["client"].send_message(boss_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " пошел по квестам, " + str(task_repeats) + " раз(а) с интервалом в " + str(time_interval) + " минут")
					addGo(task_repeats, time_interval)
				elif "#enable" in update.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.split()
					task_command = current_task[1]
					if len(current_task) == 2:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task) - 2):
							task_command = task_command + " " + current_task[x]
					task_command = quest[task_command]
					this_bot = my_bots[bot_index]
					if this_bot["account"] == my_bots[bot_index]["client"].get_me().id:
						repeats = False
						for this_task in this_bot["tasks"]:
							if this_task == task_command:
								repeats = True
						if not repeats:
							this_bot["tasks"].append(task_command)
						all_tasks = ', '.join(this_bot["tasks"])
						my_bots[bot_index]["client"].send_message(boss_id, "Понял понял. Боевой дроид " +  my_bots[bot_index]["client"].get_me().first_name + " добавил квест " + task_command + " из списка. Текущий список квестов: " + all_tasks)
				elif "#disable" in update.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.split()
					task_command = current_task[1]
					if len(current_task) == 2:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task) - 2):
							task_command = task_command + " " + current_task[x]
					task_command = quest[task_command]
					this_bot = my_bots[bot_index]
					if this_bot["account"] == my_bots[bot_index]["client"].get_me().id:
						this_bot["tasks"].remove(task_command)
						all_tasks = ', '.join(this_bot["tasks"])
						my_bots[bot_index]["client"].send_message(boss_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " убрал квест " + task_command + " из списка. Текущий список квестов: " + all_tasks)
				elif "#forward" in update.message and my_bots[bot_index]["type"] != "guest":
					for message in my_bots[bot_index]["client"].get_messages(bot, limit=1):
						my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(botID), id=[message.id], to_peer = my_bots[bot_index]["client"].get_entity(boss_id)))
				elif "#comandlog" in update.message and my_bots[bot_index]["type"] != "guest":
					all_tasks = ""
					i = 0
					for i in range(0, len(my_bots[bot_index]["do_queue"]) - 1):
						all_tasks = all_tasks + my_bots[bot_index]["do_queue"][i]["task_title"] + ", "
					my_bots[bot_index]["client"].send_message(boss_id, "Список незавершенных задании: " + all_tasks)
				elif "#cancel_do_all" in update.message and my_bots[bot_index]["type"] != "guest":
					all_tasks = ""
					i = 0
					for i in range(0, len(my_bots[bot_index]["do_queue"]) - 1):
						all_tasks = all_tasks + my_bots[bot_index]["do_queue"][i]["task_title"] + ", "
					my_bots[bot_index]["do_queue"] = []
					my_bots[bot_index]["client"].send_message(boss_id, "Готово, список удаленных задании: " + all_tasks)
				elif "#status" in update.message and my_bots[bot_index]["type"] != "guest":
					my_bots[bot_index]["client"].send_message(boss_id, "Состояние: " + my_bots[bot_index]["current_task"]["task_title"] + ", 🔋" + str(my_bots[bot_index]["energy_left"]) + ", " + my_bots[bot_index]["money_left"] + ", " + my_bots[bot_index]["castle"] + " " + my_bots[bot_index]["nick_name"] + ", " + "прокачка: " + my_bots[bot_index]["lvl_up"])
				elif "#force" in update.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.split()
					task_command = current_task[1]
					if len(current_task) == 2:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task)):
							task_command = task_command + " " + current_task[x]
					my_bots[bot_index]["client"].send_message(bot, task_command)
					my_bots[bot_index]["client"].send_message(boss_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " пошел делать " + task_command + " вне очереди")
				elif "#stock" in update.message and my_bots[bot_index]["type"] != "guest":
					my_bots[bot_index]["client"].send_message(trade_bot_id, "/start")
					my_bots[bot_index]["client"].send_message(boss_id, "Сток обновлен")
				elif "#trade" in update.message and my_bots[bot_index]["type"] != "guest":
					item_list = update.message.split()
					for item in item_list:
						if not "#trade" in item:
							my_bots[bot_index]["trade_list"].append(item)
					my_bots[bot_index]["trade_status"] = "on"
					my_bots[bot_index]["client"].send_message(trade_bot_id, random.choice(string.ascii_letters))
					my_bots[bot_index]["client"].send_message(boss_id, "Подготовка трейда началась")

		except IOError:
		    print(IOError)
		except ValueError:
		    print(ValueError)
		except:
			# if update.message.to_id.channel_id == my_bots[bot_index]["main_group"] and my_bots[bot_index]["client"].get_me().username == my_bots[bot_index]["stock_to"][1:] and :
			# 	bot_results = my_bots[bot_index]["client"](GetInlineBotResultsRequest(trade_bot, PeerChannel(my_bots[bot_index]["main_group"]), ' ', ''))
			# 	my_bots[bot_index]["client"](SendInlineBotResultRequest(my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"])), bot_results.query_id, bot_results.results[0].id))
			# 	my_bots[bot_index]["stock_to"] = ""
			if update.message.from_id == boss_id or update.message.from_id == 365685129:
				# if "report" in update.message.message:
				# 	t = Timer(5, addReport)
				# 	t.start()
				# for this_bot in my_bots:
				# 	if this_bot["account"] == my_bots[bot_index]["client"].get_me().id:
				# 		print(this_bot["energy_left"])
				if "#do" in update.message.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.message.split()
					task_command = current_task[1]
					if len(current_task) == 4:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task) - 2):
							task_command = task_command + " " + current_task[x]
					task_repeats = int(current_task[len(current_task) - 2])
					time_interval = int(current_task[len(current_task) - 1])
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " пошел делать " + task_command + ", " + str(task_repeats) + " раз(а) с интервалом в " + str(time_interval) + " минут")
					taskCame(task_command, task_repeats, my_bots[bot_index]["client"].get_me().id, time_interval)
				elif "#quest" in update.message.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.message.split()
					task_repeats = int(current_task[1])
					time_interval = int(current_task[2])
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " пошел по квестам, " + str(task_repeats) + " раз(а) с интервалом в " + str(time_interval) + " минут")
					addGo(task_repeats, time_interval)
				elif "#enable" in update.message.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.message.split()
					task_command = current_task[1]
					if len(current_task) == 2:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task) - 2):
							task_command = task_command + " " + current_task[x]
					task_command = quest[task_command]
					this_bot = my_bots[bot_index]
					if this_bot["account"] == my_bots[bot_index]["client"].get_me().id:
						repeats = False
						for this_task in this_bot["tasks"]:
							if this_task == task_command:
								repeats = True
						if not repeats:
							this_bot["tasks"].append(task_command)
						all_tasks = ', '.join(this_bot["tasks"])
						my_bots[bot_index]["client"].send_message(update.message.to_id, "Понял понял. Боевой дроид " +  my_bots[bot_index]["client"].get_me().first_name + " добавил квест " + task_command + " из списка. Текущий список квестов: " + all_tasks)
				elif "#disable" in update.message.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.message.split()
					task_command = current_task[1]
					if len(current_task) == 2:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task) - 2):
							task_command = task_command + " " + current_task[x]
					task_command = quest[task_command]
					this_bot = my_bots[bot_index]
					if this_bot["account"] == my_bots[bot_index]["client"].get_me().id:
						this_bot["tasks"].remove(task_command)
						all_tasks = ', '.join(this_bot["tasks"])
						my_bots[bot_index]["client"].send_message(update.message.to_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " убрал квест " + task_command + " из списка. Текущий список квестов: " + all_tasks)
				elif "#forward" in update.message.message and my_bots[bot_index]["type"] != "guest":
					for message in my_bots[bot_index]["client"].get_messages(bot, limit=1):
						my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(botID), id=[message.id], to_peer = my_bots[bot_index]["client"].get_entity(update.message.to_id)))
				elif "#comandlog" in update.message.message and my_bots[bot_index]["type"] != "guest":
					all_tasks = ""
					i = 0
					for i in range(0, len(my_bots[bot_index]["do_queue"]) - 1):
						all_tasks = all_tasks + my_bots[bot_index]["do_queue"][i]["task_title"] + ", "
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Список незавершенных задании: " + all_tasks)
				elif "#cancel_do_all" in update.message.message and my_bots[bot_index]["type"] != "guest":
					all_tasks = ""
					i = 0
					for i in range(0, len(my_bots[bot_index]["do_queue"]) - 1):
						all_tasks = all_tasks + my_bots[bot_index]["do_queue"][i]["task_title"] + ", "
					my_bots[bot_index]["do_queue"] = []
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Готово, список удаленных задании: " + all_tasks)
				elif "#status" in update.message.message and my_bots[bot_index]["type"] != "guest":
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Состояние: " + my_bots[bot_index]["current_task"]["task_title"] + ", 🔋" + str(my_bots[bot_index]["energy_left"]) + ", " + my_bots[bot_index]["money_left"] + ", " + my_bots[bot_index]["castle"] + " " + my_bots[bot_index]["nick_name"] + ", " + "прокачка: " + my_bots[bot_index]["lvl_up"])
				elif "#force" in update.message.message and my_bots[bot_index]["type"] != "guest":
					current_task = update.message.message.split()
					task_command = current_task[1]
					if len(current_task) == 2:
						task_command = current_task[1]
					else:
						for x in range(2, len(current_task)):
							task_command = task_command + " " + current_task[x]
					my_bots[bot_index]["client"].send_message(bot, task_command)
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Понял понял. Боевой дроид " + my_bots[bot_index]["client"].get_me().first_name + " пошел делать " + task_command + " вне очереди")
				elif "#set_group" in update.message.message and my_bots[bot_index]["type"] != "guest":
					my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Боевой дроид покидает свой 'отряд'")
					my_bots[bot_index]["main_group"] = update.message.to_id.channel_id
					my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Боевой дроид нашел новый 'отряд'")
				elif "#stock" in update.message.message and my_bots[bot_index]["type"] != "guest":
					my_bots[bot_index]["client"].send_message(trade_bot_id, random.choice(string.ascii_letters))
					my_bots[bot_index]["client"].send_message(update.message.to_id, "Сток обновлен")
				# elif "#trade" in update.message.message:
				# 	item_list = update.message.message.split()
				# 	for item in item_list:
				# 		if not "#trade" in item:
				# 			my_bots[bot_index]["trade_list"].append(item)
				# 	my_bots[bot_index]["trade_status"] = "on"
				# 	my_bots[bot_index]["client"].send_message(trade_bot_id, random.choice(string.ascii_letters))
				# 	my_bots[bot_index]["client"].send_message(update.message.to_id, "Подготовка трейда началась")
				elif "#trade" in update.message.message and my_bots[bot_index]["type"] != "guest":
					my_bots[bot_index]["trade_list"] = []
					item_list = update.message.message.split()
					for item in item_list:
						if not "#trade" in item:
							my_bots[bot_index]["trade_list"].append(item)
						else:
							to_array = item.split("@")
							give_to = "@" + to_array[1]
							my_bots[bot_index]["stock_to"] = give_to
					print(my_bots[bot_index]["client"].get_me().username + " to " + my_bots[bot_index]["stock_to"][1:])
					if my_bots[bot_index]["client"].get_me().username != my_bots[bot_index]["stock_to"][1:]:
						my_bots[bot_index]["trade_status"] = "on"
						my_bots[bot_index]["client"].send_message(trade_bot_id, random.choice(string.ascii_letters))
						my_bots[bot_index]["client"].send_message(update.message.to_id, "Передача ресурсов началась")
					else:
						my_bots[bot_index]["trade_status"] = "get"
						my_bots[bot_index]["trade_list"] = ["123", "129", "102", "101", "103", "105"]
						my_bots[bot_index]["client"].send_message(update.message.to_id, "Готов принимать ресурсы")
				elif "🇨🇾" in update.message.message:
					# last_pin = "🇨🇾"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇨🇾"]).start()
				elif "🇻🇦" in update.message.message:
					# last_pin = "🇻🇦"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇻🇦"]).start()
				elif "🇲🇴" in update.message.message:
					# last_pin = "🇲🇴"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇲🇴"]).start()
				elif "🇰🇮" in update.message.message:
					# last_pin = "🇰🇮"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇰🇮"]).start()
				elif "🇪🇺" in update.message.message:
					# last_pin = "🇪🇺"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇪🇺"]).start()
				elif "🇬🇵" in update.message.message:
					# last_pin = "🇬🇵"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇬🇵"]).start()
				elif "🌲" in update.message.message:
					# last_pin = "🌲Лесной форт"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🌲Лесной форт"]).start()
				elif "⛰" in update.message.message:
					# last_pin = "⛰Горный форт"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["⛰Горный форт"]).start()
				elif "⚓" in update.message.message:
					# last_pin = "⚓Морской форт"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["⚓Морской форт"]).start()
				elif "🇮🇲" in update.message.message:
					# last_pin = "🇮🇲"
					# threading.Timer(0.1, prepairAttack).start()
					threading.Timer(0.1, prepairAttack, ["🇮🇲"]).start()
			if update.message.from_id == cwBot:
				if "Ты встретил несколько больных созданиий, выглядящих заразными." in update.message.message or "Посетить термы" in update.message.message or "Не искушай судьбу" in update.message.message:
					my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Капча! Нужна помощь " + my_bots[bot_index]["boss_nick"])
					my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(botID), id=[update.message.id], to_peer= my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"]))))
				if "/bath" in update.message.message or "Мысли о термах не дают тебе" in update.message.message:
					sleep(random.randint(1, 4))
					my_bots[bot_index]["client"].send_message(bot, "/bath")
				if "Откажись от того, что тебе дорого, и будешь вознагражден." in update.message.message:
					my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Трейд от Васи, взгляни " + my_bots[bot_index]["boss_nick"])
					my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(botID), id=[update.message.id], to_peer= my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"]))))
				if "/go" in update.message.message:
					if utc_to_local(datetime.utcnow()).hour > 4:
						sleep(random.randint(1, 4))
						my_bots[bot_index]["client"].send_message(bot, "/go")
				if "Небольшое приключение длительностью" in update.message.message:
					random_task = my_bots[bot_index]["tasks"][random.randint(0, len(my_bots[bot_index]["tasks"]) - 1)]
					for this_row in update.message.reply_markup.rows:
						for this_button in this_row.buttons:
							if random_task in this_button.text:
								if random_task == "Лес":
									my_bots[bot_index]["energy_left"] = my_bots[bot_index]["energy_left"] - 1
								elif random_task == "Пещера":
									my_bots[bot_index]["energy_left"] = my_bots[bot_index]["energy_left"] - 2
								elif random_task == "КОРОВАНЫ":
									my_bots[bot_index]["energy_left"] = my_bots[bot_index]["energy_left"] - 2
								elif random_task == "Побережье":
									my_bots[bot_index]["energy_left"] = my_bots[bot_index]["energy_left"] - 1
								# threading.Timer(3, perform, [this_button.text]).start()
								sleep(random.randint(1, 4))
								perform(this_button.text)
								break
				if "Выносливость:" in update.message.message:
					if not "Склад:" in update.message.message:
						char_array = update.message.message.split("\n")
						i = 0
						for data in char_array:
							if "Выносливость:" in data:
								my_bots[bot_index]["energy_left"] = int(data.split()[1].split("/")[0])
								print(my_bots[bot_index]["energy_left"])
								if my_bots[bot_index]["energy_left"] > 3:
									addGo(2, 7)
							if "💰" in data:
								my_bots[bot_index]["money_left"] = data.split()[0].split("/")[0]
								# print(my_bots[bot_index]["money_left"])
							i = i + 1
						lines_array = update.message.message.split("\n")
						name_line = [s for s in lines_array if "🇮🇲" in s or "🇬🇵" in s or "🇨🇾" in s or "🇻🇦" in s or "🇲🇴" in s or "🇰🇮" in s or "🇪🇺" in s][0]
						coma_index = name_line.find(",")
						my_bots[bot_index]["nick_name"] = name_line[2:coma_index]
						my_bots[bot_index]["castle"] = name_line[0:2]
						if "/level_up" in update.message.message:
							if my_bots[bot_index]["lvl_up"] != "off":
								sleep(random.randint(4, 6))
								my_bots[bot_index]["client"].send_message(bot, "/level_up")
								sleep(random.randint(4, 6))
								if my_bots[bot_index]["lvl_up"] == "atk":
									my_bots[bot_index]["client"].send_message(bot, "+1 ⚔Атака")
								elif my_bots[bot_index]["lvl_up"] == "def":
									my_bots[bot_index]["client"].send_message(bot, "+1 🛡Защита")
				if "/fight_" in update.message.message:
					fight_message = update.message.message.split()
					print("fight " + fight_message[-1])
					my_bots[bot_index]["client"].send_message(bot, fight_message[-1])
					my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(botID), id=[update.message.id], to_peer= my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"]))))
				if "Вы потеряли:" in update.message.message:
					my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Это гг. Меня раздели, " + my_bots[bot_index]["boss_nick"])
					my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(botID), id=[update.message.id], to_peer= my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"]))))
			if update.message.from_id == 278525885:
				if "Твое предложение" in update.message.message and "[пусто]" in update.message.message:
					if not "Удалено" in update.message.message:
						my_bots[bot_index]["client"](ForwardMessagesRequest(from_peer=my_bots[bot_index]["client"].get_entity(PeerUser(trade_bot_id)), id=[update.message.id], to_peer = my_bots[bot_index]["client"].get_entity(PeerUser(enot_id))))
						if my_bots[bot_index]["trade_status"] == "on":
							bot_stock = update.message.message.split()
							count = 0
							for item in my_bots[bot_index]["trade_list"]:
								item_string = "/add_" + item
								if item_string in bot_stock:
									clear_stock = update.message.message.split("\n")
									item_number = [s for s in clear_stock if item_string in s][0].split()[-1]
									my_bots[bot_index]["client"].send_message(trade_bot_id, item_string + " " + item_number)
									count = count + 1
									sleep(random.randint(3, 5))
							my_bots[bot_index]["trade_status"] = "off"
							my_bots[bot_index]["trade_list"] = []
							if count > 0:
								my_bots[bot_index]["client"].send_message(trade_bot_id, "/done")
								sleep(4)
								bot_results = my_bots[bot_index]["client"](GetInlineBotResultsRequest(trade_bot, PeerChannel(my_bots[bot_index]["main_group"]), ' ', ''))
								my_bots[bot_index]["client"](SendInlineBotResultRequest(my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"])), bot_results.query_id, bot_results.results[0].id))
				if "Что предложишь взамен?" in update.message.message:
					if my_bots[bot_index]["trade_status"] == "get":
						bot_stock = update.message.message.split()
						print(my_bots[bot_index]["trade_list"])
						count = 0
						for item in my_bots[bot_index]["trade_list"]:
							item_string = "/add_" + item
							if item_string in bot_stock:
								my_bots[bot_index]["client"].send_message(trade_bot_id, item_string)
								count = count + 1
								break
						if count > 0:
							sleep(4)
							my_bots[bot_index]["client"].send_message(trade_bot_id, "/done")
							sleep(4)
							bot_results = my_bots[bot_index]["client"](GetInlineBotResultsRequest(trade_bot, PeerChannel(market_id), ' ', ''))
							my_bots[bot_index]["client"](SendInlineBotResultRequest(my_bots[bot_index]["client"].get_entity(PeerChannel(market_id)), bot_results.query_id, bot_results.results[0].id))
						# elif my_bots[bot_index]["trade_status"] == "gi":
						# 	bot_stock = update.message.split()
						# 	for item in my_bots[bot_index]["trade_list"]:
						# 		item_string = "/add_" + item
						# 		if item_string in bot_stock:
						# 			clear_stock = update.message.split("\n")
						# 			item_number = [s for s in clear_stock if item_string in s][0].split()[-1]
						# 			my_bots[bot_index]["client"].send_message(trade_bot_id, item_string + " " + item_number)
						# 			sleep(random.randint(3, 5))
						# 	my_bots[bot_index]["client"].send_message(trade_bot_id, "/done")
						# 	my_bots[bot_index]["trade_status"] = "off"
						# 	my_bots[bot_index]["trade_list"] = []
						# 	bot_results = my_bots[bot_index]["client"](GetInlineBotResultsRequest(trade_bot, PeerChannel(my_bots[bot_index]["main_group"]), ' ', ''))
						# 	my_bots[bot_index]["client"](SendInlineBotResultRequest(my_bots[bot_index]["client"].get_entity(PeerChannel(my_bots[bot_index]["main_group"])), bot_results.query_id, bot_results.results[0].id))

			if update.message.to_id.channel_id == market_id and my_bots[bot_index]["client"].get_me().username != my_bots[bot_index]["stock_to"][1:]:
				stock_to = my_bots[bot_index]["stock_to"][1:]
				if my_bots[bot_index]["client"].get_entity(PeerUser(update.message.from_id)).username == stock_to and my_bots[bot_index]["nick_name"] in update.message.message:
					print(update)
					sleep(1)
					my_bots[bot_index]["client"](GetBotCallbackAnswerRequest(update.message.to_id, update.message.id, data=update.message.reply_markup.rows[0].buttons[0].data))
					my_bots[bot_index]["stock_to"] = ""
					my_bots[bot_index]["client"].send_message(PeerChannel(my_bots[bot_index]["main_group"]), "Передача ресурсов завершена")
			if update.message.to_id.channel_id == my_bots[bot_index]["main_group"] and my_bots[bot_index]["client"].get_me().username == my_bots[bot_index]["stock_to"][1:] and update.message.reply_markup != None:
				my_bots[bot_index]["trade_process"] = my_bots[bot_index]["trade_process"] + 1
				time_trade = 90*my_bots[bot_index]["trade_process"] + 30
				threading.Timer(time_trade, process_trade, [update.message.to_id, update.message.id, update.message.reply_markup.rows[0].buttons[0].data]).start()
			# if update.message.from_id == cwBot:

	def process_trade(this_to_id, this_message_id, this_data):
		my_bots[bot_index]["client"](GetBotCallbackAnswerRequest(this_to_id, this_message_id, data=this_data))
		print(this_to_id)
		my_bots[bot_index]["trade_process"] = my_bots[bot_index]["trade_process"] - 1

	def send(update):
		my_bots[bot_index]["client"].send_message(bot, update)

	def update_profile():
		try:
			for message in my_bots[bot_index]["client"].get_messages(bot, limit=1):
				if message.reply_markup != None:
					for this_row in message.reply_markup.rows:
						for this_button in this_row.buttons:
							if "Герой" in this_button.text or "Назад" in this_button.text:
								my_bots[bot_index]["client"].send_message(bot, this_button.text)
								if "Назад" in this_button.text:
									threading.Timer(2, update_profile).start()
				else:
					my_bots[bot_index]["client"].send_message(bot, "/hero")
					threading.Timer(2, update_profile).start()
		except IOError:
			my_bots[bot_index]["client"].send_message(bot, "/hero")
			threading.Timer(2, update_profile).start()
		except ValueError:
			my_bots[bot_index]["client"].send_message(bot, "/hero")
			threading.Timer(2, update_profile).start()
		except:
			my_bots[bot_index]["client"].send_message(bot, "/hero")
			threading.Timer(2, update_profile).start()
			raise

	def prepairAttack(pin):
		try:
			my_bots[bot_index]["client"].send_message(bot, "⚔Атака")
			threading.Timer(3.6, sendPin, [pin]).start()
			# for this_bot in my_bots:
			# 	temp = TelegramClient(this_bot["session_name"], this_bot["api_id"], this_bot["api_hash"], spawn_read_thread=False)
			# 	temp.start()
			# 	threading.Timer(0.1, sendPin, ["⚔Атака", temp]).start()
			# 	threading.Timer(6, sendPin, [pin, temp]).start()
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise

	def sendPin(pin):
		try:
			# for this_bot in my_bots:
			# 	temp = this_bot["client"]
			# 	temp.start()
			my_bots[bot_index]["client"].send_message(bot, pin)
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise
	
	def taskCame(current_task, repeats, client_id, time_interval):
		try:
			i = 0
			for i in range(0, repeats):
				this_task = {"time_interval": time_interval, "task_title": current_task}
				my_bots[bot_index]["do_queue"].append(this_task)
				i = i + 1
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise

	def perform(current_task):
		try:
			if this_bot["type"] != "main":
				my_bots[bot_index]["client"].send_message(bot, current_task)
				my_bots[bot_index]["do_queue"].pop(0)
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise
		
	def addReport():
		my_bots[bot_index]["client"].send_message(bot, "/report")
		# threading.Timer(1, addGo, [5, 7]).start()

	def addGo(repeats, time_interval):
		try:
			i = 0
			for i in range(0, repeats):
				this_task = {"time_interval": time_interval, "task_title": "quest"}
				my_bots[bot_index]["do_queue"].append(this_task)
				i = i + 1
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise
			

	def sendQuest(this_bot):
		try:
			if this_bot["type"] != "main" and len(this_bot["tasks"]) > 0 and this_bot["energy_left"] > 0:
				my_bots[bot_index]["client"].send_message(bot, "🗺 Квесты")
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise

	# if client.get_me().id == boss:
	# 	client.add_update_handler(attack)
	# elif my_bots[bot_index]["type"] == "twink":
	# 	client.add_update_handler(twink)
	# elif my_bots[bot_index]["type"] == "guest":
	# 	client.add_update_handler(guest)

	def update_hero(type):
		try:
			if type == "info":
				if utc_to_local(datetime.utcnow()).hour > 3:
					update_profile()
				threading.Timer(random.randint(2000, 3800), update_hero, ["info"]).start()
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise

	def timing(type):
		try:
			if type == "main":
				length_check = len(my_bots[bot_index]["do_queue"]) > 0
				free_check = my_bots[bot_index]["current_task"]["task_title"] == "free"
				if length_check:
					if free_check:
						this_task = my_bots[bot_index]["do_queue"][0]
						my_bots[bot_index]["current_task"] = this_task
						threading.Timer(1, task_timer, ["task"]).start()
				if utc_to_local(datetime.utcnow()).hour%4 == my_bots[bot_index]["forest_time"]["hour"] and utc_to_local(datetime.utcnow()).minute == my_bots[bot_index]["forest_time"]["minute"] and utc_to_local(datetime.utcnow()).hour > 3:
					rel_time = utc_to_local(datetime.utcnow()).hour - 3 + utc_to_local(datetime.utcnow()).hour%4
					more_check = my_bots[bot_index]["forest_time"]["last_hr"] < rel_time
					less_check = my_bots[bot_index]["forest_time"]["last_hr"] > utc_to_local(datetime.utcnow()).hour
					if more_check or less_check:
						addGo(my_bots[bot_index]["energy_left"], 7)
						# my_bots[bot_index]["forest_time"]["last_hr"] = utc_to_local(datetime.utcnow()).hour
						next_hour = my_bots[bot_index]["forest_time"]["hour"] + random.randint(-1, 1)
						if next_hour < 0:
							my_bots[bot_index]["forest_time"] = {"minute": random.randint(1, 59), "hour": 3, "last_hr": utc_to_local(datetime.utcnow()).hour}
						elif next_hour > 3:
							my_bots[bot_index]["forest_time"] = {"minute": random.randint(1, 59), "hour": 0, "last_hr": utc_to_local(datetime.utcnow()).hour}
						else:
							my_bots[bot_index]["forest_time"] = {"minute": random.randint(1, 59), "hour": next_hour, "last_hr": utc_to_local(datetime.utcnow()).hour}
				elif utc_to_local(datetime.utcnow()).hour == 23 and utc_to_local(datetime.utcnow()).minute == (15 + bot_index%5*3):
					addGo(my_bots[bot_index]["energy_left"] + 1, 7)
				elif utc_to_local(datetime.utcnow()).hour%4 == 0 and utc_to_local(datetime.utcnow()).minute == 3:
					my_bots[bot_index]["client"].send_message(trade_bot_id, random.choice(string.ascii_letters))
					my_bots[bot_index]["client"].send_message(bot, "/report")
				threading.Timer(60, timing, ["main"]).start()
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise

	def task_timer(type):
		try:
			if type == "task":
				if len(my_bots[bot_index]["do_queue"]) > 0:
					interval = my_bots[bot_index]["do_queue"][0]["time_interval"]
					if my_bots[bot_index]["do_queue"][0]["task_title"] == "quest":
						sendQuest(my_bots[bot_index])
					else:
						perform(my_bots[bot_index]["do_queue"][0]["task_title"])
					threading.Timer(random.randint(interval*60, (interval + 1)*60), task_timer, ["task"]).start()
				else:
					my_bots[bot_index]["current_task"]["task_title"] = "free"
					my_bots[bot_index]["current_task"]["time_interval"] = 0
		except IOError:
			print(IOError)
		except ValueError:
			print(ValueError)
		except:
			print("Unexpected error 3")
			raise


	if my_bots[bot_index]["type"] != "main":
		# my_bots[bot_index]["client"].send_message(bot, "/hero")
		threading.Timer(1*(bot_index%10), timing, ["main"]).start()
		threading.Timer(1*(bot_index%10), update_hero, ["info"]).start()

	my_bots[bot_index]["client"].idle()
	# my_bots[bot_index]["client"].disconnect()

# @app.route('/')
# def root():
# 	process = psutil.Process(os.getpid())
# 	print(str(process.memory_info().rss) + " bytes")
# 	return 'hii'

if __name__ == '__main__':
	# backProc = Process(target = main, args=(my_bots[0]["api_id"], my_bots[0]["api_hash"], my_bots[0]["boss_id"], my_bots[0]["session_name"], 0))
	# backProc.start()
	id = 0
	for this_bot in my_bots:
		if this_bot["type"] != "main":
			backProc = Process(target = bot_method, args=(this_bot["api_id"], this_bot["api_hash"], this_bot["boss_id"], this_bot["session_name"], id))
			backProc.start()
			# try:
			# 	bot_method(this_bot["api_id"], this_bot["api_hash"], this_bot["boss_id"], this_bot["session_name"], id)
			# except IOError:
			# 	print(IOError)
			# except ValueError:
			# 	print(ValueError)
			# except:
			# 	print("Unexpected error 3")
			# 	raise
			sleep(1)
			id = id + 1
	# main(my_bots[1]["api_id"], my_bots[1]["api_hash"], my_bots[1]["boss_id"], my_bots[1]["session_name"], 1)
	# port = int(os.environ.get('PORT', 5020))
	# app.run(host='0.0.0.0', port = port, debug=True, use_reloader=False)


