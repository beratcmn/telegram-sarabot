import os
from dotenv import load_dotenv
import telebot
from request_handler import RequestHandler
from classes.news import News, Article

load_dotenv()

API_KEY = os.getenv("TELEGRAM_SARABOT_API_KEY")
VALID_PIN = os.getenv("PIN")
logged_in = False

bot = telebot.TeleBot(API_KEY)


def check_login(message):
    if logged_in == False:
        bot.send_message(
            message.chat.id,
            "You are not logged in. Please use /login to login.",
        )
        return False
    else:
        return True

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hello, this is SARA. I am a bot that can help you with your daily tasks. Before we start I need authorization. Use /login to login.",
    )



@bot.message_handler(commands=["login"])
def login(message):
    global logged_in
    bot.send_message(
        message.chat.id,
        "Checking your credentials...",
    )

    input_pin = message.text[len(message.text) - len(VALID_PIN) :].strip()

    if input_pin == VALID_PIN:
        logged_in = True
        bot.send_message(
            message.chat.id,
            "You are now logged in. Welcome back sir!",
        )
        bot.send_message(
            message.chat.id,
            "Check /list to see what I can do for you.",
        )
    else:
        bot.send_message(
            message.chat.id,
            "Invalid credentials. Please try again.",
        )


@bot.message_handler(commands=["list"])
def list_actions(message):
    if check_login(message) == False:
        return

    bot.send_message(
        message.chat.id,
        "Here is a list of things I can do for you:",
    )
    bot.send_message(
        message.chat.id,
        "/list - List all available actions"+
        "\n"+
        "/login - Login to SARA"+
        "\n"+
        "/news - Show todays headlines"
    )


@bot.message_handler(commands=["news"])
def show_news(message):
    if check_login(message) == False:
        return

    bot.send_message(
        message.chat.id,
        "Here are todays headlines:",
    )   

    request_handler = RequestHandler(NEWS_API=os.getenv("NEWS_API_KEY"))
    news = request_handler.getNews()

    for article in news.articles:
        bot.send_message(
            message.chat.id,
            article.title,
        )




# ? Normal message handler
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if check_login(message) == False:
        return

    bot.send_message(
        message.chat.id,
        message.text,
    )
    

if __name__ == "__main__":
    print("SARA is running...")
    bot.polling()