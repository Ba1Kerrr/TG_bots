import telebot
from telebot import types
import googletrans
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_API_key'))
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я LinguaBot. Я помогу вам перевести текст.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Перевести текст':
        bot.send_message(message.chat.id, 'Пожалуйста, введите текст для перевода.')
        bot.register_next_step_handler(message, translate_text)
def translate_text(message):
    text_to_translate = message.text
    # Обработка перевода текста
    bot.send_message(message.chat.id, 'Текст переведен!')
bot.polling(none_stop=True)