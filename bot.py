from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

loop = asyncio.get_event_loop()

SUPPORT_GROUP = -1002034052245
SUPPORT_LINK = 'https://t.me/fsmoviebotz'

START_MESSAGE = """ʜᴇʟʟᴏ, {user},
ᴍʏ ɴᴀᴍᴇ ɪꜱ ᴄᴏɴᴛᴀᴄᴛ
ɪ ᴀᴍ ᴀ ꜱɪᴍᴩʟᴇ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ ꜰɪʀᴏꜱ
ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴀᴅᴍɪɴ.
ʏᴏᴜ ᴄᴀɴ ᴀꜱᴋ ᴀɴʏ qᴜᴇꜱᴛɪᴏɴ ɴᴏᴡ.
ᴍʏ ᴀᴅᴍɪɴ ᴡɪʟʟ ʀᴇᴩʟᴀʏ ʏᴏᴜ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇꜱ."""

API_ID =17432758
API_HASH = 'c9e31fda0ce722e3f3033a9d4f140783'
TOKEN = '6949032971:AAF_WqJvnvCq36yrhZLZ0QGkmccq03qJyI0'

firos = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

@firos.on_message(filters.command("start"))
async def start(client, message):
    welcome_message = START_MESSAGE.format(user=message.from_user.first_name)
    btn1 = [[
            InlineKeyboardButton('Support Group', url=SUPPORT_LINK),
            InlineKeyboardButton('ADMIN',url='https://t.me/firossha')
        ]]
    await message.reply_text(welcome_message,reply_markup=InlineKeyboardMarkup(btn1))
    
firos.run()