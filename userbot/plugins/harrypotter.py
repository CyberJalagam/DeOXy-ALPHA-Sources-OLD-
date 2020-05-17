"""
Pulls Up A Random Chant From Harry Potter Series...
Syntax: .hp
    orginal author : AlenPaulVarghese(@STARKTM1)
"""
from telethon import events
import asyncio
import os
import sys
import random



@borg.on(events.NewMessage(pattern=r"\.hp", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    x=(random.randrange(1,40)) 
    if (x==1):
      await event.edit("**MAGIC - Aberto**")
    if (x==2):
      await event.edit("**MAGIC - Accio**")
    if (x==3):
      await event.edit("**MAGIC - Aguamenti**")
    if (x==4):
      await event.edit("**MAGIC - Alohomora**")
    if (x==5):
      await event.edit("**MAGIC - Avada Kedavra**")
    if (x==6):
      await event.edit("**MAGIC - Colloportus**")
    if (x==7):
      await event.edit("**MAGIC - Confringo**")
    if (x==8):
      await event.edit("**MAGIC - Confundo**")
    if (x==9):
      await event.edit("**MAGIC - Crucio**")
    if (x==10):
      await event.edit("**MAGIC - Descendo**")
    if (x==11):
      await event.edit("**MAGIC - Diffindo**")
    if (x==12):
      await event.edit("**MAGIC - Engorgio**")
    if (x==13):
      await event.edit("**MAGIC - Episkey**")
    if (x==14):
      await event.edit("**MAGIC - Evanesco**")
    if (x==15):
      await event.edit("**MAGIC - Expecto Patronum**")
    if (x==16):
      await event.edit("**MAGIC - Expelliarmus**")
    if (x==17):
      await event.edit("**MAGIC - Finestra**")
    if (x==18):
      await event.edit("**MAGIC - Homenum Revelio**")
    if (x==19):
      await event.edit("**MAGIC - Impedimenta**")
    if (x==20):
      await event.edit("**MAGIC - Imperio**")
    if (x==21):
      await event.edit("**MAGIC - Impervius**")
    if (x==22):
      await event.edit("**MAGIC - Incendio**")
    if (x==23):
      await event.edit("**MAGIC - Levicorpus**")
    if (x==24):
      await event.edit("**MAGIC - Lumos**")
    if (x==25):
      await event.edit("**MAGIC - Muffliato**")
    if (x==26):
      await event.edit("**MAGIC - Obliviate**")
    if (x==27):
      await event.edit("**MAGIC - Petrificus Totalus**")
    if (x==28):
      await event.edit("**MAGIC - Priori Incantato**")
    if (x==29):
      await event.edit("**MAGIC - Protego**")
    if (x==30):
      await event.edit("**MAGIC - Reducto**")
    if (x==31):
      await event.edit("**MAGIC - Rennervate**")
    if (x==32):
      await event.edit("**MAGIC - Revelio**")
    if (x==33):
      await event.edit("**MAGIC - Rictusempra**")
    if (x==34):
      await event.edit("**MAGIC - Riddikulus**")
    if (x==35):
      await event.edit("**MAGIC - Scourgify**")
    if (x==36):
      await event.edit("**MAGIC - Sectumsempra**")
    if (x==37):
      await event.edit("**MAGIC - Silencio**")
    if (x==37):
      await event.edit("**MAGIC - Stupefy**")
    if (x==38):
      await event.edit("**MAGIC - Tergeo**")
    if (x==39):
      await event.edit("**MAGIC - Wingardium Leviosa**")
