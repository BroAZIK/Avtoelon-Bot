from telegram import Bot
from parsing.db import get

# Bot tokenini o'zgartiring
TOKEN = '6385184981:AAH5Iv-UWMA3M_vix1b3NDclgkPGrWIx6dk'
bot = Bot(token=TOKEN)

users = get(table="users")
def all_mes(category):
    if category == "moto":
        for user in users:
            user_id = user['user_id']
            bot.send_message(chat_id=user_id,text="Mototsikl elonlari yangilandi!🏍")
    if category == "avto":
        for user in users:
            user_id = user['user_id']
            bot.send_message(chat_id=user_id,text="Avtomobil elonlari yangilandi!🚙")


