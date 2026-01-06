import telebot
from config import BOT_API_KEY
from user_messages import registrar_handlers

bot = telebot.TeleBot(BOT_API_KEY)

registrar_handlers(bot)

print("🤖 Bot em execução...")
bot.polling(none_stop=True, interval=0, timeout=10)
