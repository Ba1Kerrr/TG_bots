import telebot
from telebot import types
bot = telebot.TeleBot('YOUR_BOT_TOKEN')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я ContentCraft. Я помогу вам создавать контент.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Создать контент':
        bot.send_message(message.chat.id, 'Пожалуйста, введите тему контента.')
        bot.register_next_step_handler(message, create_content)
def create_content(message):
    content_topic = message.text
    # Обработка создания контента
    bot.send_message(message.chat.id, 'Контент создан!')
bot.polling()