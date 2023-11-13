import os, json, atexit
from dotenv import load_dotenv

load_dotenv()

def check_for_environment_vars(variables: list):
  for variable in variables:
    if not os.environ.get(variable):
      raise EnvironmentError(f"Environment variable {variable} was not set!")

class HamalBotConfig():
  TOKEN = os.getenv('DISCORD_TOKEN')
  CHANNELS_PATH = os.path.join("data", "channels.json")

  check_for_environment_vars(["DISCORD_TOKEN"])

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
    print("Saving text channels...")
    if not self.__text_channels: 
      print("No text channels found returning...")
      return

    parent_folder = os.path.dirname(HamalBotConfig.CHANNELS_PATH)
    if not os.path.exists(parent_folder):
      os.makedirs(parent_folder)

    with open(HamalBotConfig.CHANNELS_PATH, "w") as channels_file:
      json.dump(self.__text_channels, channels_file)

    print("Saved text channels to config successfully!")
