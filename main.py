import logging
import os

from transliterate import translit
import telebot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Dobryj vecher!')


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, '''
Ya
SVS
Dr.Sergey V.Smirnov
Associate professor
Department of Higher Geometry and Topology
Faculty of Mechanics and Mathematics
Moscow State University
Vorob'evy Gory, 1
Moscow, 119991, Russia
''')


message_history = {}
sent_message_history = {}


@bot.message_handler(content_types=['text'])
def message_handler(message):
    chat_id = message.chat.id
    message_text = message.text
    prev_message = message_history.get(chat_id, None)
    prev_sent_message = sent_message_history.get(chat_id, None)
    print(chat_id, message_text)

    if prev_message == message_text and prev_sent_message != message_text:
        bot.send_message(chat_id, translit(message_text, 'ru', reversed=True))
        sent_message_history[chat_id] = message_text

    message_history[chat_id] = message_text


@bot.message_handler(content_types=['sticker'])
def message_handler(message):
    chat_id = message.chat.id
    message_sticker = message.sticker
    sticker_info = {
        'width': message_sticker.width,
        'height': message_sticker.height,
        'emoji': message_sticker.emoji,
        'set_name': message_sticker.set_name,
        'file_size': message_sticker.file_size,
    }
    prev_message = message_history.get(chat_id, None)
    prev_sent_message = sent_message_history.get(chat_id, None)
    print(chat_id, message_sticker)

    if prev_message == sticker_info and prev_sent_message != sticker_info:
        bot.send_sticker(chat_id, message_sticker.file_id)
        sent_message_history[chat_id] = sticker_info

    message_history[chat_id] = sticker_info


if __name__ == '__main__':
    bot.polling()