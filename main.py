import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.message_content = True
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents, application_id='1118428787323965513')
load_dotenv()
token = os.environ['TOKEN']

@bot.command(name="sync")
async def sync(ctx) -> None:
    fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    await ctx.send(f'Synced {len(fmt)} commands.')

@bot.event
async def setup_hook():
    await bot.load_extension('cogs.maincog')
    await bot.load_extension('cogs.musiccog')
    print('Cogs loaded!')

bot.run(token)