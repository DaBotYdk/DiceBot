import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os

Client = discord.Client()

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    dcrl = message.content()
    if dcrl[0, 6] == "DiceBot":
        if isinstance(dcrl[8, len(dcrl)-1], int):
            maxnum = dcrl[8, len(dcrl)-1]
            await client.send_message(message.channel, random.randint(1, maxnum))

client.run("TOKEN")
