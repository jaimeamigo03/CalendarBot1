import constants as keys
from telegram.ext import *
import responses as R
import calendar_setup as C

print("Bot started...")

def crear_evento(update, context):
    text = str(update.message.text)
    C.main(R.create_event(text))
    update.message.reply_text("Listo") 

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("evento", crear_evento))

    updater.start_polling(1)
    updater.idle()

main() 