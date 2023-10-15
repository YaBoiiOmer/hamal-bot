import requests
from bs4 import BeautifulSoup

class HamalAPI():
  BASE_URL = 'https://hamal.co.il'

  def __init__(self) -> None:
    self.__build_id = self.__get_build_id()
    self.__last_message_id_sent = None

  def has_news(self):
    return self.__last_message_id_sent != self.get_last_item()['_id']

  def set_last_message_id_sent(self, last_message_id):
    self.__last_message_id_sent = last_message_id

  def get_last_item(self):
      return max(self.get_main_items(), key=lambda item: item['publishedAt'], default=None)

  def get_main_items(self):
    url = f"https://hamal.co.il/_next/data/{self.__build_id}/he/main.json?hashtag=main"
    response = requests.get(url).json()
    items = response['pageProps']['items']
    return items
  
  @staticmethod
  def get_element_by_type(item, type):
    # title / text / picture
    for element in item['body']:
      if element['type'] == type:
        return element['value']

  def __get_build_id(self):
      response = requests.get(self.BASE_URL)

      soup = BeautifulSoup(response.text, 'html.parser')
      scripts = soup.find_all('script')

      for script in scripts:
        if not script.has_attr('src'): continue
        if not "/_next/static" in script['src']: continue
        
        build_id = script['src'].split("/")[3]
        if build_id in ["chunks"]: continue

        return build_id


if __name__ == '__main__':
  hamal = HamalAPI()
  print(hamal.get_last_item())