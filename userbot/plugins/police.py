"""Emoji
Available Commands:
.police"""

from telethon import events

import asyncio


from uniborg.util import admin_cmd





@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 66)
    
    input_str = event.pattern_match.group(1)

    if input_str == "police":

        await event.edit(input_str)
        
        animation_chars = [
        
		
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",    
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "**Telegram Security Service is on its way here.**",
            "**Telegram Security Service is on its way here..**",
            "**Telegram Security Service is on its way here...**",
            "**Directly entering this Chat.**",
            "**Directly entering this Chat..**",
            "Via",
            "Server",
            "`2048`",
            "`2048.786`",
            "`2048.786.69`",
            "`2048.786.69.1`",
            "Passing by Narrow and Complicated Servers.",
            "Passing by Narrow and Complicated Servers..",
            "**@CyberJalagam Police is here**",
            "**@CyberJalagam Police is here!!**",
            "`Connecting to 2048.786.69.1`",
            "`syncing the server 2048.786.69.1`",
            "**`Connected!`**",
            "`Connecting To DMCA`",
            "`https://www.dmca.com/signup/createtakedown.aspx?r=mSAT`",
            "`Loading.`",
            "`Loading..`",
            "`Loading...`",
            "`Loading....`",
            "`Loading.....`",
            "`Loading......`",
            "`Loading.......`",
            "`Loading........`",
            "`Loading.........`",
            "`Creating Takedown`",
            "`Dectecting User`",
            "Looking for Guilty.",
            "Looking for Guilty..",
            "Looking for Guilty...",
            "Successful",
            "`Sending DMCA`",
            "`Processing.`",
            "`Processing..`",
            "`Processing...`",
            "`Processing....`",
            "`Processing.....`",
            "`Processing......`",
            "`Processing.......`",
            "`Processing........`",
            "`Processing.........`",
            "`DMCA Successfully Completed`",
            "**2048.786.69.1 Disconnected**"
	    "**!!Guilty Arrested!!**",
            "**!! Guilty Arrested !!**",
            "__user BANNED fron Telegram__",
            "__USER banned FROM telegram__",
            "***JUSTICE***\n\nPolice has arrested the targeted user)
    
	]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 66])
