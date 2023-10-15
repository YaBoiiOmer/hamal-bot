import os, json, atexit
from dotenv import load_dotenv

load_dotenv()

class HamalBotConfig():
  CHANNELS_PATH = os.getenv("CHANNELS_PATH")
  TOKEN = os.getenv('DISCORD_TOKEN')

  def __init__(self):
    atexit.register(self.__save_channels)
    self.__load_channels()

  def register_channel(self, guild_id: int, channel_id: int):
    self.__text_channels[guild_id] = channel_id
    print(f"{guild_id} - {channel_id} was registered.")

  def get_channels(self):
    """
    Returns:
        int: Registered channel ids
    """
    return self.__text_channels.values()

  def __load_channels(self):
    if not os.path.exists(HamalBotConfig.CHANNELS_PATH): 
      self.__text_channels = {}
      return
    with open(HamalBotConfig.CHANNELS_PATH) as channels_file:
      self.__text_channels = json.load(channels_file)

  def __save_channels(self):
    if not self.__text_channels: return

    parent_folder = os.path.dirname(HamalBotConfig.CHANNELS_PATH)
    if not os.path.exists(parent_folder):
      os.makedirs(parent_folder)

    with open(HamalBotConfig.CHANNELS_PATH, "w") as channels_file:
      json.dump(self.__text_channels, channels_file)