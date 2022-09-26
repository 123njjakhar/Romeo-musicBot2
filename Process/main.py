from pyrogram import Client
from Romeo.config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "Romeo",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Romeo.Player"),
    )

rj = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(rj,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(rj, overload_quiet_mode=True)

with Client("Romeo", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with rj as app:
    me_rj = app.get_me()
