from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
from telethon.tl.types import InputPeerUser
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.types import UpdateShortMessage
from telethon import utils
from time import sleep
from flask import Flask
import os
import sched, time
import random
from threading import Timer
from datetime import timezone
from datetime import datetime
from multiprocessing import Pool
import pytz
import asyncio
import threading
from threading import Thread
from multiprocessing import Process
from multiprocessing.dummy import Pool as ThreadPool
from flask import send_from_directory
from telethon.tl.functions.messages import ForwardMessagesRequest

app = Flask(__name__)
boss = 259885177

def main(api_id, api_hash, session_name):
	client = TelegramClient(session_name, api_id, api_hash, update_workers = 1, spawn_read_thread=False)
	client.start()

	otryad = PeerChannel(1053997467) #insert here id of otryad channel
	botID = 265204902 #ChatWarsBot
	RCBot = PeerUser(207224603)  #insert here id of castle bot
	reportID = 317117977 #insert here id of report bot
	oratorID = 317117977 #Glazik should be here
	bot = "ChatWarsBot"


	repairComands = ["/repair_wall", "/repair_hq"]

	local_tz = pytz.timezone('Europe/Moscow')
	def utc_to_local(utc_dt):
		local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
		return local_tz.normalize(local_dt)

	def attack(update):
		if update.message.from_id == oratorID and update.message.to_id == otryad and (utc_to_local(datetime.utcnow()).hour%4)%3 == 0:
			theMessage = update.message.message
			if "📊Куда вы ушли?" in theMessage or "⛳️Сводки с полей" in theMessage or "🏆Рейтинг дня🏆" in theMessage or "Отозвались помочь:" in theMessage or "запрашивает поддержку" in theMessage:
				print("wheredyougo")
			else:
				if "🇨🇾" in theMessage:
					client.send_message(bot, "🇨🇾")
					sendPin("🇨🇾", client)
				elif "🇻🇦" in theMessage:
					client.send_message(bot, "🇻🇦")
					sendPin("🇻🇦", client)
				elif "🇲🇴" in theMessage:
					client.send_message(bot, "🇲🇴")
					sendPin("🇲🇴", client)
				elif "🇰🇮" in theMessage:
					client.send_message(bot, "🇰🇮")
					sendPin("🇰🇮", client)
				elif "🇪🇺" in theMessage:
					client.send_message(bot, "🇪🇺")
					sendPin("🇪🇺", client)
				elif "🇬🇵" in theMessage:
					client.send_message(bot, "🇬🇵")
					sendPin("🇬🇵", client)
				elif "🌲" in theMessage:
					client.send_message(bot, "🌲Лесной форт")
					sendPin("🌲Лесной форт", client)
				elif "⛰" in theMessage:
					client.send_message(bot, "⛰Горный форт")
					sendPin("⛰Горный форт", client)
				elif "⚓" in theMessage:
					client.send_message(bot, "⚓Морской форт")
					sendPin("⚓Морской форт", client)
				elif "🇮🇲" in theMessage:
					client.send_message(bot, "🇮🇲")
					sendPin("🇮🇲", client)

		if update.message.from_id == botID and "результаты в бою" in update.message.message:
			client(ForwardMessagesRequest(from_peer=client.get_entity(PeerUser(botID)), id=[update.message.id], to_peer= client.get_entity(RCBot)))

		if update.message.to_id == reportID and "Сводки с полей" in update.message.message:
			t = Timer(10, addReport)
			t.start()

	def addReport():
		client.send_message(bot, "/report")

	client.add_update_handler(attack)

	client.idle()
	client.disconnect()

@app.route('/')
def root():
	return 'hi'

if __name__ == '__main__':
	backProc = Process(target = main, args=("243918", "2ace13b37b702eb5407964ff753fc37d", "first")) #insert api_id, api_hash and session_name here
	backProc.start()
	port = int(os.environ.get('PORT', 5010))
	app.run(host='0.0.0.0', port = port, debug=True, use_reloader=True)
