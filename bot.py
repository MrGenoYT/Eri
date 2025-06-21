import discord
from discord.ext import commands
from config import TOKEN
from handler import message_handler, edit_handler
from commands import dashboard, settings
from misc import role_manager

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"Eri is online as {bot.user}")

@bot.event
async def on_message(message):
    await message_handler.handle_message(bot, message)

@bot.event
async def on_message_edit(before, after):
    await edit_handler.handle_edit(before, after)

@bot.event
async def on_guild_join(guild):
    await role_manager.ensure_role(bot, guild)

bot.add_cog(dashboard.Dashboard(bot))
bot.add_cog(settings.Settings(bot))

bot.run(TOKEN)
