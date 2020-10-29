import discord
from discord.ext import commands 
import os
import sys
import time
from pynput.keyboard import Key, Controller
import pyautogui as pg 
from discord.utils import get 
from discord.ext import commands, tasks
import asyncio

keyboard = Controller()
a = "a"
class TypeKeyboard(commands.Cog):
    def __init__(self, client):
        self.client = client


    '''@commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        msg_dump_channel = 760182149839716423
        channel = self.bot.get_channel(msg_dump_channel)
        if message.guild is None and not message.author.bot:
            if (len(message.attachments)>0):
                await channel.send(f"Author: {message.author}\nAuthor ID: {message.author.id}\nAttachment: {message.attachments[0].url} \nContent: {message.content}")
            else:
                if message.guild is None and not message.author.bot:
                    await channel.send(f"Author: {message.author}\nAuthor ID: {message.author.id}\nContent: {message.content}")'''
    @commands.command()
    @commands.has_role('Idiots')
    async def dm(self, ctx, *, content):
        user = self.client.get_user(229948716868567040)
        await user.send(content)


    @commands.command()
    @commands.has_role('Idiots')
    async def send(self, ctx, channel: discord.TextChannel, *, content):
            await channel.send(content)

    @commands.command()
    @commands.has_role('Idiots')
    async def typethis(self, ctx, *, content):
        await pg.typewrite(content)


def setup(client):
    client.add_cog(TypeKeyboard(client))