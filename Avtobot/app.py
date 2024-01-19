from details.handlers import *
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    Dispatcher
)
from telegram import Bot, Update
from details.handlers import (
    start,
    text,
    update,
)
from flask import Flask, request
TOKEN = "6385184981:AAH5Iv-UWMA3M_vix1b3NDclgkPGrWIx6dk"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)
app = Flask(__name__)
@app.route('/webhook', methods=['GET',"POST"])
def register_handlers():
    if request.method == "GET":
        return "Avtoelon.uz boti ishga tushdi!"
    if request.method == 'POST':

        body = request.get_json()
        update = Update.de_json()
        dispatcher.add_handler(CommandHandler("start", start)),
        dispatcher.add_handler(MessageHandler(Filters.text("Upgrade🔄"),update)),
        dispatcher.add_handler(MessageHandler(Filters.text, text)),
        dispatcher.add_handler(CallbackQueryHandler(button_callback)),


        dispatcher.process_update(update)

        return {'message': "ok"}


app.run(debug=True)
