"""Emoji
Available Commands:
.hackallph

from telethon import events

from telethon.tl.functions.users import GetFullUserRequest

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "hackallph":
        
        await event.edit(input_str)
        
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 767014786:
            await reply_message.reply("`Wait a second, This is my boss!`\n**How dare you threaten to hack my boss' google account stupid!**\n\n__Your account will be hacked in a few minutes! Pay 50$ to my Boss__ [MrMobTechYT](https://t.me/cyberjalagam) __OR delete your telegram account to prevent the virus getting into your Gmail account __😏")
        else:
            animation_chars = [
        
            "`Connecting To DarkWeb.ONION...`",
            "`Successful!`",
            "`Connected 69.669.699.96
            "`Targetting Selected Message.`",
            "`Successfully Founded The Hash Of The Account`"
            "`Targeting PH: HackAll.onion`"
            "`Attempting method I... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method I FAILED!`",
            "`Attempting method II... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method II Does Not Exist!`",
            "`Attempting method III... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Disabling Account Security... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting Password... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Pulling Information... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 69%\n█████████████████▒▒▒▒▒▒▒▒ `",
            "`Hacking... 74%\n███████████████████▒▒▒▒▒▒▒ `",
            "`Hacking.... 80%\n█████████████████████▒▒▒▒ `",
            "`Adding Modules... 84%\n█████████████████████▒▒▒▒ `",
            "`Adding Finishing Touches... 96%\n████████████████████████▒`",
            "`HACKED 100%\n█████████████████████████ `",
            "`Targeted PH: All Accounts Hacked. ×_× Hacked Successfully...`\n__Targeted account is under Boss' control now__\n\n**Pay 50$ To** @CyberJalagam **Or Get Ready To See Your E-Mail and YouTube Channel Spamming Everywhere.**"
   
            
            
            
            ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
