# By Priyam Kalra
# Syntax .oof, .sed, .emoji
from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types

emojis = {
    "yee": "ツ",
    "happy": "(ʘ‿ʘ)",
    "veryhappy": "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
    "amazed": "ヾ(o✪‿✪o)ｼ",
    "crying": "༎ຶ‿༎ຶ",
    "dicc": "╰U╯☜(◉ɷ◉ )",
    "fek": "╰U╯\n(‿ˠ‿)",
    "ded": "✖‿✖",
    "sad": "⊙︿⊙",
    "lenny": "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "idk": "¯\_(ツ)_/¯"
}

unpacked_emojis = ""

for emoji in emojis:
    unpacked_emojis += f"`{emoji}`\n"

# this dictionary is a mess but meh
ascii = {
    "mf": "'                            / ¯͡  ) \n                           /...../ \n                         /´¯´/ \n                       /¯..../ \n                    /....  / \n             /´¯/'...' /´¯¯·¸ \n          / '/.../..../..../.. /¨¯\ \n        ('(...´...´.... ¯~'/...')  /\n         \.................'..... /´ \n          \................ _.·´\n            \..............( \n'             \.............\\n"
}

unpacked_ascii = ""

for art in ascii:
    unpacked_ascii += f"{art}\n"


@borg.on(admin_cmd(pattern="oof ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    oof = event.pattern_match.group(1)
    if not oof:
        oof = 10
    try:
        oof = int(oof)
    except:
        return await event.edit("Count must be an integer!")
    oof = int(oof/2)
    output = ""
    for _ in range(oof):
        output += "Oo"
        await event.edit(output)
    output += "f"
    await event.edit(output)


@borg.on(admin_cmd(pattern="hek ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(5):
        await event.edit(";_;")
        await event.edit("_;;")
        await event.edit(";;_")
    await event.edit(";_;")


@borg.on(admin_cmd(pattern="sed ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(4):
        await event.edit(":/")
        await event.edit(":|")
        await event.edit(":\\")
        await event.edit(":|")
    await event.edit(":/")


@borg.on(admin_cmd(pattern="emoji ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_emoji = emojis[str(input_str)]
        await event.edit(req_emoji)
    except KeyError:
        await event.edit("Emoji not found!")


@borg.on(admin_cmd(pattern="ascii ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_ascii = ascii[str(input_str)]
        await event.edit(req_ascii)
    except KeyError:
        await event.edit("ASCII art not found!")
