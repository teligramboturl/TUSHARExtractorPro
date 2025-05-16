import asyncio
import importlib
from pyrogram import idle
from Extractor import app  # Tera Pyrogram Client instance
from Extractor.modules import ALL_MODULES
from aiohttp import web

# HTTP server ke liye ek simple handler
async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_http_server():
    app_http = web.Application()
    app_http.add_routes([web.get('/', handle)])
    
    runner = web.AppRunner(app_http)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  # Render default port 8080
    await site.start()
    print("✅ HTTP server running on port 8080")

async def main():
    # Modules load karna
    for module in ALL_MODULES:
        importlib.import_module(f"Extractor.modules.{module}")

    # HTTP server start karna (background me)
    await start_http_server()

    print("✅ Bot Deployed Successfully! Polling Started 🔥")

    # Bot polling start (idle)
    await idle()

    print("👋 Bot Stopped. Bye!")

if __name__ == "__main__":
    # Yeh async context manager se start kar (safe way)
    async def runner():
        async with app:
            await main()

    asyncio.run(runner())
    



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
