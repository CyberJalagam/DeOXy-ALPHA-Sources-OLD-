"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, oof nub set a name"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("      👍🏻  `Currently Alive!` 🍻\n"
                     "__Telethon version: 6.9.0 // Python: 3.7.3\n\n__"
                     "**◆ --------------------- ✪ ---------------------◆**\n"
                     "𝐵𝑜𝑡 𝓂𝑜𝒹𝒾𝒻𝒾𝑒𝒹 𝑏𝑦: [𝕄𝕣.𝕄𝕠𝕓𝕋𝕖𝕔𝕙𝕐𝕋✪](t.me/CyberJalagam)\n"
                     "Thanks to:[SnapDragon](tg://user?id=719877937), @anubisxx\n"
                     f"ℱÃ𝐈𝕥н𝒻𝕦l𝕝𝔂 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑓𝑜𝑟: 🎖{DEFAULTUSER}\n"
                     "**◆ --------------------- ✪ ---------------------◆**\n\n"
                     "                       ★彡 [GitHub](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram) 彡★"
                     "                                                ")
