import telebot
from telebot import types
bot = telebot.TeleBot('YOUR_BOT_TOKEN')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я LeadGenie. Я помогу вам генерировать лиды.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Генерировать лиды':
        bot.send_message(message.chat.id, 'Пожалуйста, введите информацию о вашем продукте или услуге.')
        bot.register_next_step_handler(message, generate_lead)
def generate_lead(message):
    lead_info = message.text
    # Обработка информации о лиде
    bot.send_message(message.chat.id, 'Лид сгенерирован!')
bot.polling()