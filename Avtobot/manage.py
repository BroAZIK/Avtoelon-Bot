from details.handlers import *
import requests
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from details.handlers import (
    start,
    text,
    update,
    moto_app,
)
TOKEN = "6385184981:AAH5Iv-UWMA3M_vix1b3NDclgkPGrWIx6dk"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def register_handlers():

    dispatcher.add_handler(CommandHandler("start", start)),
    dispatcher.add_handler(MessageHandler(Filters.text("Upgrade🔄"),update)),
    # dispatcher.add_handler(MessageHandler(Filters.text("Mototsikllar🏍"), moto_app)),
    dispatcher.add_handler(MessageHandler(Filters.text, text)),
    dispatcher.add_handler(CallbackQueryHandler(button_callback)),


    

    updater.start_polling()
    updater.idle()


register_handlers()