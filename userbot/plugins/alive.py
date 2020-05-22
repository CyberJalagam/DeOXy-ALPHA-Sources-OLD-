"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST


MODULE_LIST.append("alive")


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, Just do set a name nibber."

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("•._.••´¯``•.¸¸.•` 𝔡𝓔𝐎𝕩𝕐 `•.¸¸.•´´¯`••._.•\n\n"
                     "👍🏻  `-̷-̷-̷-̷-̷-̷ Currently Alive! 🍻 -̷-̷-̷-̷-̷-̷` \n\n"
                     "__Telethon version: 6.9.0 // Python: 3.7.3\n\n__"
                     "**◆ --------------------- ✪ ---------------------◆**\n"
                     "𝓑𝓸𝓽 𝓜𝓪𝓭𝓮 𝓑𝔂: [𝕄𝕣.𝕄𝕠𝕓𝕋𝕖𝕔𝕙𝕐𝕋✪](t.me/CyberJalagam)\n"
                     "Thanks to: @SnapDragon7410, @anubisxx\n"
                     f"ℱÃ𝐈𝕥н𝒻𝕦l𝕝𝔂 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑓𝑜𝑟: 🎖{DEFAULTUSER}\n"
                     "**◆ --------------------- ✪ ---------------------◆**\n\n"
                     "                       ★彡 [GitHub](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram) 彡★"
                     "                                                ")
SYNTAX.update({
    "alive": "\
**Requested Module --> alive**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.alive```\
\nUsage: Checks If Userbot Is Alive.\
"
})
