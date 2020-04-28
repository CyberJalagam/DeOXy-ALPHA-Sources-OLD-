"""Emoji

Available Commands:

.police

if u edit it then u r gay"""

from telethon import events

import asyncio
from telethon.tl.functions.users import GetFullUserRequest

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 60)

    input_str = event.pattern_match.group(1)

    if input_str == "police":

        await event.edit(input_str)
	
	if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
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
            "Passing by Narrow and Conplicated Servers.",
            "Passing by Narrow and Conplicated Servers..",
            "@CyberJalagam **Police iz Here**",
            "Who The Fuck Kanged My Stuff Without Ma Permission?",
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
            "`User Dectected Successfully`",
            "Guilty : [{}](tg://user?id={})".format(firstname, idd),
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
            "***JUSTICE***\n\nDMCA Completed. [{}](tg://user?id={})".format(firstname, idd)
       
        
        
        
        ]
             
         

        
        
        
        
        
        
        
     

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 60])
