import asyncio
import importlib
from aiohttp import web
from pyrogram import Client, idle
from Extractor import app  # Tera Pyrogram Client
from Extractor.modules import ALL_MODULES

# HTTP server for Render healthcheck
async def web_server():
    async def handle(request):
        return web.Response(text="✅ Bot is Alive (Render Healthcheck)")

    app_web = web.Application()
    app_web.add_routes([web.get("/", handle)])

    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    print("✅ HTTP Server running on port 8080 for Render healthcheck")

# Main Bot Function
async def main():
    # Load all modules
    for module in ALL_MODULES:
        importlib.import_module(f"Extractor.modules.{module}")

    # Start HTTP Server in background
    asyncio.create_task(web_server())

    print("✅ Bot Started! Polling running...")

    # Wait for updates (polling)
    await idle()

    print("👋 Bot Stopped!")

if __name__ == "__main__":
    # Run Pyrogram Client in async context
    app.run(main)
    
    



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
