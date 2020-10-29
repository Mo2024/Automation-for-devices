import discord
from discord.ext import commands 
import os
import subprocess

class Volume(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Volume commands are working')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def mute(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\mute.bat', 'open')
        await ctx.send('Computer muted')

    @commands.has_role('Idiots')
    @commands.command()
    async def unmute(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\unmute.bat', 'open')
        await ctx.send('Computer unmuted') 
   
    @commands.has_role('Idiots')
    @commands.command()
    async def volup(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\volup.bat', 'open') 
        await ctx.send('Volume increased by 10')

    @commands.has_role('Idiots')
    @commands.command()
    async def voldown(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\voldown.bat', 'open')
        await ctx.send('Volume decreased by 10')

    @commands.has_role('Idiots')
    @commands.command()
    async def speakers(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\speakers.bat', 'open')
        await ctx.send('Output speakers')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def headphones(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\headphones.bat', 'open') 
        await ctx.send('Output headphones')

def setup(client):
    client.add_cog(Volume(client))