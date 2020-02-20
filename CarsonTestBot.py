import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.event
async def on_member_join(member, server):
    print(f"(member) has joined (server).")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Yep, still alive with {round(bot.latency*1000)}ms ping.")
    


bot.run("Njc5OTMzMTU4NzQ1MDQ3MDQx.Xk74Cg.B0YizMQDWQYH9IFFrdd51IghLA0")

