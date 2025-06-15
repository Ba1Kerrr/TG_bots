import telebot
from telebot import types
bot = telebot.TeleBot('YOUR_BOT_TOKEN')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я SocialSphere. Я помогу вам управлять социальными сетями.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Опубликовать пост':
        bot.send_message(message.chat.id, 'Пожалуйста, введите текст поста.')
        bot.register_next_step_handler(message, publish_post)
def publish_post(message):
    post_text = message.text
    # Обработка публикации поста
    bot.send_message(message.chat.id, 'Пост опубликован!')
bot.polling()