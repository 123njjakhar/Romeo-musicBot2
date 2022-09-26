## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "Romeo")
ALIVE_NAME = getenv("ALIVE_NAME", "")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RomeoBot_OP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Romeo_OP")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Romeo-RJ/Romeo-musicBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/18b7b640bccc59b331998.jpg")
