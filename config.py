# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "22470912"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "511be78079ed5d4bd4c967bc7b5ee023")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7678862761"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7678862761").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://ugbot31:ugbot1234@cluster0.n1uexk5.mongodb.net/UGxPRO?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-100"))

