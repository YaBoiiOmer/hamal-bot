from bot.config.config import HamalBotConfig
from bot.hamal_api import HamalAPI

import discord
from discord.ext import commands

class HamalBot(commands.Bot):

  def __init__(self) -> None:
    super().__init__(command_prefix='', intents=discord.Intents().default())
    self.__hamal_api = HamalAPI()
    self.__config = HamalBotConfig()
  
  def run(self):
    super().run(self.__config.TOKEN)

  async def on_ready(self):
    await self.__load_extensions()
    await self.tree.sync()
    print(f"Bot is now running!")

  def get_config(self):
    return self.__config
  
  def get_hamal_api(self):
    return self.__hamal_api

  async def __load_extensions(self):
    await self.load_extension("bot.commands.set_news_channel_command")
    await self.load_extension("bot.tasks.check_for_updates")