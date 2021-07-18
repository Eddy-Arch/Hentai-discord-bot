#!/usr/bin/env python3
import discord, asyncio, io, colorama, random
import time, requests, nekos, sys, os, config
from discord.ext import commands
from colorama import Fore, Back, Style
from discord.ext.commands import has_permissions, CheckFailure
from config import *
from datetime import datetime
from colorama import init

init()
# set the prefix and disable the builtin help command that comes with
# discord.py

client = commands.Bot(command_prefix=conf_bot_prefix)
client.remove_command("help")

# all of the available commands sent as a message. it consists of about 5
# embedded messages with different colors. i recommend deleting this, 
# and just linking to a website for help.
@client.command()
async def help(ctx,*, reason=None):
    author = ctx.message.author
    helpembed= discord.Embed(colour=discord.Color.green())
    helpembed.set_author(name="Options")
    if nsfw_enabled == True:
        helpembed.add_field(name="+help nsfw", value = "available nsfw commands")
        helpembed.add_field(name="+help more nsfw", value = "more available nsfw\
                commands")
    helpembed.add_field(name="+help social", value = "available social\
            commands")
    helpembed.add_field(name="+help admin", value = "available admin commands")
    helpembed.add_field(name="+help misc", value = "available misc commands")
    if reason == "nsfw" and nsfw_enabled == True:
        await help_nsfw(ctx)
        return
    if reason == "more nsfw" and nsfw_enabled == True:
        await help_more_nsfw(ctx)
        return
    if reason == "social":
        await help_social(ctx)
        return
    if reason == "admin":
        await help_admin(ctx)
        return
    if reason == "misc":
        await help_misc(ctx)
        return
    await ctx.author.send(embed=helpembed)

###help commands
@client.command()
async def help_nsfw(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Color.blurple())
    embed.set_author(name="Available NSFW commands")
    embed.add_field(name="+feet", value='NSFW feet pics', inline=False)
    embed.add_field(name="+yuri", value='NSFW yuri pics', inline=False)
    embed.add_field(name="+trap", value='NSFW trap pics', inline=False)
    embed.add_field(name="+futanari",value='NSFW futanari pics', inline=False)
    embed.add_field(name="+hololewd",value='NSFW hololewd pics', inline=False)
    embed.add_field(name="+lewdkemo",value='NSFW lewdkemo pics', inline=False)
    embed.add_field(name="+solo_gif",value='NSFW solo gifs', inline=False)
    embed.add_field(name="+feet_gif",value='NSFW feet gif', inline=False)
    embed.add_field(name="+cum",value='NSFW cum on catgirls \
            pics', inline=False)
    embed.add_field(name="+erokemo", value='NSFW erokemo pics', inline=False)
    embed.add_field(name="+les", value='NSFW les pics', inline=False)
    embed.add_field(name="+wallpaper", value='cute wallpapers', inline=False)
    embed.add_field(name="+lewdk", value='NSFW lewdk pics', inline=False)
    embed.add_field(name="+neko_gif",value='cute neko pics \
            :flushed:', inline=False)
    embed.add_field(name="+meow", value='cute cat pics', inline=False)
    embed.add_field(name="+lewd",value='lewd catgirls', inline=False)
    embed.add_field(name="+gegc",value='genetically engineered catgirl\
            memes', inline=False)
    embed.add_field(name="+eroyuri",value='NSFW eroyuri', inline=False)
    embed.add_field(name="+eron",value='NSFW eron', inline=False)
    embed.add_field(name="+bj",value='NSFW bj', inline=False)
    embed.add_field(name="+nsfw_neko_gif",value='NSFW neko gif', inline=False)
    embed.add_field(name="+solo",value='NSFW solo pic', inline=False)
    embed.add_field(name="+kemonomimi",value="kemonomimi", inline =False)
    embed.add_field(name="+random",value="random hentai gif", inline =False)
    embed.add_field(name="+lesbian",value="random lesbian gif", inline =False)
    embed.add_field(name="+kuni",value="random kuni gif", inline =False)
    await ctx.author.send(embed=embed)

@client.command()
async def help_more_nsfw(ctx):
    author = ctx.message.author
    embed2 = discord.Embed(colour=discord.Color.blurple())
    embed2.set_author(name="More NSFW")
    embed2.add_field(name="+nsfw_avatar", value='NSFW avatar pic for u\
            horny virgins',inline=False)
    embed2.add_field(name="+anal", value='NSFW anal pic', inline=False)
    embed2.add_field(name="+hentai", value='NSFW hentai pic', inline=False)
    embed2.add_field(name="+avatar",value='generates a dope avatar\
            pic', inline=False)
    embed2.add_field(name="+erofeet", value='NSFW erofeet', inline=False)
    embed2.add_field(name="+pussy", value='NSFW pussy', inline=False)
    embed2.add_field(name="+tits", value='NSFW tits', inline=False)
    embed2.add_field(name="+waifu",value='waifu. self explanatory\
            you weeb', inline=False)
    embed2.add_field(name="+boobs", value='boobs', inline=False)
    embed2.add_field(name="+smallboobs", value='small boobies', inline=False)
    embed2.add_field(name="+fox_girl", value='fox girl pics', inline=False)
    embed2.add_field(name="+cat", value='cute kitty pics', inline=False)
    embed2.add_field(name="+neko", value='neko pics', inline=False)
    await ctx.author.send(embed=embed2)

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
    embed3.add_field(name="+baka",value='usage: "+baka" @user', inline=False)
    await ctx.author.send(embed=embed3)

@client.command()
async def help_admin(ctx):
    author = ctx.message.author
    embed4 = discord.Embed(colour=discord.Color.blue())
    embed4.set_author(name="Moderation")
    embed4.add_field(name="+timeban",
                     value='usage: +timeban @user [reason] [time, in seconds]\
                      (this will send them a dm notifying them that they\'ve \
                     been temporarily banned for a reason u specify)',inline=False)
    embed4.add_field(name="+kick",
                     value='usage: +kick @user [reason] (this will send them\
                     a dm notifying them that they\'ve been kicked for a reason\
                     u specify)',inline=False)
    embed4.add_field(name="+ban",
                     value='usage: +ban @user [reason] (this will send them\
                     a dm notifying them that they\'ve been banned for a \
                     reason u specify)',inline=False)
    embed4.add_field(name="+purge", value='usage: +purge <amount of messages \
                     to purge>', inline=False)
    embed4.add_field(name="+warn",
                     value='usage: +warn @user [reason] (this will send them \
                     a dm notifying them that they\'ve been warned for a  \
                     reason u specify)',inline=False)
    embed4.add_field(name="+contribute",
                     value='get the github repository link, to which you can \
                     contribute if you choose to do so (please do)',inline=False)
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
    embed5.add_field(name="+goose", value="random image of a goose")
    embed5.add_field(name="+lizard", value="random image of a lizard")
    embed5.add_field(name="+8ball", value="play 8 ball.")
    await ctx.author.send(embed=embed5)

print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + "\
    attempting to establish connection to the client")

@client.command()
async def verify(ctx, * role: discord.Role):
  user = ctx.message.author
  role = discord.utils.get(user.guild.roles, name=verify_role_name)
  await user.add_roles(role)
  await ctx.send("you've been verified")


@client.event
async def on_message(message):
    if logging_enabled == True: 
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
    else:
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
        and don\'t forget to follow the rules! to be able to chat, \
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
        await ctx.send("you must enter a reason to ban")
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
        await ctx.send("you must enter a reason to ban")
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
    role = discord.utils.get(member.guild.roles, name=mute_role_name)
    if reason == None:
        await ctx.send("you must enter a reason to mute")
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
        await ctx.send("you must enter a reason to kick")
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


# @client.command()
# async def kick(ctx, member : discord.Member, *, reason = None):
#   await ctx.member.name.send(f"kicked {member.name} for {reason} by {ctx.message.author} from {message.guild} ")
#  await member.kick(reason=reason)
# await ctx.channel.send(f"kicked {member.name} for {reason} by {ctx.message.author} ")


# @client.command()
# async def unban(ctx, *, member):
#   banned_users= await ctx.guild.bans()
#  member_name, member_discriminator = member.split("#")

# for ban_entry in banned_users:
#    user = ban_entry.user
#   if(user.name, user.discriminator) == (member_name, member_discriminator):
#   await ctx.guild.unban(user)
#  await ctx.channel.send(f"unbanned {user.name}")


####################################/////////////////////////////////////////////////////NSFW SHIT////////////////////////////////////////////////////####################################

@client.command()
async def feet(ctx):
    await nsfwimgfetchfuncs(ctx,"feet","","")

# print(Fore.WHITE + "["+ Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA+ f"{ctx.author.name} executed command !feet result: {feet}   time:{round(client.latency * 1000)}ms")

# YURI
@client.command()
async def yuri(ctx):
    await nsfwimgfetchfuncs(ctx,"yuri","","")


# traps (gay)
@client.command()
async def trap(ctx):
    await nsfwimgfetchfuncs(ctx,"trap","","")

# futanari (chicks with dicks)
@client.command()
async def futanari(ctx):
    await nsfwimgfetchfuncs(ctx,"futanari","","")

# hololewd {dk what this is either}
@client.command()
async def hololewd(ctx):
    await nsfwimgfetchfuncs(ctx,"hololewd","","")


@client.command()
async def lewdkemo(ctx):
    await nsfwimgfetchfuncs(ctx,"lewdkemo","","")


@client.command()
async def solo_gif(ctx):
    await nsfwimgfetchfuncs(ctx,"solo_gif","","")


@client.command()
async def feet_gif(ctx):
    await nsfwimgfetchfuncs(ctx,"feet_gif","","")

@client.command()
async def cum(ctx):
    await nsfwimgfetchfuncs(ctx,"cum","","")

@client.command()
async def erokemo(ctx):
    await nsfwimgfetchfuncs(ctx,"erokemo","","")


@client.command()
async def les(ctx):
    await nsfwimgfetchfuncs(ctx,"les","","")

@client.command()
async def wallpaper(ctx):
    await nsfwimgfetchfuncs(ctx,"wallpaper","","")

@client.command()
async def lewdk(ctx):
    await nsfwimgfetchfuncs(ctx,"lewdk","","")

@client.command()
async def lesbian(ctx):
    await nsfwimgfetchfuncs(ctx,"lesbian","","")

@client.command()
async def kuni(ctx):
    await nsfwimgfetchfuncs(ctx,"kuni","","")

@client.command()
async def neko_gif(ctx):
    await imgfetchfuncs(ctx,"neko_gif","","")


@client.command()
async def meow(ctx):
    await imgfetchfuncs(ctx,"meow","","")

@client.command()
async def baka(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "baka", "doesnt think much of", member, reason)

@client.command()
async def tickle(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "tickle", "tickled", member, reason)


@client.command()
async def lewd(ctx):
    await nsfwimgfetchfuncs(ctx, "lewd", "","")


@client.command()
async def feed(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "feed", "fed", member, reason)


@client.command()
async def gecg(ctx):
    await imgfetchfuncs(ctx,"gecg","","")

@client.command()
async def goose(ctx):
    await imgfetchfuncs(ctx,"goose","","")

@client.command()
async def lizard(ctx):
    await imgfetchfuncs(ctx,"lizard","","")

@client.command()
async def eroyuri(ctx):
    await nsfwimgfetchfuncs(ctx,"eroyuri", "", "")


@client.command()
async def eron(ctx):
    await nsfwimgfetchfuncs(ctx,"eron", "", "")


@client.command()
async def bj(ctx):
    await nsfwimgfetchfuncs(ctx,"bj", "", "")


@client.command()
async def nsfw_neko_gif(ctx):
    await nsfwimgfetchfuncs(ctx,"nsfw_neko_gif", "", "")


@client.command()
async def solo(ctx):
    await nsfwimgfetchfuncs(ctx,"solo", "", "")


@client.command()
async def kemonomimi(ctx):
    await nsfwimgfetchfuncs(ctx,"kemonomimi", "", "")



@client.command()
async def gasm(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "gasm", "is in awe with", member, reason)


@client.command()
async def nsfw_avatar(ctx):
    await nsfwimgfetchfuncs(ctx, "nsfw_avatar", "", "")


@client.command()
async def poke(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "poke", "poked",  member, reason)
@client.command()
async def anal(ctx):
    await nsfwimgfetchfuncs(ctx, "anal", "", "")


@client.command()
async def slap(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "slap", "slapped", member, reason)


@client.command()
async def hentai(ctx):
    await nsfwimgfetchfuncs(ctx,"hentai","","")


@client.command()
async def avatar(ctx):
    await imgfetchfuncs(ctx,"avatar","","")


@client.command()
async def erofeet(ctx):
    await nsfwimgfetchfuncs(ctx,"erofeet","","")


@client.command()
async def pussy(ctx):
    await nsfwimgfetchfuncs(ctx,"pussy","","")


@client.command()
async def tits(ctx):
    await nsfwimgfetchfuncs(ctx,"tits","","")


@client.command()
async def waifu(ctx):
    await imgfetchfuncs(ctx,"waifu","","")


@client.command()
async def boobs(ctx):
        await nsfwimgfetchfuncs(ctx,"boobs","","")


@client.command()
async def smallboobs(ctx):
    await nsfwimgfetchfuncs(ctx,"smallboobs","","")


@client.command()
async def pat(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"pat","patted", member, reason)


@client.command(pass_context=True)
async def kiss(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"kiss","kissed", member, reason)


@client.command()
async def spank(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"spank","spanked", member, reason)


@client.command()
async def cuddle(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"cuddle","is cuddling with", member, reason)


@client.command()
async def hug(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"hug","hugged", member, reason)


@client.command()
async def foxgirl(ctx):
    await imgfetchfuncs(ctx, "fox_girl", "", "fox girls > all")



@client.command()
async def contribute(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='contribution',
        description='contribution to the project is always welcome, feel free to contribute, edit, clean up, document and improve the source code at: https://github.com/Eddy-Arch/hentai-discord-bot',
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

@client.command()
async def eightball(ctx,*, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    author = ctx.message.author


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    text = nekos.eightball()
    #print(text)
    embed.add_field(name=text[0:256], value='‎', inline=False)
    await ctx.send(embed=embed)


# 2b2t alterations
@client.command()
async def queuepeak(ctx,*, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    r = requests.get('https://rebane2001.com/queuepeek/data.json')
    embed.set_author(name="2B2T queue status")
    embed.add_field(name='in queue right now:', value=r.json()['queuepos'], inline=False)
    embed.add_field(name='time to wait', value=r.json()['queueest'], inline=False)
    if reason == "players":
        embed.add_field(name='fart', value=r.json()['players'][0]['name'][0:220], inline=False)
    await ctx.send(embed=embed)


 # image fetch style commands
@client.command()
async def neko(ctx):
    await imgfetchfuncs(ctx, "neko", "", "")

@client.command()
async def smug(ctx):
    await imgfetchfuncs(ctx, "smug", "smug", "smug doe")

async def imgfetchfuncs(ctx, img_endpoint, title, description):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Color.from_rgb(r, g, b)
    )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command {conf_bot_prefix}{title} result: {img}   time:{round(client.latency * 1000)}ms")

async def nsfwimgfetchfuncs(ctx,img_endpoint,title,description):
    if not nsfw_enabled == True:
        return
    if not ctx.channel.is_nsfw():
        error_embed = discord.Embed(
            colour=discord.Colour.red()
        )
        error_embed.add_field(name="Error", value="You tried running an __**NSFW**__ channel only command in a non __**NSFW**__ channel.\nsorry for the inconvience this might have caused, have a neko.")
        error_img = nekos.img("neko")
        error_embed.set_image(url=error_img)
        await ctx.author.send(embed=error_embed)
        await ctx.message.delete()
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.from_rgb(r, g, b)
        )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")

async def socialfuncs(ctx,img_endpoint, action, member, arg=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    await ctx.message.delete()
    if arg != "":
        embed = discord.Embed(
            title=f"{ctx.message.author} {action} {member.name}",
            description=f'{ctx.message.author.name}: {arg}',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    else:
        embed = discord.Embed(
            title=f"{ctx.message.author} {action} {member.name} {arg}",
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )

    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")
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
