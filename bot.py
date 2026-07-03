import telebot
import os

TOKEN = "8316342765:AAGweEHWcSUHXDVp-4oi-lFZvZrryvooOVc"
WEBSITE_URL = os.getenv('WEBSITE_URL', 'https://yourapp.railway.app')  # بعدا تنظیم می‌کنیم

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """
سلام! 🎡
من بات گردونه شانس هستم.

دستورات:
/link - لینک سایت
/help - راهنما
    """)

@bot.message_handler(commands=['link'])
def send_link(message):
    bot.send_message(message.chat.id, f"""
🔗 لینک سایت:

{WEBSITE_URL}

برو و شروع کن! 🎰
    """)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, """
📖 راهنما:

/start - شروع
/link - دریافت لینک سایت
/help - این پیام
    """)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "سلام! برای راهنما /help رو بفرست.")

if __name__ == '__main__':
    print("بات شروع شد...")
    bot.infinity_polling()
