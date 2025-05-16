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
    
    



"""
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
