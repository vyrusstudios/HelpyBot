import discord
from discord.ext import commands
import asyncio
import sqlite3
import datetime
import sys
import os
import random


client = commands.Bot(command_prefix='h-', case_insenstive=True)

@client.event
async def on_ready():
    db = sqlite3.connect('HelpyBot.db')
    cursor = db.cursor()
    print('Helpy Online!')
    return await client.change_presence(activity=discord.Activity(type=1, name='Help Wanted Custom Night', url='https://twitch.tv/VyTV'))

client.remove_command('help')

initial_extensions = ['cogs.commands']

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f'Helpy is studying {extension}', file=sys.stderr)

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

@client.command()
async def hi(ctx):
	ping = client.latency
	embed=discord.Embed(title='Henlo!', colour=discord.Colour(0xf296ff), description=f'My name is Helpy! I am developed by Vy#2021!')
	embed.add_field(name=' Latency::ping_pong:', value=f'{ping}')
	await ctx.message.channel.send(embed=embed)

	
@client.command()
async def henlo(ctx):
	ping = client.latency
	embed=discord.Embed(title='Henlo!', colour=discord.Colour(0xf296ff), description=f'My name is Helpy! I am developed by Vy#2021!')
	embed.add_field(name=' Latency::ping_pong:', value=f'{ping}')
	await ctx.message.channel.send(embed=embed)

@client.command()
async def hello(ctx):
	ping = client.latency
	embed=discord.Embed(title='Henlo!', colour=discord.Colour(0xf296ff), description=f'My name is Helpy! I am developed by Vy#2021!')
	embed.add_field(name=' Latency :ping_pong:', value=f'{ping}')
	await ctx.message.channel.send(embed=embed)

@client.command()
async def hewwo(ctx):
	ping = client.latency
	embed=discord.Embed(title='Hewwo! uwu', colour=discord.Colour(0xf296ff), description=f'My nameu is Hewpy uwu! I am devewoped by Vy#2021! owo')
	embed.add_field(name=' Latency::ping_pong:', value=f'{ping}')
	await ctx.message.channel.send(embed=embed)

client.run("")
