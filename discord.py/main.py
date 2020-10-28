# imports
# packages needed for repl.it is only discord.py and flask
# asyncio installation breaks bot
import aiohttp
import random
import json
import discord
from discord.ext import commands
from discord.utils import get,find
from discord.ext.commands import has_permissions
from keep_alive import keep_alive

#prefix list

prefixes = [">"]

# Insert token here
TOKEN=""
client=commands.Bot(command_prefix=prefixes)

# for cmd running
@client.event
async def on_ready():
      print("Online")

# for listening to

@client.event
async def on_ready():
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=">help"))

# Saying hello aka test

@client.command()
async def hello(ctx):
      await ctx.send("Hi")

# credits

@client.command()
async def credits(ctx):
      await ctx.send("Made using discord.py, repl.it, uptime robot and flask")

# Must include this to proceed...

@client.command()
async def madeby(ctx):
      await ctx.send("Copyright made by sn0wstar#2485 aka L4xus")
# clear msgs

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=100):
      await ctx.channel.purge(limit = amount)
      await ctx.send("Cleared messages")

@client.command(aliases=['k']) 
@commands.has_permissions(kick_members = True) 
async def kick(ctx,member : discord.Member,*,reason =  "No reason provided"): 
      await ctx.send("kicked "+member )
      await member.send("You have been kicked because "+reason) 
      await member.kick(reason=reason)

@client.command(aliases=['b']) 
@commands.has_permissions(ban_members = True) 
async def ban(ctx,member : discord.Member,*,reason =  "No reason provided"): 
      await ctx.send("banned "+member )
      await member.send("You have been banned because "+reason) 
      await member.ban(reason=reason)


anc = ["16/2020 Today announcements have been made"]

@client.command()
async def announce(ctx):
      await ctx.send(anc[0])
  
#@client.command()
#async def say(ctx,announcement):
#      await ctx.send(announcement)

@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.send(mesg)

@client.command(aliases=['git'])
async def github(ctx):
  await ctx.send("https://github.com/l4xus")

@client.command()
async def source(ctx):
  await ctx.send("https://github.com/L4xus/Dank-Arena-Bot")

@client.command()
async def prefix(ctx,new):
  prefixes.append(new)
  await ctx.send("prefix is now "+new)

@client.command()
async def delprefix(ctx,oofx):
  prefixes.remove(oofx)
  await ctx.send("prefix is removed "+oofx)

@client.command()
async def pxs(ctx):
  await ctx.send(prefixes)

# EZ meme system developed by sn0wstar aka L4xus

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="meme", description="Dank arena memer")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


# flask ping for uptimerobot.com
keep_alive()

client.run(TOKEN)
