import telebot
from telebot import types

TOKEN = '7575411916:AAHyK0mYKECdUDXkeRr3EiL4EgI4KNWDzPQ'
bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📖 Algebra darslari")
    btn2 = types.KeyboardButton("💬 Savol berish")
    btn3 = types.KeyboardButton("ℹ️ Bot haqida")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Salom! Quyidagilardan birini tanlang:", reply_markup=markup)

# Tugma orqali javoblar
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📖 Algebra darslari":
        bot.send_message(message.chat.id, "Algebra darslari ro‘yxati:\n1. Tenglamalar\n2. Sistemalar\n3. Funksiyalar")
    elif message.text == "💬 Savol berish":
        bot.send_message(message.chat.id, "Savolingizni yozing, men javob berishga harakat qilaman.")
    elif message.text == "ℹ️ Bot haqida":
        bot.send_message(message.chat.id, "Men Tohirjon tomonidan yaratilgan o‘quvchi uchun yordamchi Telegram botman.")
    else:
        bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")

# Botni ishga tushirish
bot.polling()
