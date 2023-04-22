import os
from dotenv import load_dotenv
import telebot

load_dotenv()

print(os.getenv("TELEGRAM_SARABOT_API_KEY"))