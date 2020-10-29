import discord
from discord.ext import commands 
import os
import sys
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
a = "a"
class Power(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Power commands are working')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def login(self, ctx):      
        await keyboard.press('a')
        #await os.system("login.vbs")

    @commands.has_role('Idiots')
    @commands.command()
    async def shutdown(self, ctx):
        os.system("shutdown /s /t 10")
        await ctx.send('Shutting down in 10 seconds')

    @commands.has_role('Idiots')
    @commands.command()
    async def a(self, ctx):
        os.system("shutdown /a")
        await ctx.send('Aborting shutdown')

    @commands.has_role('Idiots')
    @commands.command()
    async def reboot(self, ctx):
        os.system("shutdown /r /t 10") 
        await ctx.send('Rebooting in 10 seconds')

    @commands.has_role('Idiots')
    @commands.command()
    async def lock(self, ctx):
        os.system("Rundll32.exe User32.dll,LockWorkStation")
        await ctx.send('Computer is locked')

    counter = 0

    @commands.has_role('Idiots')
    @commands.command()
    async def sleep(self, ctx):
        '''while counter != 10:
            counter += 1
            if int(counter) == 10:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
                await ctx.send('Computer is asleep')'''
        

    @commands.has_role('Idiots')
    @commands.command()
    async def hibernate(self, ctx):
        os.system("rundll32.exe PowrProf.dll,SetSuspendState") 
        await ctx.send('Computer has been hibernated')
    
    @commands.has_role('Idiots')
    @commands.command()
    async def rebootbot(self, ctx):
        os.execv(sys.executable, ['python'] + sys.argv)

def setup(client):
    client.add_cog(Power(client))