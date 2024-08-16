from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from config import TELEGRAM_BOT_TOKEN
from financial_reporting import main

SAVE_FOLDER = "uploaded_files"  

# Create the folder if it doesn't exist
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'This is the telegram chatbot that will calculate the financial documents')

async def send_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    file_path = "Data/Bangan1.jpg"
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as document:
            await context.bot.send_document(chat_id=chat_id, document=document, read_timeout=120)
    else:
        await update.message.reply_text('Sorry, the document could not be found.')

async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = await context.bot.get_file(update.message.document.file_id)
    
    file_path = os.path.join(SAVE_FOLDER, update.message.document.file_name)
    
    # await file.download_to_drive(custom_path=file_path)  # Use download instead of download_to_drive
    # await update.message.reply_text(f'File saved to {file_path}')

    await file.download_to_drive(custom_path=file_path)

    output = main(file_path=file_path)

    await update.message.reply_text(output)


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("send", send_document))
app.add_handler(MessageHandler(filters.Document.ALL, file_handler))

app.run_polling()