# Credits --> @authoritydmc and Priyam Kalra
# A clean and beautiful alternative to .help
# Syntax (.modules)

from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types
from global_variables_sql import MODULE_LIST


@borg.on(admin_cmd(pattern="modules ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    modules = "**List of available modules:**\n"
    MODULE_LIST.sort()
    prev = "1"
    num = 0
    for module in MODULE_LIST:
        num += 1
        if prev[0] != module[0]:
            modules += f"\n\t{module[0].upper()}\n"
        modules += f"~ ```{module}```\n"
        prev = module
    modules += f"**\n\nNumber of modules loaded:** {num}\n**Tip: Use .syntax <module_name> for more info.**"
    await event.edit(modules)
