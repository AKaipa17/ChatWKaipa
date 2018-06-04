import sys
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
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon import events
from flask import Flask
from flask import send_from_directory
from time import sleep
from datetime import timezone
from datetime import datetime
from threading import Timer
from multiprocessing import Process
import os
import pytz

app = Flask(__name__)

def main():
    client = TelegramClient("bot", 193978, '3a20d69f0e8b06a9052dc78f34caa82f', spawn_read_thread=False, update_workers = 1)
    client.start()
    def lop(update):
        print(update.message.message)
    @client.on(events.NewMessage)
    threading.timer(5, lop, [update])
    client.idle()

    @app.route('/')
    def root():
    	return 'hi'

    if __name__ == '__main__':
    	main()
    	#backProc = Process(target = main, args=())
    	#backProc.start()
    	port = int(os.environ.get('PORT', 5020))
    	app.run(host='0.0.0.0', port = port, debug=True, use_reloader=False)
