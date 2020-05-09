# For UniBorg
# By Priyam Kalra
#Ported To X-tra MOD 2.0 By MrMobTech

from uniborg.util import admin_cmd
from telethon.tl import functions, types
import time


@borg.on(admin_cmd(pattern="log ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    rep = await event.get_reply_message()
    msg = rep.text
    await log(msg)
    await event.delete()


async def log(text):
    LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
    await borg.send_message(LOGGER, text)
