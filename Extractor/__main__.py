import asyncio
import importlib
from aiohttp import web
from pyrogram import idle
from Extractor import app  # Tera Client instance
from Extractor.modules import ALL_MODULES

# HTTP server for Render health check
async def handle(request):
    return web.Response(text="Bot is Alive!")

async def start_http_server():
    app_http = web.Application()
    app_http.router.add_get("/", handle)

    runner = web.AppRunner(app_http)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("✅ HTTP Server Running on port 8080")

async def bot_main():
    # Sab modules ko import karlo
    for module in ALL_MODULES:
        importlib.import_module(f"Extractor.modules.{module}")

    # HTTP Server ko chalu karo (background me)
    await start_http_server()

    print("✅ Bot Deployed Successfully! Polling Started 🔥")

    # Pyrogram polling listener (idle)
    await idle()

    print("👋 Bot Stopped. Bye!")

if __name__ == "__main__":
    async def main():
        # Pyrogram Client ko safe async context me chalao
        async with app:
            await bot_main()

    asyncio.run(main())
    
    



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
