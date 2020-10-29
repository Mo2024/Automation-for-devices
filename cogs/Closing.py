import discord
from discord.ext import commands 
import os

class Closing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Clsoing apps commands are working')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def cdiscord(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\cdiscord.bat', 'open')
        await ctx.send("Clsoing Discord")

    @commands.has_role('Idiots')
    @commands.command()
    async def cspotify(self, ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\cspotify.bat', 'open')   
        await ctx.send('Closing Spotify')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def closeall(self,ctx):
        os.startfile(r'C:\Users\Mohamed Osama\Documents\Discord-bot-controller\executables\closeall.bat', 'open')
        await ctx.send('Closing all apps')

def setup(client):
    client.add_cog(Closing(client))