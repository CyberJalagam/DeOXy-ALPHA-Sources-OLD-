"""Emoji

Available Commands:

.call"""

from telethon import events
import asyncio
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("call")


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @CyberJalagam ,`Please Connect me to my lil bro,Vishnu`",
            "`User Authorised.`",
            "`Calling @kingsman_vishnu`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Vishnu: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @CyberJalagam ",
            "`Vishnu: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Vishnu: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Vishnu: Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Vishnu: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
            
SYNTAX.update({
    "call": f"\
**Requested Module --> Call meme**\
\n\nDetailed usage of fuction(s):\
\n\n```.call```\
\nUsage: Calls a friend.\
"
})
