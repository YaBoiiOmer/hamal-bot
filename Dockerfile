FROM python:3.11.4
RUN pip install bs4 requests discord.py python-dotenv
ADD . /home/hamalbot
CMD ["python", "/home/hamalbot/main.py"]