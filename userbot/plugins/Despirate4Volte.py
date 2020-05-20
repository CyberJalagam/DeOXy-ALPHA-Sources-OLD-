#Don't Mess With The Credits
#Written By: @CyberJalagam and @TechyNewbie

"""Emoji
#SYNTAX .volte"""

from global_variables_sql import SYNTAX, MODULE_LIST
from telethon import events

import asyncio

MODULE_LIST.append("desp4volte")



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 41)

    input_str = event.pattern_match.group(1)

    if input_str == "volte":

        await event.edit(input_str)

        animation_chars = [
        
            "Checking Device",
            "`Realme 1 (MTK Helio P60)` detected",
            "Detecting System",
            "`LOS 16` detected",
            "`Connecting To Jio Network...`",
            "` ▒ ▒ ▒ ▒ ▒`",           
            "` ▂ ▒ ▒ ▒ ▒`",
            "` ▂ ▄ ▒ ▒ ▒`",
            "` ▂ ▄ ▆ ▒ ▒`",
            "` ▂ ▄ ▆ ▇ ▒`",
            "` ▂ ▄ ▆ ▇ █`",
            "**No SIM Card detected**",
            "**Not for Jio users**",
            "__Flashing GSI__",
            "`Connecting To Jio Network...`",
            "` ▒ ▒ ▒ ▒ ▒`",           
            "` ▂ ▒ ▒ ▒ ▒`",
            "` ▂ ▄ ▒ ▒ ▒`",
            "` ▂ ▄ ▆ ▒ ▒`",
            "` ▂ ▄ ▆ ▇ ▒`",
            "` ▂ ▄ ▆ ▇ █`",
            "**Connection Successful!**",
            "`Checking VoLTE`",
            "`Checking VoLTE.`",
            "`Checking VoLTE`..",
            "**VoLTE Not Detected ;_; **",
            "**Not for Jio users**",
            "__Flashing Stock ColorOS__",
            "`Connecting To Jio Network...`",
           "` ▒ ▒ ▒ ▒ ▒`",           
            "` ▂ ▒ ▒ ▒ ▒`",
            "` ▂ ▄ ▒ ▒ ▒`",
            "` ▂ ▄ ▆ ▒ ▒`",
            "` ▂ ▄ ▆ ▇ ▒`",
            "` ▂ ▄ ▆ ▇ █`",
            "**Connection Succesful!**",
            "`Checking VoLTE`",
            "`Checking VoLTE.`",
            "`Checking VoLTE..`",
            "**Stable VoLTE Dectected**",
            "`#JioGeng Continue The Sed ShitOS Loif ;_; `"


 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 41])

SYNTAX.update({
    "desp4volte": "\
**Requested module --> Despirate For VoLTE**\
\n\n• `.volte`\
\n__Usage: Express the sed loif of a MemeTek GSI/ROM user__\
"
})            
