# plugin by lejend @r4r4n4
"""Emoji

Available Commands:

.lucky"""

from telethon import events
from global_variables_sql import SYNTAX, MODULE_LIST

import asyncio



MODULE_LIST.append("lucky")


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "lucky":

        await event.edit(input_str)

        animation_chars = [
        
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",    
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/Dark-Princ3/X-tra-Telegram/)⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
            "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
            "⬜⬜\n⬜⬜",
            "[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/X-tra-Telegram/)"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 17])

SYNTAX.update({
    "lucky": f"\
**Requested Module --> Lucky**\
\n\nDetailed usage of fuction(s):\
\n\n```.lucky```\
\nUsage: Gives the lucky use a Gift :-0 .\
"
})            
