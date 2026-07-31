import telebot

TOKEN = "8849624925:AAF01JH8vA8atOT1fDG75CQStqXwagLwehA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет!")

bot.infinity_polling()
