import telebot

# Replace ‘YOUR_API_TOKEN’ with the API token you received from the BotFather
API_TOKEN = "6941904293:AAHMBb2_Mq1-tX6zWRp43SP4LMuwVCpnve4"

bot = telebot.TeleBot(API_TOKEN)

# Define a command handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to YourBot! Type /info to get more information.")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "This is a simple Telegram bot implemented in Python.")

# Define a message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()