"""Emoji

Available Commands:

.police

if u edit it then u r gay"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

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
            "@CyberJalagam **Police iz Here**"
            "Who The Fuck Kanged My Stuff Without Ma Permission?"
            "`Connecting to 698.69.96`"
            "`syncing the server 698.69.96`"
            "**`Connected!`**"
            "`Connecting To DMCA`"
            "`https://www.dmca.com/signup/createtakedown.aspx?r=mSAT`"
            "`Loading.`"
            "`Loading..`"
            "`Loading...`"
            "`Loading....`"
            "`Loading.....`"
            "`Loading......`"
            "`Loading.......`"
            "`Loading........`"
            "`Loading.........`"
            "`Creating Takedown`"
            "`Dectecting User`"
            
        ]
            if idd == 767014786:
            await reply_message.reply("`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ [Anubis](tg://user?id=742506768) __to release your account__😏")
        else:
            jnl=("`Warning!! `"
                  "[{}](tg://user?id={})"
                  "` Takedown By @CyberJalagam ...\n\n`"
                  "**First Name: ** __{}__\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim's username** : @{}\n".format(usname)
         

        
        
        
        
        
        
        
        


        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
