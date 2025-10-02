from os import getenv


API_ID = int(getenv("API_ID", "23673651"))
API_HASH = getenv("API_HASH", "f032bfa12ee46e1283f6fb23cfca5c6b")
BOT_TOKEN = getenv("BOT_TOKEN", "8307502375:AAH0_nZ784i-0Hdg4d75TlpIveBMbV7ynqE")
OWNER_ID = int(getenv("OWNER_ID", "6677821706"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6677821706").split()))
MONGO_URL = getenv("MONGO_DB", "MONGO_DB=mongodb+srv://beqaliha:BOn3lVYHJMjyD0P0@cluster0.asioswd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002755790239"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1003047586469"))
API_HASH = environ.get("API_HASH", "f032bfa12ee46e1283f6fb23cfca5c6b"")

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "23673651"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "f032bfa12ee46e1283f6fb23cfca5c6b")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8307502375:AAH0_nZ784i-0Hdg4d75TlpIveBMbV7ynqE")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Urluploderbot_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6677821706"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6677821706").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002755790239"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "MONGO_DB=mongodb+srv://beqaliha:BOn3lVYHJMjyD0P0@cluster0.asioswd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003047586469"))
