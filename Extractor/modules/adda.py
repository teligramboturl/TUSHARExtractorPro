import requests
import json
import random
import uuid
import time
import asyncio
import io
import aiohttp
from pyrogram import Client, filters
import os
import requests
from Extractor import app
from config import CHANNEL_ID



log_channel = CHANNEL_ID

@app.on_message(filters.command(["adda"]))
async def adda_command_handler(app, m):
    try:
        e_message = await app.ask(m.chat.id, "Send **Adda247 Token** or Email*Password.\n\n**Format**: Email*Password OR Token")
        ap = e_message.text.strip()

        headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": "fpoa43edty5"
        }

        # Login Flow
        if "*" in ap:
            e, p = ap.split("*")
            login_url = "https://userapi.adda247.com/login?src=aweb"
            data = {"email": e, "providerName": "email", "sec": p}

            # ✅ Debug Patch added here:
            login_resp_raw = requests.post(login_url, json=data, headers=headers)
            try:
                login_resp = login_resp_raw.json()
            except Exception as e:
                await m.reply_text(f"❗ Invalid JSON response:\nStatus: {login_resp_raw.status_code}\nResponse: {login_resp_raw.text}")
                return

            jwt = login_resp.get("jwtToken")
            if not jwt:
                await m.reply_text("❌ Login failed. Invalid credentials or blocked request.")
                return
        else:
            jwt = ap  # direct token input

        headers["X-Jwt-Token"] = jwt

        # Fetch Purchased Packages
        packages_url = "https://store.adda247.com/api/v3/ppc/package/purchased?pageNumber=0&pageSize=20&src=aweb"
        packages_resp = requests.get(packages_url, headers=headers).json()
        packages = packages_resp.get("data", [])

        if not packages:
            await m.reply_text("❗ No packages found in your account.")
            return

        for package in packages:
            package_id = package.get("packageId")
            package_title = package.get("title", "").replace('|', '_').replace('/', '_')
            if not package_id or not package_title:
                continue

            await m.reply_text(f"📦 Processing: {package_title} ({package_id})")
            start_time = time.time()
            file_name = f"{package_id}_{package_title}.txt"

            with open(file_name, "w", encoding="utf-8") as file:
                # Get Child Packages
                child_url = f"https://store.adda247.com/api/v3/ppc/package/child?packageId={package_id}&category=ONLINE_LIVE_CLASSES&isComingSoon=false&pageNumber=0&pageSize=20&src=aweb"
                child_resp = requests.get(child_url, headers=headers).json()
                child_packages = child_resp.get("data", {}).get("packages", [])

                for child in child_packages:
                    child_id = child.get("packageId")
                    child_title = child.get("title", "").replace('|', '_').replace('/', '_')
                    if not child_id:
                        continue

                    # Get Online Classes Content
                    content_url = f"https://store.adda247.com/api/v2/my/purchase/OLC/{child_id}?src=aweb"
                    content_resp = requests.get(content_url, headers=headers).json()
                    online_classes = content_resp.get("data", {}).get("onlineClasses", [])

                    for content in online_classes:
                        class_name = content.get("name", "").replace('|', '_').replace('/', '_')

                        # PDF Extraction
                        pdf_file = content.get("pdfFileName")
                        if pdf_file:
                            pdf_link = f"https://store.adda247.com/{pdf_file}"
                            file.write(f"{class_name} : {pdf_link}\n")

                        # Video Extraction
                        video_url = content.get("url")
                        if video_url:
                            try:
                                video_api = f"https://videotest.adda247.com/file?vp={video_url}&pkgId={child_id}&isOlc=true"
                                video_resp = requests.get(video_api, headers=headers).text

                                if "480p30playlist.m3u8" in video_resp:
                                    stream_link = video_resp.strip().replace('/updated', '/demo/updated')
                                    file.write(f"{class_name} : {stream_link}\n")
                            except Exception as ve:
                                print(f"⚠️ Video Fetch Error: {ve}")

            # Send file if not empty
            if os.path.getsize(file_name) > 0:
                elapsed = time.time() - start_time
                caption = f"**App : ADDA 247**\n**Batch : {package_title}**\n⏳ Time : {elapsed:.1f}s\n\n**╾── Cobra Extractor ──╼**"
                await m.reply_document(file_name, caption=caption)
                await app.send_document(log_channel, file_name, caption=caption)

            os.remove(file_name)

    except Exception as e:
        await m.reply_text(f"❗ Error : {str(e)}")
        
        
