import telebot

TOKEN = "8242252445:AAH_NHbTNtxfUNqB6d-AiaqR5QvKNdBPKNg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Bot chal raha hai ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot started...")
bot.polling()
