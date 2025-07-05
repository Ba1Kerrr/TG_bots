import telebot
from telebot import types
import datetime
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

bot = telebot.TeleBot(os.getenvt('TG_API_key'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я SchedulePro. Я помогу вам бронировать встречи и планировать собрания.')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Бронировать встречу':
        bot.send_message(message.chat.id, 'Пожалуйста, введите дату и время встречи.')
        bot.register_next_step_handler(message, book_meeting)

def book_meeting(message):
    meeting_date = message.text
    # Обработка бронирования встречи
    bot.send_message(message.chat.id, 'Встреча забронирована!')

bot.polling(none_stop=True)