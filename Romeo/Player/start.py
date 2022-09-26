from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Romeo.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Process.filters import other_filters2
from time import time
from Process.filters import command
from datetime import datetime
from Process.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""𝐇𝐞𝐥𝐥𝐨 ❥︎ {message.from_user.mention()}, 
𝐌𝐲 𝐍𝐚𝐦𝐞 𝐢𝐬 @{BOT_NAME}.
𝐈'𝐦 𝐀 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭.
𝐏𝐥𝐚𝐲 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 𝐖𝐢𝐭𝐡𝐨𝐮𝐭 𝐋𝐚𝐠𝐬.
𝐄𝐧𝐣𝐨𝐲 𝐘𝐨𝐮𝐫 𝐦𝐮𝐬𝐢𝐜 24*7.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "Commands & Help ❔", callback_data="cbbasic"
                    ), 
                  ],[
                    InlineKeyboardButton(
                       "Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                       "Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/90b77eaaa02658d5bbefd.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ", url=f"https://github.com/Romeo-RJ/Romeo-musicBot")
                ]
            ]
        ),
    )
