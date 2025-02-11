import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_API_TOKEN' with the provided API token
API_TOKEN = '7683114012:AAHv4veCAJRRDFrfthBtxC0bCVwMc4eGpww'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am the Knky.co bot.')

def main():
    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
