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
from telethon import events
from telethon.tl.functions.messages import ForwardMessagesRequest

app = Flask(__name__)
def main(api_id, api_hash, session_name):
    client = TelegramClient(session_name, api_id, api_hash, update_workers = 1, spawn_read_thread=False)
    client.start()
    @client.on(events.NewMessage)
    def attack(update):
        print(update)
    client.idle()
    client.disconnect()

@app.route('/')
def root():
	return 'hi'

if __name__ == '__main__':
    main(243918, "2ace13b37b702eb5407964ff753fc37d", "Eyefirst")
	#backProc = Process(target = main, args=("243918", "2ace13b37b702eb5407964ff753fc37d", "first")) #insert api_id, api_hash and session_name here
	#backProc.start()
	#port = int(os.environ.get('PORT', 5010))
	#app.run(host='0.0.0.0', port = port, debug=True, use_reloader=True)
