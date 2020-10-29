import discord
from discord.ext import commands 
import os
import pyautogui as pg

class Open(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Opening apps commands are working')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def discord(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\discord.bat', 'open') 
        await ctx.send('Opening Discord')   

    @commands.has_role('Idiots')
    @commands.command()
    async def spotify(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\spotify.bat', 'open')
        await ctx.send('Opening Spotify') 

    @commands.has_role('Idiots')
    @commands.command()
    async def chrome(self, ctx):
        os.system("start chrome")
        await ctx.send('Opening Chrome')
    
    @commands.command()
    @commands.has_role('Idiots')
    async def web(self, ctx):
            await pg.typewrite('WhatsApp Desktop\n')
    
    @commands.command()
    @commands.has_role('Idiots')
    async def cmd(self, ctx):
            await os.system("start cmd")
        
def setup(client):
    client.add_cog(Open(client))