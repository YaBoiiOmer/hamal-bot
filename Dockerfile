FROM python:3.11.4-alpine
RUN pip install bs4 requests discord.py python-dotenv
COPY . /home/hamalbot
CMD ["python", "/home/hamalbot/main.py"]