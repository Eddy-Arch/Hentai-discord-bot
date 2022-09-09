#!/usr/bin/env python3
import discord, asyncio, io, colorama, random
import time, requests, nekos, sys, os, config
from discord.ext import commands
from colorama import Fore, Back, Style
from discord.ext.commands import has_permissions, CheckFailure
from config import *
from datetime import datetime
from colorama import init
from scripts.txt2img2 import draw_image

init()
# set the prefix and disable the builtin help command that comes with
# discord.py
client = commands.Bot(command_prefix=conf_bot_prefix,intents=discord.Intents.default())
client.remove_command("help")

# all of the available commands sent as a message. it consists of about 5
# embedded messages with different colors. i recommend deleting this, 
# and just linking to a website for help.
@client.command()
async def imggen(ctx,*, reason=None):
    author = ctx.message.author
    helpembed= discord.Embed(colour=discord.Color.green())
    helpembed.set_author(name="Options")
    helpembed.add_field(name="test", value = "test")
#    embed.set_image(url=draw_image(reason))
    await ctx.author.send(embed=helpembed)
# dummy token in here, well its a dummy now. appearantly discord has a web crawler that found my bots token in here. pretty damn cool.
client.run(token)

#br
# this is the animation that gets played in case of a crash, error, dyno error etc. if you are running this from windows, i recommend replacing "clear" with "cls" to avoid a visual bug, reminding you that the clear command is unix like only. the t == 3 LOC means the amount of times the animation will repeat before terminating the application.
t = 0
while t != 10:
    print("died")
    time.sleep(1)
    os.system("clear")
    print("died.")
    time.sleep(1)
    os.system("clear")
    print("died..")
    time.sleep(1)
    os.system("clear")
    print("died...")
    time.sleep(1)
    os.system("clear")
    print("died..")
    time.sleep(1)
    os.system("clear")
    print("died.")
    time.sleep(1)
    os.system("clear")
    t+= 1
    if(t == 3):
        exit()
