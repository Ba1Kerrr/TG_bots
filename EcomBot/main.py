import telebot
from telebot import types
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_API_key'))
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я EcomBot. Я помогу вам интегрировать с электронной коммерцией.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Интегрировать с электронной коммерцией':
        bot.send_message(message.chat.id, 'Пожалуйста, введите информацию о вашем магазине.')
        bot.register_next_step_handler(message, integrate_ecommerce)
def integrate_ecommerce(message):
    ecommerce_info = message.text
    # Обработка интеграции с электронной коммерцией
    bot.send_message(message.chat.id, 'Интеграция с электронной коммерцией завершена!')
bot.polling(none_stop=True)