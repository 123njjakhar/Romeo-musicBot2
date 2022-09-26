from pyrogram import Client, errors
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0

def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="𝐌𝐞𝐧𝐮", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="𝐈𝐧𝐥𝐢𝐧𝐞", switch_inline_query_current_chat=""),
    ],
    [
      InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data=f'cls'),
    ],
  ]
  return buttons

def stream_markup(user_id, dlurl):
  buttons = [
    [
      InlineKeyboardButton(text="𓊕", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="⏭", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="◼", callback_data=f'cbstop | {user_id}')
    ],
    [
      InlineKeyboardButton(text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/RomeoBot_OP"),
      InlineKeyboardButton(text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/Romeo_OP"),
    ],
    [
      InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data=f'cls'),
    ],
  ]
  return buttons

def menu_markup(user_id):
  buttons = [
     [InlineKeyboardButton(text="𓊕", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶", callback_data=f'cbresume | {user_id}')],
     [InlineKeyboardButton(text="⏭", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="◼", callback_data=f'cbstop | {user_id}')
    ],
     [InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/Romeo_OP"),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}')],
  ]
  return buttons

def song_download_markup(videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="☟︎︎︎ 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="☟︎︎︎ 𝐕𝐢𝐝𝐞𝐨",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐚𝐜𝐤",
                callback_data="cbhome",
            )
        ],
    ]
    return buttons

close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "𝐂𝐥𝐨𝐬𝐞", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "𝐁𝐚𝐜𝐤", callback_data="cbmenu"
      )
    ]
  ]
)
