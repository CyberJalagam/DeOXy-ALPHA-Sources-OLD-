# For UniBorg
# By Priyam Kalra
# Syntax (.rmota <device_model>)
#Ported To Xtra MOD v2.0 By MrMobTech
from telethon import events
from telethon.tl import functions, types
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="rmota ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        if input_str.startswith("RM") or input_str.startswith("CPH"):
            model = input_str
        else:
            await event.edit("**ERROR: Please enter a valid device model name!**")
            return
    else:
        await event.edit("**ERROR: Please enter a valid device model name!**")
        return
    bot = "@realmeupdaterbot"
    await event.edit(f"```Looking for latest OTA for {model}...```")

    async with borg.conversation(bot) as bot_conv:
        if True:
            response = await silently_send_message(bot_conv, "/start")
            if not response.text.startswith("Hey!"):
                await event.edit(f"{response.text}")
                return
            response = await silently_send_message(bot_conv, f"/GetLatestOTA {model}")
            if response.text.startswith("There"):
                await event.edit(f"{response.text}")
                return
            await event.edit(response.text)


async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response
