#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 26075120
API_HASH = '1fda88a5d1de46058a4791c78bce198e'
BOT_TOKEN = '6322457392:AAGt3Aeav7PsofTOUm_86FRh9ptp9IdocbY'
SESSION = 'BQFhMqkAjXZrOHRa3_EQMpRCX4ieuxg19me1AvUXGpoZ4qMIzOsCH5m3MmV8BG_mNLEwwKSsDJfi4vukf3U4F1x1nV5SV_0du6nKgaqDFF3soOqimdKOZgIqmpG50RZ9Ql4a7KNIqHjXTMzTzUcixYqSooAgkEXHEK65Jv9H-xQOg_AcqzJ65XcKW-D1exWU8LGMG4eg8VOnDP2rKSPrv4kjRmuSa9GAC1UNsjvmkFuJLBrhKTLaQzlkZe_OzpM3mL1tptSvPi4qR4bJztAtbyvHzkpaLdJoiE_ubcwjiTHs66uuoJ_yyuP_6wiaIW17EN1r9K1EqehAQWH_h0_ofpB2EXdEsgAAAAGNRBjKAA'
FORCESUB = 'jaijaijaisiyarama'
AUTH = 5621114370

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
