import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import asyncio
import schedule
import time
import os
import sys
####################################################################################
TOKEN = 'NICE TRY'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
URL = "https://www.google.com/search?q=weather+keesler+afb&rlz=1C1UEAD_enUS1019US1019&sxsrf=ALiCzsZ-VuiPENm2nF2K_vQPDoiv_yYegg%3A1661528204606&ei=jOgIY7zKJISlqtsP6-Kt2AY&ved=0ahUKEwi8wK3z6uT5AhWEkmoFHWtxC2sQ4dUDCA4&uact=5&oq=weather+keesler+afb&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQgAIyBggAEB4QFjIGCAAQHhAWMgkIABAeEMkDEBYyBQgAEIYDOgoIABBHELADEMkDOggIABCSAxCwAzoHCAAQRxCwAzoOCAAQsQMQgwEQyQMQkQI6BQgAEJIDOhkILhCABBCHAhCxAxCDARDHARDRAxDUAhAUOhEILhCxAxCDARDHARDRAxCRAjoFCAAQkQI6CwgAEIAEELEDEIMBOgsIABCxAxCDARCRAjoICAAQsQMQgwE6BQgAEIAEOggIABCABBCxAzoQCAAQgAQQhwIQsQMQgwEQFDoPCAAQgAQQhwIQFBBGEIACOgoIABCABBCHAhAUOggIABAeEA8QFkoECEEYAEoECEYYAFDyBFiaHGCRHmgCcAB4AIABwQGIAe4MkgEEMS4xMpgBAKABAcgBCsABAQ&sclient=gws-wiz"
html = requests.get(URL).content
soup = BeautifulSoup(html, "html.parser")
####################################################################################
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(name="the SEC+ courses", type=5))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(name="for !help", type=3))
        await asyncio.sleep(10)
        
async def restart_task():
    while True:
        await asyncio.sleep(300)
        await os.execl(sys.executable, sys.executable, *sys.argv)
#####################################################################################

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    bot.loop.create_task(restart_task())

bot.remove_command('help')
#######################################################################################
@bot.command(name='help', help='This command.')
async def help(ctx):
    embed=discord.Embed(title="COMMANDS",color=0x0c5fe4)
    embed.add_field(name="!temp", value="Returns current temperature", inline=True)
    embed.add_field(name="!sky", value="Returns current sky conditions", inline=True)
    embed.add_field(name="!time", value="Returns latest time update ", inline=True)
    await ctx.send(embed=embed)

    
@bot.command(name='time', help='time')
async def time(ctx):
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    currenttime = data[0]
    sky = data[1]
    await ctx.send(currenttime)
    
@bot.command(name='temp', help='Gives local temp.')
async def temp(ctx):
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    await ctx.send(temp)

@bot.command(name='sky', help = 'Sky conditions.')
async def sky(ctx):
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    currenttime = data[0]
    sky = data[1]
    await ctx.send(sky)

bot.run(TOKEN)

