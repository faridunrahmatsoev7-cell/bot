import telebot
import time
TOKEN = "8830467337:AAEu-BLJ1qovTLYoVtP9ezmVwhB2F6g6N58"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Привет! Я бот Chinese Academy TJ. Напиши /help")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, "Получил: " + m.text)

while True:
    try:
        bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(e)
        time.sleep(5)
