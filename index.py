import discord
import asyncio
import io
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import random
import time
import requests
import nekos
from discord.ext.commands import has_permissions, CheckFailure
import sys
import os
import config
from config import token, admin_actions_log_channel_id
from config import general_actions_log_channel_id
from config import verify_role_name, conf_bot_prefix
from config import mute_role_name
from datetime import datetime
from colorama import init

init()
# set the preifx and disable the builtin help command that comes with
# discord.py

client = commands.Bot(command_prefix=conf_bot_prefix)
client.remove_command("help")

# all of the available commands sent as a message. it consists of about 5
# embedded messages with different colors. i recommend deleting this, 
# and just linking to a website for help.
@client.command()
async def help(ctx):
    author = ctx.message.author
    helpembed= discord.Embed(colour=discord.Color.green())
    helpembed.set_author(name="Options")
    helpembed.add_field(name="+help_social", value = "available social commands")
    helpembed.add_field(name="+help_admin", value = "available admin commands")
    helpembed.add_field(name="+help_misc", value = "available misc commands")
    await ctx.author.send(embed=helpembed)

@client.command()
async def help_social(ctx):
    author = ctx.message.author
    embed3 = discord.Embed(colour=discord.Color.magenta())
    embed3.set_author(name="Social")
    embed3.add_field(name="+tickle",value='usage: +tickle @user tickle tickle', inline=False)
    embed3.add_field(name="+feed",value='usage: +feed @user eat up fatty', inline=False)
    embed3.add_field(name="+gasm",value='usage: +gasm @user no way dude', inline=False)
    embed3.add_field(name="+poke",value='usage: +poke @user beep', inline=False)
    embed3.add_field(name="+slap",value='usage: +slap @user u cunt', inline=False)
    embed3.add_field(name="+pat",value='usage: +pet @user u cutie', inline=False)
    embed3.add_field(name="+kiss",value='usage: +kiss @user muah (no homo)', inline=False)
    embed3.add_field(name="+spank",value='usage: +spank @user BRUH', inline=False)
    embed3.add_field(name="+cuddle",value='usage: +cuddle @user u cutie', inline=False)
    embed3.add_field(name="+hug",value='usage: +hug @user u cutie', inline=False)
    embed3.add_field(name="+owoify",value='usage: "owoifys" some text', inline=False)
    await ctx.author.send(embed=embed3)

@client.command()
async def help_admin(ctx):
    author = ctx.message.author
    embed4 = discord.Embed(colour=discord.Color.blue())
    embed4.set_author(name="Moderation")
    embed4.add_field(name="+timeban",
                     value='usage: +timeban @user [reason] [time, in seconds]\
                      (this will send them a dm notifying them that theyve \
                     been temporarily banned for a reason u specify)',inline=False)
    embed4.add_field(name="+kick",
                     value='usage: +kick @user [reason] (this will send them\
                     a dm notifying them that theyve been kicked for a reason\
                     u specify)',inline=False)
    embed4.add_field(name="+ban",
                     value='usage: +ban @user [reason] (this will send them\
                     a dm notifying them that theyve been banned for a \
                     reason u specify)',inline=False)
    embed4.add_field(name="+purge", value='usage: +purge <amount of messages \
                     to purge>', inline=False)
    embed4.add_field(name="+warn",
                     value='usage: +warn @user [reason] (this will send them \
                     a dm notifying them that theyve been warned for a  \
                     reason u specify)',inline=False)
    embed4.add_field(name="+contribute",
                     value='get the github repository link, to which you can \
                     contribute if you choose to do so. (please do)',inline=False)
    embed4.add_field(name="+mute",
                     value='usage: +mute [mute rolename] @user [time can be \
                     represented like 1m ( for one minute) or 1h \
                     (for one hour)] [reason]',inline=False)
    await ctx.author.send(embed=embed4)

@client.command()
async def help_misc(ctx):
    author = ctx.message.author
    embed5 = discord.Embed(colour=discord.Color.red())
    embed5.set_author(name="Misc")
    embed5.add_field(name="+wordsfromgod", value='gives you a list of random \
                     words, which are the words of god. inspired by terry \
                     a davis, RIP.')
    embed5.add_field(name="+coronavirus", value = 'usage: !coronavirus \
                     <country>. gives you the current world stats o\
                     f the pandemic')
    await ctx.author.send(embed=embed5)

print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + "\
    attempting to establish connection to the client")

@client.event
async def on_ready():
    print("")

@client.command()
async def verify(ctx, * role: discord.Role):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name=verify_role_name)
  await user.add_roles(role)
  await ctx.send("you've been verified ")


@client.event
async def on_message(message):
    with io.open("chatlogs.txt", "a", encoding="utf-8") as f:
        f.write(
            "[{}] | [{}] | [{}] @ {}: {}\n".format(message.guild,
                                                   message.channel,
                                                   message.author,
                                                   message.created_at,
                                                   message.content))
    f.close()
    print(
        Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]"
        + Fore.LIGHTRED_EX + "[{}] | [{}] | [{}] @ {}: {}".format(
            message.guild, message.channel, message.author,
            message.created_at, message.content))

    await client.process_commands(message)


@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://twitch.tv/epic",
                                 name=f"+help | helping {len(client.guilds)} \
                                 guilds!")
    await client.change_presence(status=discord.Status.idle,
                                 activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN
        + " connection established, logged in as: " + client.user.name)


@client.event
async def on_member_join(member):
    print(f'{member} has joined')
    embed = discord.Embed(
        title='Hello there!',
        description=f'thanks for joining {member}! have a good time,\
        and dont forget to follow the rules! to be able to chat, \
        please type ```+verify``` in the #verify-me channel',
        colour=discord.Colour.blurple()
    )
    channel = discord.utils.get(member.guild.channels, name=welcome_message_channel_name)
    bruh = member.avatar_url

    embed.set_image(url=bruh)

    await member.send(embed=embed)
    await channel.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is \
                   {round(client.latency * 1000)}ms")
    print(
        Fore.WHITE + "[" + Fore.YELLOW + '+' + Fore.WHITE + "]"
        + Fore.YELLOW + f"{ctx.author.name} executed command \
        !ping result:{round(client.latency * 1000)}ms ")

# purge command
@client.command(pass_context=True)
async def purge(ctx, amount=5):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members and amount < 1000:
        await ctx.channel.purge(limit=amount)
        await ctx.author.send(f"purged {amount} messages.")
        channel = client.get_channel(general_actions_log_channel_id)
        await channel.send(str(ctx.message.author)+ " " + f"just purged {amount} messages! ")


@client.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    admin = ctx.message.author.guild_permissions.administrator
    banperm = ctx.message.author.guild_permissions.ban_members
    if reason == None:
        await ctx.send("you must enter a reason to warn")
    else:
        try:
            if admin or banperm:
                message = f"You have been warned from `` {ctx.guild.name} ``\
                    by `` {ctx.message.author} `` for `` {reason} ``"
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="WARNED",
                                value=message,
                                inline=False)
                await member.send(embed=embed)
                embed = discord.Embed(title=
                                      "User was warned for {}".format(reason),
                                      description="**{}** has been warned!"
                                      .format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author,
                                 icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=embed)
                author = ctx.message.author
                channel = client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just warned {member} for {reason} ")
            else:
                embed = discord.Embed(title="Permission Denied.",
                                      description="You don't have \
                                      permission to use this command.",
                                      color=discord.Color.red())
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="Permission Denied.",
                                  description="Bot doesn't have correct \
                                  permissions, or bot can't ban this user.",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)




@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    admin = ctx.message.author.guild_permissions.administrator
    banperm = ctx.message.author.guild_permissions.ban_members

    if reason == None:
        await ctx.send("you must enter a reason to ban.")
    else:
        try:
            if admin or banperm:
                message = f"You have been banned from `` {ctx.guild.name} `` by `` {ctx.message.author} `` for `` {reason}``"
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="BANNED",
                                value=message,
                                inline=False)
                await member.send(embed=embed)
                await ctx.guild.ban(member)
                embed = discord.Embed(title="User banned was banned for {}".format(reason),
                                      description="**{}** has been banned!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=embed)
                author = ctx.message.author
                channel = client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just banned {member} for {reason}")
            else:
                embed = discord.Embed(title="Permission Denied.",
                                      description="You don't have permission to use this command.",
                                      color=discord.Color.red())
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="Permission Denied.",
                                  description="Bot doesn't have correct permissions, or bot can't ban this user.",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
##time ban
now = datetime.now()
@client.command(pass_context=True)
async def timeban(ctx, member: discord.Member, time = None, *, reason=None, ):
    if reason == None:
        await ctx.send("you must enter a reason to ban.")
    if time == None:
        await ctx.send("you must enter the time (in seconds) a user should be banned for")
    else:
        try:
            if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
                message = f"You have been warned from {ctx.guild.name} by {ctx.message.author} for {reason}"
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="BANNED",
                                #timemsg = time.strftime('%H:%M:%S', time)
                                value=f'You have been temporarily banned from `` {ctx.guild.name} `` by `` {ctx.message.author} `` for `` {reason}. You will be unbanned in {time} ``',
                                inline=False)
                await member.send(embed=embed)
                await ctx.guild.ban(member)
                embed = discord.Embed(title="User banned was banned for {}".format(reason),
                                      description="**{}** has been banned!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

            if "m" in time:
                print("inital time: " + time)
                m_bantime = time.replace("m", "")
                await ctx.send(embed=embed)
                author = ctx.message.author
                channel = client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just banned {member} for {reason}")
                await asyncio.sleep(int(m_bantime) * 60)
                print(f"{author} just unbanned {member} for {reason}")
                await ctx.guild.unban(member)
                print(time + "is up")
            ###
            if "h" in time:
                print("inital time: " + time)
                h_bantime = time.replace("h", "")
                await ctx.send(embed=embed)
                author = ctx.message.author
                channel = client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just banned {member} for {reason}")
                await asyncio.sleep(int(h_bantime) * 3600)
                print(f"{author} just unbanned {member} for {reason}")
                await ctx.guild.unban(member)
        except:
            embed = discord.Embed(title="Permission Denied.",
                                description="Bot doesn't have correct permissions, or bot can't ban this user.",
                                color=discord.Color.red())

@client.command(pass_context=True)
async def mute(ctx, role: discord.Role, member: discord.Member, time = None, *, reason=None):
    role = discord.utils.get(member.guild.roles, name="muted")
    if reason == None:
        await ctx.send("you must enter a reason to mute.")
    if time == None:
        await ctx.send("you must enter the time (in seconds) a user should be muted for")
    else:
        try:
            if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
                message = f"You have been muted in {ctx.guild.name} by {ctx.message.author} for {reason}"
                unmute_message=f'You have been unmuted in `` {ctx.guild.name} ``. You were muted by `` {ctx.message.author} `` for `` {reason}. You were muted for {time} ``',
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="MUTED",
                                #timemsg = time.strftime('%H:%M:%S', time)
                                value=f'You have been temporarily muted from `` {ctx.guild.name} `` by `` {ctx.message.author} `` for `` {reason}. You will be unmuted in {time} ``',
                                inline=False)
                await member.send(embed=embed)
                await member.add_roles(role)
                embed = discord.Embed(title="User was muted for {}".format(reason),
                                      description="**{}** has  been muted!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

            if "m" in time:
                print("inital time: " + time)
                m_mutetime = time.replace("m", "")
                await ctx.send(embed=embed)
                author = ctx.message.author
                channel = client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just muted {member} for {reason}")
                await asyncio.sleep(int(m_mutetime) * 60)
                print(f"{author} just muted {member} for {reason}")
                await member.remove_roles(role)
                print(time + "is up")
                unmute_embed = discord.Embed(
                    colour=discord.Color.red()
                )
                unmute_embed.add_field(name="MUTED",
                                #timemsg = time.strftime('%H:%M:%S', time)
                                value=unmute_message,
                                inline=False)
                await member.send(embed=unmute_embed)
            ###
            if "h" in time:
                print("inital time: " + time)
                h_mutetime = time.replace("h", "")
                await ctx.send(embed=embed)
                author = ctx.message.author
                channel = client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just muted {member} for {reason}")
                await asyncio.sleep(int(h_mutetime) * 3600)
                print(f"{author} just unbanned {member} for {reason}")
                await user.remove_roles(member)

        except:
            embed = discord.Embed(title="Permission Denied.",
                                description="Bot doesn't have correct permissions, or bot can't ban this user.",
                                color=discord.Color.red())


@client.command(pass_context=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send("you must enter a reason to kick.")
    else:
        try:
            if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="KICKED",
                                value=f'You have been kicked from `` {ctx.guild.name} `` by  `` {ctx.message.author} `` for  `` {reason} ``',
                                inline=False)
                await member.send(embed=embed)
                reason = reason
                await ctx.guild.kick(member)
                embed = discord.Embed(title="User kicked was kicked for {}".format(reason),
                                      description="**{}** has been kicked!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=embed)
                author = ctx.message.author
                channel =client.get_channel(admin_actions_log_channel_id)
                await channel.send(f"{author} just kicked {member} for {reason}")
            else:
                embed = discord.Embed(title="Permission Denied.",
                                      description="You don't have permission to use this command.",
                                      color=discord.Color.red())
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="Permission Denied.",
                                  description="Bot doesn't have correct permissions, or bot can't kick this user.",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)



@client.command()
async def feet(ctx):
    try:
        author = ctx.message.author
        if not ctx.channel.is_nsfw():
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object

    except:
        print(bruh)
        print(bruh)

    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='feet doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    feet = nekos.img("feet")

    embed.set_image(url=feet)

    await ctx.send(embed=embed)


# print(Fore.WHITE + "["+ Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA+ f"{ctx.author.name} executed command !feet result: {feet}   time:{round(client.latency * 1000)}ms")

# YURI
@client.command()
async def yuri(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='yuri doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    yur1 = nekos.img("yuri")

    embed.set_image(url=yur1)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !yuri result: {yur1}   time:{round(client.latency * 1000)}ms")


# traps (gay)
@client.command()
async def trap(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        author = ctx.message.author
        embed = discord.Embed(
            title='traps are gay',
            description='',
            colour=discord.Colour.from_rgb(r , g, b)
        )
    trap = nekos.img("trap")

    embed.set_image(url=trap)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !trap result: {trap}   time:{round(client.latency * 1000)}ms")


# futanari {tbh dont know what this is}
@client.command()
async def futanari(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        embed = discord.Embed(
            title='futanari doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    futanari = nekos.img("futanari")

    embed.set_image(url=futanari)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !futanari result: {futanari}   time:{round(client.latency * 1000)}ms")


# holowed {dk what this is either}
@client.command()
async def hololewd(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        embed = discord.Embed(
            title='hololewd doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r , g, b)
        )
    hololewd = nekos.img("hololewd")

    embed.set_image(url=hololewd)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hololewd result: {hololewd}   time:{round(client.latency * 1000)}ms")


@client.command()
async def lewdkemo(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='lewdkemo doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    lewdkemo = nekos.img("lewdkemo")

    embed.set_image(url=lewdkemo)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !lewdkemo result: {lewdkemo}   time:{round(client.latency * 1000)}ms")


##################
@client.command()
async def solo_gif(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=':flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    solog = nekos.img("solog")

    embed.set_image(url=solog)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !solog result: {solog}   time:{round(client.latency * 1000)}ms")


#######################
@client.command()
async def feet_gif(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='feet :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    feetg = nekos.img("feetg")

    embed.set_image(url=feetg)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !feetg result: {feetg}   time:{round(client.latency * 1000)}ms")


#####################
@client.command()
async def cum(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='cum :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    cum = nekos.img("cum")

    embed.set_image(url=cum)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !cum result: {cum}   time:{round(client.latency * 1000)}ms")


##################################
@client.command()
async def erokemo(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='erokemo :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    erokemo = nekos.img("erokemo")

    embed.set_image(url=erokemo)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !erokemo result: {erokemo}   time:{round(client.latency * 1000)}ms")


#########################################
@client.command()
async def les(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='les :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    les = nekos.img("les")

    embed.set_image(url=les)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !les result: {les}   time:{round(client.latency * 1000)}ms")


######################################
@client.command()
async def wallpaper(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='wallpaper :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    wallpaper = nekos.img("wallpaper")

    embed.set_image(url=wallpaper)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !wallpaper result: {wallpaper}   time:{round(client.latency * 1000)}ms")


###############################################################

@client.command()
async def lewdk(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='lewdk :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    lewdk = nekos.img("lewdk")

    embed.set_image(url=lewdk)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !lewdk result: {lewdk}   time:{round(client.latency * 1000)}ms")


############################################################
@client.command()
async def neko_gif(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='ngif :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g ,b)
    )
    ngif = nekos.img("ngif")

    embed.set_image(url=ngif)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !ngif result: {ngif}   time:{round(client.latency * 1000)}ms")


############################################################


###########################################################
@client.command()
async def tickle(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} tickled {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    tickle = nekos.img("tickle")

    embed.set_image(url=tickle)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !tickle result: {tickle}   time:{round(client.latency * 1000)}ms")


###########################################################


###################################################################
@client.command()
async def feed(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} fed {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    feed = nekos.img("feed")

    embed.set_image(url=feed)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !feed result: {feed}   time:{round(client.latency * 1000)}ms")


################################################################

@client.command()
async def gasm(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} is in awe with {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g ,b)
    )
    gasm = nekos.img("gasm")

    embed.set_image(url=gasm)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !gasm result: {gasm}   time:{round(client.latency * 1000)}ms")


####################################################################
#######################################################################
@client.command()
async def poke(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} poked {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    poke = nekos.img("poke")

    embed.set_image(url=poke)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !poke result: {poke}   time:{round(client.latency * 1000)}ms")


######################################################################
@client.command()
async def slap(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} slapped {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    slap = nekos.img("slap")

    embed.set_image(url=slap)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !slap result: {slap}   time:{round(client.latency * 1000)}ms")



#######################################################################################################################################
@client.command()
async def pat(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} patted {member.name}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    pat = nekos.img("pat")

    embed.set_image(url=pat)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !pat result: {pat}   time:{round(client.latency * 1000)}ms")


#####################################################################################################################################
@client.command()
async def kiss(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} kissed {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    kiss = nekos.img("kiss")

    embed.set_image(url=kiss)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !kiss result: {kiss}   time:{round(client.latency * 1000)}ms")


#######################################################################################################################################
@client.command()
async def spank(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} spanked {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    spank = nekos.img("spank")

    embed.set_image(url=spank)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !spank result: {spank}   time:{round(client.latency * 1000)}ms")


#######################################################################################################################################
@client.command()
async def cuddle(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} cuddled {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    cuddle = nekos.img("cuddle")

    embed.set_image(url=cuddle)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !cuddle result: {cuddle}   time:{round(client.latency * 1000)}ms")


########################################################################################################################################
@client.command()
async def hug(ctx, member: discord.Member, *, reason=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} hugged {member.name} {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    hug = nekos.img("hug")

    embed.set_image(url=hug)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hug result: {hug}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def fox_girl(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    fox_girl = nekos.img("fox_girl")

    embed.set_image(url=fox_girl)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !fox_girl result: {fox_girl}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def neko(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' nekos:flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    neko = nekos.img("neko")

    embed.set_image(url=neko)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !neko result: {neko}   time:{round(client.latency * 1000)}ms")


@client.command()
async def contribute(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='contributon',
        description='contribution to the project is always welcome, feel free to contribute, edit, ,clean up, document, and improve the source code at: https://github.com/Eddy-Arch/hentai-discord-bot',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    neko = nekos.img("neko")

    embed.set_image(url=neko)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !neko result: {neko}   time:{round(client.latency * 1000)}ms")

@client.command()
async def wordsfromgod(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    author = ctx.message.author
    word_site = "https://www.wordgenerator.net/application/p.php?id=dictionary_words&type=1&spaceflag=true"

    response = requests.get(word_site)
    wordy = response.content.decode()
    bruh = wordy.replace(",", " ")


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    embed.set_author(name="God says:")
    embed.add_field(name=bruh[0:256], value='This command was inspired by Terry A. davis. RIP.', inline=False)
    await ctx.send(embed=embed)



@client.command()
async def coronavirus(ctx, reason="None"):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    author = ctx.message.author


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    r = requests.get('https://corona-stats.online/' + reason + '?format=json')
    stats = r.json()['data'][0]['country'], r.json()['data'][0]['cases']
    embed.set_author(name=r.json()['data'][0]['country'])
    embed.add_field(value='cases:', name="===========================", inline=False)
    embed.add_field(value='cases today:', name=r.json()['data'][0]['cases'], inline=False)
    embed.add_field(value="recovered:", name=r.json()['data'][0]['todayCases'], inline=False)
    embed.add_field(value="deaths:", name=r.json()['data'][0]['recovered'], inline=False)
    embed.add_field(value="died today:", name=r.json()['data'][0]['deaths'], inline=False)
    embed.add_field(value="active:", name=r.json()['data'][0]['todayDeaths'], inline=False)
    embed.add_field(value="critical condition:", name=r.json()['data'][0]['active'], inline=False)
    world = "-=worldwide=- cases:", r.json()['worldStats']['cases'], " cases today: ", r.json()['worldStats']['todayCases'] , " deaths: ", r.json()['worldStats']['deaths'], " died today", r.json()['worldStats']['todayDeaths'], " recovered: ", r.json()['worldStats']['recovered'], " critical: ", r.json()['worldStats']['critical'], " cases per one million: ", r.json()['worldStats']['casesPerOneMillion']
    embed.add_field(value=world, name=r.json()['data'][0]['critical'], inline=False)
    embed.set_author(name=r.json()['data'][0]['country'], icon_url=r.json()['data'][0]['countryInfo']['flag'])
    await ctx.send(embed=embed)



#this command takes in a string and "owoifys" it
@client.command()
async def owoify(ctx,*, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    author = ctx.message.author


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    text = nekos.owoify(reason)
    #print(text)
    embed.add_field(name=text[0:256], value='‎', inline=False)
    await ctx.send(embed=embed)


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

