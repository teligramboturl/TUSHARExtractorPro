import asyncio
import logging
from pyrogram import Client
from flask import Flask
import threading
import os
from config import API_ID, API_HASH, BOT_TOKEN  # Apni config file mein rakho

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

app = Client(
    "extractor_bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=120,
    workers=500,
)

flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "Bot is alive!"

async def start_pyrogram():
    await app.start()
    me = await app.get_me()
    logger.info(f"Bot started: {me.first_name} (@{me.username})")
    await app.idle()
    await app.stop()

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Flask ko alag thread me chalao
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Pyrogram bot ko asyncio me run karo (main thread)
    asyncio.run(start_pyrogram())
    





"""
import importlib
import threading
import time
from flask import Flask
from pyrogram import Client, idle

from Extractor import app  # Tera Pyrogram client instance
from Extractor.modules import ALL_MODULES

# Flask app banate hain
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is alive!", 200

def run_flask():
    # Flask ko alag thread me 0.0.0.0:8080 port pe chalao
    flask_app.run(host="0.0.0.0", port=1000)

def start_bot():
    # Modules load karo
    for module in ALL_MODULES:
        importlib.import_module(f"Extractor.modules.{module}")

    # Bot start karo
    app.start()
    print("✅ Bot Started. Polling mode ON!")

    # Bot ko idle rakho (polling)
    idle()

    # Bot band hone pe stop karo
    app.stop()
    print("👋 Bot stopped.")

if __name__ == "__main__":
    # Flask server ko background thread me chalao
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Bot ko main thread me chalao
    start_bot()
    
    




import asyncio
import importlib
from pyrogram import idle
from Extractor.modules import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
"""
