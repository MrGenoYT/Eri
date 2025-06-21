import discord
from discord.ext import commands
from ai.gemini_ai import ai_client
from db import mongo

class Dashboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dashboard(self, ctx):
        embed = discord.Embed(title="Eri's Dashboard")
        view = discord.ui.View()
        
        view.add_item(discord.ui.Select(placeholder="Select Option", options=[
            discord.SelectOption(label="Persona"),
            discord.SelectOption(label="Exclusive Features"),
            discord.SelectOption(label="Reset")
        ]))
        
        await ctx.send(embed=embed, view=view)
