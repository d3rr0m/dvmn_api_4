from telegram import Bot
from os import environ
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    bot = Bot(environ['TELEGRAM_BOT_TOKEN'])
    chat_id = '@d3rr0m'
    bot.send_message(chat_id=chat_id, text='Hi there!')
