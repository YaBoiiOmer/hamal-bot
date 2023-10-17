from bot.bot import HamalBot
import discord
from discord.ext import tasks, commands

class CheckForUpdatesTask(commands.Cog):

  def __init__(self, bot: HamalBot):
    self.bot = bot
    self.check_for_updates.start()

  @tasks.loop(seconds=5)
  async def check_for_updates(self):
    hamal = self.bot.get_hamal_api()
    if not hamal.has_news(): return
    print("Spreading the news!")
    for channel_id in self.bot.get_config().get_channels():
      channel = self.bot.get_channel(channel_id)
      if not channel: continue

      await self.__send_news_message(channel, hamal)
      
  async def cog_unload(self):
    self.check_for_updates.cancel()

  async def __send_news_message(self, channel, hamal):
    async with channel.typing():
      last_item = hamal.get_last_item()

      embed = discord.Embed(
                          title=hamal.get_element_by_type(last_item, "title"), 
                          url=f"https://hamal.co.il/main/{last_item['metaData']['slug']}",
                          description=hamal.get_element_by_type(last_item, "text"),
                          color=0xFF0000)
      
      video = hamal.get_element_by_type(last_item, "video")
      
      if video:
        preview_url = video['previewUrl']
        if preview_url: 
          embed.set_image(url=preview_url)

      await channel.send(embed=embed)
      hamal.set_last_message_id_sent(last_item['_id'])

async def setup(bot):
  await bot.add_cog(CheckForUpdatesTask(bot))
