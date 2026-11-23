import telebot
from telebot import types
import time
import threading
from flask import Flask

TOKEN = "8830467337:AAFLegVrjduz937H3knGFK2JhEla9F6GRkQ"
bot = telebot.TeleBot(TOKEN)

# --- Баланс ---
balance = {}

# --- Flask чтобы Render не спал ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# --- Клавиатура ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📚 Курсы", "📅 Расписание")
    markup.add("👩‍🏫 Преподаватели", "📍 Контакты")
    markup.add("🎬 Смотреть рекламу +0.25", "💰 Мой баланс")
    markup.add("📝 Записаться")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        "🇨🇳 Привет! Это Chinese Academy!\n\nИзучай китайский с нами!\n\n🎬 Смотри рекламу и копи баллы!\n100 баллов = скидка на курс!",
        reply_markup=main_menu())

@bot.message_handler(commands=['balance'])
def show_balance_cmd(message):
    b = balance.get(message.chat.id, 0)
    bot.send_message(message.chat.id, f"💰 Твой баланс: {b} баллов\n\n100 баллов = скидка на курс!")

@bot.message_handler(func=lambda m: m.text == "💰 Мой баланс")
def show_balance_btn(message):
    b = balance.get(message.chat.id, 0)
    bot.send_message(message.chat.id, f"💰 Твой баланс: {b} баллов\n\nСмотри рекламу и копи еще!")

@bot.message_handler(func=lambda m: m.text == "📚 Курсы")
def courses(message):
    bot.send_message(message.chat.id,
        "📚 Наши курсы:\n\n1. HSK 1 - для начинающих - 300 сомони/мес\n2. HSK 2 - 350 сомони/мес\n3. Разговорный - 400 сомони/мес\n4. Для детей - 250 сомони/мес")

@bot.message_handler(func=lambda m: m.text == "📅 Расписание")
def schedule(message):
    bot.send_message(message.chat.id, "📅 Расписание:\n\nПн-Ср-Пт: 16:00 и 18:00\nВт-Чт-Сб: 15:00 и 17:00")

@bot.message_handler(func=lambda m: m.text == "👩‍🏫 Преподаватели")
def teachers(message):
    bot.send_message(message.chat.id, "👩‍🏫 Наши преподаватели - носители и опытные учителя с HSK 5-6!")

@bot.message_handler(func=lambda m: m.text == "📍 Контакты")
def contacts(message):
    bot.send_message(message.chat.id, "📍 Душанбе, ул. Р
