import discord
from discord.ext import commands
from discord import app_commands

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="test")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("testing complete")

async def setup(bot):
    await bot.add_cog(MainCog(bot), guilds=[discord.Object(id=861358799570468876), discord.Object(id=646183824815947806)])