import telebot

from logic import gen_pass

bot = telebot.TeleBot('7980289623:AAHSbGizH1P1cZNSrEsi417Ymf47B3H355w')
@bot.message_handler(commands=['start', 'help'])
def send_hello(message):
    bot.send_message(message.chat.id, 'Привет! я тестовый бот ')
@bot.message_handler(commands=['pas'])
def send_hello(message):
    bot.send_message(message.chat.id, str(gen_pass(2)))


bot.infinity_polling()
