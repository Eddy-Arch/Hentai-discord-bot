import discord
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

##commited from arch linux belive it or not i know this is mega swagg innit
from colorama import init

init()
#set the preifx and disable the builtin help command that comes with discord.py
client = commands.Bot(command_prefix="+")
client.remove_command("help")

#all of the available commands sent as a message. it consists of about 5 embedded messages with different colors. i recommend deleting this, and just linking to a website for help.
@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Color.purple()
    )

    embed2 = discord.Embed(
        colour=discord.Color.blurple()
    )

    embed3 = discord.Embed(
        colour=discord.Color.magenta()
    )

    embed4 = discord.Embed(
        colour=discord.Color.blue()
    )
    embed5 = discord.Embed(
        colour=discord.Color.red()
    )

    embed5.set_author(name="Misc")
    embed.set_author(name="Available NSFW commands")
    embed.add_field(name="+feet", value='NSFW feet pics', inline=False)
    embed.add_field(name="+yuri", value='NSFW yuri pics', inline=False)
    embed.add_field(name="+trap", value='NSFW trap pics', inline=False)
    embed.add_field(name="+futanari", value='NSFW futanari pics', inline=False)
    embed.add_field(name="+hololewd", value='NSFW hololewd pics', inline=False)
    embed.add_field(name="+lewdkemo", value='NSFW lewdkemo pics', inline=False)
    embed.add_field(name="+solo_gif", value='NSFW solo gifs', inline=False)
    embed.add_field(name="+feet_gif", value='NSFW feet gif', inline=False)
    embed.add_field(name="+cum", value='NSFW cum on catgirls pics', inline=False)
    embed.add_field(name="+erokemo", value='NSFW erokemo pics', inline=False)
    embed.add_field(name="+les", value='NSFW les pics', inline=False)
    embed.add_field(name="+wallpaper", value='cute wallpapers', inline=False)
    embed.add_field(name="+lewdk", value='NSFW lewdk pics', inline=False)
    embed.add_field(name="+neko_gif", value='cute neko pics :flushed:', inline=False)
    embed.add_field(name="+meow", value='cute cat pics', inline=False)
    embed3.add_field(name="+tickle", value='usage: +tickle @user tickle tickle', inline=False)
    embed.add_field(name="+lewd", value='lewd catgirls', inline=False)
    embed3.add_field(name="+feed", value='usage: +feed @user eat up fatty', inline=False)
    embed.add_field(name="+gegc", value='genetically engineerd catgirl memes', inline=False)
    embed.add_field(name="+eroyuri", value='NSFW eroyuri', inline=False)
    embed.add_field(name="+eron", value='NSFW eron', inline=False)
    embed.add_field(name="+bj", value='NSFW bj', inline=False)
    embed.add_field(name="+nsfw_neko_gif", value='NSFW neko gif', inline=False)
    embed.add_field(name="+solo", value='NSFW solo pic', inline=False)
    embed.add_field(name="+kemonomimi", value='NSFW kemonomimi pic', inline=False)
    embed2.add_field(name="+nsfw_avatar", value='NSFW avatar pic for u horny virgins', inline=False)
    embed3.add_field(name="+gasm", value='usage: +gasm @user no way dude', inline=False)
    embed3.add_field(name="+poke", value='usage: +poke @user beep', inline=False)
    embed3.add_field(name="+slap", value='usage: +slap @user u cunt', inline=False)
    embed2.add_field(name="+anal", value='NSFW anal pic', inline=False)
    embed2.add_field(name="+hentai", value='NSFW hentai pic', inline=False)
    embed2.add_field(name="+avatar", value='generates a dope avatar pic', inline=False)
    embed2.add_field(name="+erofeet", value='NSFW erofeet', inline=False)
    embed2.add_field(name="+pussy", value='NSFW pussy', inline=False)
    embed2.add_field(name="+tits", value='NSFW tits', inline=False)
    embed2.add_field(name="+waifu", value='waifu. self explanotory you weeb', inline=False)
    embed2.add_field(name="+boobs", value='boobs', inline=False)
    embed2.add_field(name="+smallboobs", value='smallboobies ', inline=False)
    embed3.add_field(name="+pat", value='usage: +pet @user u cutie', inline=False)
    embed3.add_field(name="+kiss", value='usage: +kiss @user muah (no homo)', inline=False)
    embed3.add_field(name="+spank", value='usage: +spank @user BRUH', inline=False)
    embed3.add_field(name="+cuddle", value='usage: +cuddle @user u cutie', inline=False)
    embed3.add_field(name="+hug", value='usage: +hug @user u cutie', inline=False)
    embed2.add_field(name="+fox_girl", value='fox girl pics', inline=False)
    embed2.add_field(name="+cat", value='cute kitty pics', inline=False)
    embed2.add_field(name="+neko", value='neko pics', inline=False)
    embed3.add_field(name="+owoify", value='usage: "owoifys" some text', inline=False)
    embed4.set_author(name="Moderation")
    embed3.set_author(name="Social")
    embed2.set_author(name="More NSFW")
    embed4.add_field(name="+kick",
                     value='usage: +kick @user [reason] (this will send them a dm notifying them that theyve been kicked for a reason u specify)',
                     inline=False)
    embed4.add_field(name="+ban",
                     value='usage: +ban @user [reason] (this will send them a dm notifying them that theyve been banned for a reason u specify)',
                     inline=False)
    embed4.add_field(name="+purge", value='usage: +purge <amount of messages to purge>', inline=False)
    embed4.add_field(name="+warn",
                     value='usage: +warn @user [reason] (this will send them a dm notifying them that theyve been warned for a reason u specify)',
                     inline=False)
    embed4.add_field(name="+contribute",
                     value='get the github repository link, to which you can contribute if you choose to do so. (please do)',
                     inline=False)
    embed5.add_field(name="+wordsfromgod", value='gives you a list of random words, which are the words of god. inspired by terry a davis, RIP.')
    embed5.add_field(name="+coronavirus", value = 'usage: !coronavirus <country>. gives you the current world stats of the pandemic')

    await ctx.author.send(embed=embed)
    await ctx.author.send(embed=embed2)
    await ctx.author.send(embed=embed3)
    await ctx.author.send(embed=embed4)
    await ctx.author.send(embed=embed5)


# fox_girl


print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + " attempting to establish connection to the client")


@client.event
async def on_ready():
    print("")


@client.command()
async def verify(ctx, * role: discord.Role):
  user = ctx.message.author
  #role = discord.utils.get(user.guild.roles, name="poop")
  role = discord.utils.get(user.guild.roles, name='Verified')
  await user.add_roles(role)

    
@client.command()
async def info(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Color.purple()
    )
    embed.set_author(name="Info")
    embed.add_field(name="Creator:", value='Eddy#4792', inline=False)
    embed.add_field(name="Website:", value='https://hentai-distributor.glitch.me/', inline=False)
    embed.add_field(name="Purpouse:", value='to give cute catgirls (foxgirls are better doe)', inline=False)
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    with io.open("bruhgaming78.txt", "a", encoding="utf-8") as f:
        f.write(
            "[{}] | [{}] | [{}] @ {}: {}\n".format(message.guild, message.channel, message.author, message.created_at,
                                                   message.content))
    f.close()
    print(
        Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]" + Fore.LIGHTRED_EX + "[{}] | [{}] | [{}] @ {}: {}".format(
            message.guild, message.channel, message.author,
            message.created_at, message.content))

    await client.process_commands(message)


@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://twitch.tv/epic",
                                 name=f"+help | helping {len(client.guilds)} guilds!")
    await client.change_presence(status=discord.Status.idle, activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established, logged in as: " + client.user.name)


@client.event
async def on_member_join(member):
    print(f'{member} has joined')
    embed = discord.Embed(
        title='New Member joined',
        description=f'thanks for joining {member}! have a good time, and dont forget to follow the rules!',
        colour=discord.Colour.blurple()
    )
    channel = discord.utils.get(member.guild.channels, name="general")
    bruh = member.avatar_url

    embed.set_image(url=bruh)

    await member.send(embed=embed)
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    print(f'{member} has left')


@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")
    print(
        Fore.WHITE + "[" + Fore.YELLOW + '+' + Fore.WHITE + "]" + Fore.YELLOW + f"{ctx.author.name} executed command !ping result:{round(client.latency * 1000)}ms ")


@client.command()
async def helpme(ctx):
    await ctx.send(f"gaming connection speed is {round(client.latency * 1000)}ms")
    print(
        Fore.WHITE + "[" + Fore.YELLOW + '+' + Fore.WHITE + "]" + Fore.YELLOW + f"{ctx.author.name} executed command !ping result:{round(client.latency * 1000)}ms ")


# shit
@client.command(pass_context=True)
async def purge(ctx, amount=5):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
        await ctx.channel.purge(limit=amount)
        await ctx.author.send(f"purged {amount} messages.")


@client.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send("you must enter a reason to warn")
    else:
        try:
            if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
                message = f"You have been warned from `` {ctx.guild.name} ``  by `` {ctx.message.author} `` for `` {reason} ``"
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="WARNED",
                                value=f'You have been warned from `` {ctx.guild.name} ``  by `` {ctx.message.author} `` for `` {reason} ``',
                                inline=False)
                await member.send(embed=embed)
                embed = discord.Embed(title="User was warned for {}".format(reason),
                                      description="**{}** has been warned!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=embed)
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


@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send("you must enter a reason to ban.")
    else:
        try:
            if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.ban_members:
                message = f"You have been warned from {ctx.guild.name} by {ctx.message.author} for {reason}"
                embed = discord.Embed(
                    colour=discord.Color.red()
                )
                embed.add_field(name="BANNED",
                                value=f'You have been banned from `` {ctx.guild.name} `` by `` {ctx.message.author} `` for `` {reason} ``',
                                inline=False)
                await member.send(embed=embed)
                await ctx.guild.ban(member)
                embed = discord.Embed(title="User banned was banned for {}".format(reason),
                                      description="**{}** has been banned!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=embed)
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
                await ctx.guild.kick(member)
                embed = discord.Embed(title="User kicked was kicked for {}".format(reason),
                                      description="**{}** has been kicked!".format(member),
                                      color=discord.Color.green())
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=embed)
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
@client.command()
async def meow(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='meow :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    meow = nekos.img("meow")

    embed.set_image(url=meow)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !meow result: {meow}   time:{round(client.latency * 1000)}ms")


###########################################################
@client.command()
async def tickle(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} tickled {member.name} because {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    tickle = nekos.img("tickle")

    embed.set_image(url=tickle)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !tickle result: {tickle}   time:{round(client.latency * 1000)}ms")


###########################################################

@client.command()
async def lewd(ctx):
    if not ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        embed = discord.Embed(
            title='lewd doe :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    lewd = nekos.img("lewd")

    embed.set_image(url=lewd)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !lewd result: {lewd}   time:{round(client.latency * 1000)}ms")


###################################################################
@client.command()
async def feed(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} fed {member.name} because {reason}",
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
async def gecg(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='gecg :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    gecg = nekos.img("gecg")

    embed.set_image(url=gecg)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !gecg result: {gecg}   time:{round(client.latency * 1000)}ms")


##############################################################
@client.command()
async def eroyuri(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='eroyuri :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    eroyuri = nekos.img("eroyuri")

    embed.set_image(url=eroyuri)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !eroyuri result: {eroyuri}   time:{round(client.latency * 1000)}ms")


###############################################################
@client.command()
async def eron(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='eron :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    eron = nekos.img("eron")

    embed.set_image(url=eron)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !eron result: {eron}   time:{round(client.latency * 1000)}ms")


############################################################
@client.command()
async def bj(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title='bj :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    bj = nekos.img("bj")

    embed.set_image(url=bj)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !bj result: {bj}   time:{round(client.latency * 1000)}ms")


@client.command()
async def nsfw_neko_gif(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    nsfw_neko_gif = nekos.img("nsfw_neko_gif")

    embed.set_image(url=nsfw_neko_gif)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !nsfw_neko_gif result: {nsfw_neko_gif}   time:{round(client.latency * 1000)}ms")


###########################################################################
@client.command()
async def solo(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    solo = nekos.img("solo")

    embed.set_image(url=solo)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !solo result: {solo}   time:{round(client.latency * 1000)}ms")


############################################################################
@client.command()
async def kemonomimi(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    kemonomimi = nekos.img("kemonomimi")

    embed.set_image(url=kemonomimi)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !kemonomimi result: {kemonomimi}   time:{round(client.latency * 1000)}ms")


###################################################################

@client.command()
async def gasm(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} is in awe with {member.name} because {reason}",
        description='',
        colour=discord.Colour.from_rgb(r, g ,b)
    )
    gasm = nekos.img("gasm")

    embed.set_image(url=gasm)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !gasm result: {gasm}   time:{round(client.latency * 1000)}ms")


####################################################################
@client.command()
async def nsfw_avatar(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    nsfw_avatar = nekos.img("nsfw_avatar")

    embed.set_image(url=nsfw_avatar)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !nsfw_avatar result: {nsfw_avatar}   time:{round(client.latency * 1000)}ms")


#######################################################################
@client.command()
async def poke(ctx, member: discord.Member, *, reason=None):
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
async def anal(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g ,b)
        )
    anal = nekos.img("anal")

    embed.set_image(url=anal)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !anal result: {anal}   time:{round(client.latency * 1000)}ms")


####################################################################################################################################
@client.command()
async def slap(ctx, member: discord.Member, *, reason=None):
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


######################################################################################################################################
@client.command()
async def hentai(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    hentai = nekos.img("hentai")

    embed.set_image(url=hentai)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hentai result: {hentai}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def avatar(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    avatar = nekos.img("avatar")

    embed.set_image(url=avatar)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !hentai result: {avatar}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def erofeet(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    erofeet = nekos.img("erofeet")

    embed.set_image(url=erofeet)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !erofeet result: {erofeet}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def pussy(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    pussy = nekos.img("pussy")

    embed.set_image(url=pussy)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !pussy result: {pussy}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def tits(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    tits = nekos.img("tits")

    embed.set_image(url=tits)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !tits result: {tits}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def waifu(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    waifu = nekos.img("waifu")

    embed.set_image(url=waifu)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !waifu result: {waifu}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def boobs(ctx):
    if not ctx.channel.is_nsfw():
        author = ctx.message.author
        await ctx.author.send("```not an nsfw channel```")
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    boobs = nekos.img("boobs")

    embed.set_image(url=boobs)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !boobs result: {boobs}   time:{round(client.latency * 1000)}ms")


######################################################################################################################################
@client.command()
async def smallboobs(ctx):
    embed = discord.Embed(
        title=' :flushed:',
        description='',
        colour=discord.Colour.blurple()
    )
    smallboobs = nekos.img("smallboobs")

    embed.set_image(url=smallboobs)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !smallboobs result: {smallboobs}   time:{round(client.latency * 1000)}ms")


#######################################################################################################################################
@client.command()
async def pat(ctx, member: discord.Member, *, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=f"{ctx.message.author} petted {member.name}",
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
async def kiss(ctx, member: discord.Member, *, reason=None):
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
async def spank(ctx, member: discord.Member, *, reason=None):
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
async def cuddle(ctx, member: discord.Member, *, reason=None):
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
async def hug(ctx, member: discord.Member, *, reason=None):
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
        description='contribution to the project is always welcome, feel free to contribute, edit, ,clean up, document, and improve the source code at: https://github.com/Eddy-Arch/NSFW_Discordb_bot',
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
    world = "-=worldwide=- cases:" , r.json()['worldStats']['cases'] , " cases today: " , r.json()['worldStats']['todayCases'] , " deaths: " , r.json()['worldStats']['deaths'] , " died today" , r.json()['worldStats']['todayDeaths'] , " recovered: " , r.json()['worldStats']['recovered'] , " critical: " , r.json()['worldStats']['critical'] , " cases per one million: " , r.json()['worldStats']['casesPerOneMillion']
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
async def cat(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='cute kitties :)',
        description='',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    neko = nekos.cat()
    embed.set_image(url=neko)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !neko result: {neko}   time:{round(client.latency * 1000)}ms")


# dummy token in here, well its a dummy now. appearantly discord has a web crawler that found my bots token in here. pretty damn cool.
client.run("demo token")

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

