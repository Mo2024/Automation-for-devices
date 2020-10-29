import os
import discord
from discord.ext import commands 
import pyautogui as pg

client = commands.Bot(command_prefix = '?') #sets prefix 

f = 19

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb)

@commands.has_role('Idiots')
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1) 
    if f == 19: 
        await ctx.send( str(amount) + ' messages has been cleared')

@commands.has_role('Idiots')
@client.command()
async def winleft(ctx):
    await pg.hotkey('winleft') 

@commands.has_role('Idiots')
@client.command()
async def enter(ctx):
    await pg.hotkey('enter') 

@commands.has_role('Idiots')
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@commands.has_role('Idiots')
@client.command()
async def unload (ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run('NzQ1NjMzNTIxODc1NDE5MTY4.Xz0nVA.7oI4LSWV5ZKdSS66EJpHafjwkKg') #You know what this is fuck off