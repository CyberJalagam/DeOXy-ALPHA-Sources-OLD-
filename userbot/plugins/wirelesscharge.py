# For @UniBorg

"""Countdown Commands

.wchar"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(q?w)char'))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Realmeme Wireless Charging (beta) Started...\nDevice Detected: Realmeme 1 (CPH1861)\nBattery Percentage:` '

 j=10

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k+10

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Realmeme Wireless Charging (beta) Completed...\nDevice Detected: Realmeme 1(Diamond Black Varient)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4) ", link_preview=True)

