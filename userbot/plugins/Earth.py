# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

from telethon import events
import asyncio
from collections import deque
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("solarsystem")

@borg.on(events.NewMessage(pattern=r"\.earth", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
SYNTAX.update({
    "solarsystem": f"\
**Requested Module --> Solar System**\
\n\nDetailed usage of fuction(s):\
\n\n\
\nUsage: Creates Cool Planet Emojis.\n\
\n\nList of included Animaes:\
\```.Earth```\n\
\n```.moon```\n\
\n```.solarsystem```\n\
"
})
