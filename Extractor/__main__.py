import importlib
from aiohttp import web
from pyrogram import Client, filters
from Extractor import app  # Tera Client instance
from Extractor.modules import ALL_MODULES

# Webhook handler
async def handle(request):
    await app.process_webhook_update(await request.json())
    return web.Response(text="OK")

# Health check route (optional but good for Render)
async def health_check(request):
    return web.Response(text="Bot is alive!")

async def main():
    # Sab modules load karwa le
    for module in ALL_MODULES:
        importlib.import_module(f"Extractor.modules.{module}")

    # Web server setup (Render pr 0.0.0.0:8080 fix hai)
    app_web = web.Application()
    app_web.add_routes([
        web.post("/", handle),
        web.get("/", health_check)
    ])

    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    print("✅ Webhook Server running on port 8080")

    # Start Pyrogram Client with webhook settings
    await app.start()
    await app.set_webhook("https://tusharextractorpro.onrender.com")  # <-- Change this URL

    print("✅ Bot Started with Webhook 🔥")

    # Idle loop chalayenge taki process zinda rahe
    await app.idle()

    # Jab stop karenge
    await app.stop()
    print("👋 Bot Stopped. Bye!")

if __name__ == "__main__":
    import asyncio
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
