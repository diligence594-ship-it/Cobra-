import logging
import os
import sys

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN


# ---------------------------------------------------------
# Base directories
# ---------------------------------------------------------

BASE_DIR = os.path.join(
    os.path.expanduser("~"),
    ".extractor_bot"
)

SESSION_DIR = os.path.join(
    BASE_DIR,
    "sessions"
)


# ---------------------------------------------------------
# Create session directory
# ---------------------------------------------------------

try:
    os.makedirs(
        SESSION_DIR,
        mode=0o700,
        exist_ok=True
    )
except Exception as e:
    print(f"Error creating directories: {e}")
    sys.exit(1)


# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# Pyrogram Bot Client
# ---------------------------------------------------------

try:
    app = Client(
        os.path.join(
            SESSION_DIR,
            "extractor_bot"
        ),
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        sleep_threshold=120,
        workers=500
    )

except Exception as e:
    logger.error(
        f"Failed to initialize client: {e}"
    )
    sys.exit(1)
