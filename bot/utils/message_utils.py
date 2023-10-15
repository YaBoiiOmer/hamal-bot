import datetime

def timestamp():
  return datetime.datetime.strftime(datetime.datetime.now(), "%I:%M:%S %p")

if __name__ == '__main__':
  print(timestamp())