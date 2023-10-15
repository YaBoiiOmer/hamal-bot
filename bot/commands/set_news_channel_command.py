import discord
from discord.ext import commands
from discord import app_commands
from bot.bot import HamalBot

class SetNewsChannelCommand(commands.Cog):
  def __init__(self, bot: HamalBot):
    self.bot = bot

  @app_commands.command(name="setnewschannel", description="Sets the hamal news channel to the current channel.")
  async def set_news_channel(self, interaction: discord.Interaction):
    self.bot.get_config().register_channel(interaction.guild_id, interaction.channel_id)
    await interaction.response.send_message(f"Succesfully set the hamal news to text channel **#{interaction.channel.name}**")

async def setup(bot):
  await bot.add_cog(SetNewsChannelCommand(bot))