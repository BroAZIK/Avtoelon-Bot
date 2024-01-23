from parsing.moto.main import moto_parser
from parsing.yengil.main import yengil_parser
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.parsemode import ParseMode
from parsing.db import get, update_db, insert, delete, soni, upd
from .items.buttons import *
from pprint import pprint
from parsing.moto.main import moto_parser
from parsing.yengil.main import yengil_parser
import json
from datetime import datetime
from all_message import *
current_time = datetime.now()


with open("parsing/yengil/page_Avto.json", 'r') as file:
    avto_datas = json.load(file)
with open("parsing/moto/page_Moto.json", "r") as file:
    Moto_datas = json.load(file)

Admin_id = 5027127747
channel = "@Tarjima_Kinolar_Celestial"
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    first = update.effective_chat.first_name
    last = update.effective_chat.last_name
    counts = soni()

    if user_id == Admin_id:
        user = {'stage': "start"}
        try:
            insert(table="stage",user_id=user_id, data=user)
        except:
            pass
            
            aupd = get(table="avto_time")['avto_upd']
            mupd = get(table="moto_time")['moto_upd']
        update.message.reply_text(
            text=f"Salom Admin!\nBot_members: {counts['users']}\nBot_motos: {counts['motos']}\nBot_avtos: {counts['avtos']}\n\nLast avto update: {aupd}\nLast moto update: {mupd}",
            reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
        )

    else:
        try:
            insert(table="users", user_id=user_id, data={"user_id":user_id, "first_name": first, "last_name": last})
            insert(table="stage", user_id=user_id, data={'stage': "start"})
            try:
                update.message.reply_text(
                    text=f"Assalomu Aleykum {first}, Botimizga xush kelibsiz☺️!",
                    reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
                )
                update.message.reply_text(
                    text="Siz asosiy menyudasiz🔝"
                )
            except:
                pass
        except:
            try:
                update_db(table="stage", user_id=user_id, data={'stage': "start"})
            except:
                insert(table="stage", user_id=user_id, data={'stage': "start"})
            update.message.reply_text(
                text="Siz asosiy menyudasiz🔝",
                reply_markup=ReplyKeyboardMarkup(all_start, resize_keyboard=True)
            )
        try:
            insert(table="users", user_id=user_id, data={"user_id":user_id, "first_name": first, "last_name": last})
        except:
            pass

def text(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    text = update.message.text
    son = soni()

    if text == "Avtomobillar🚙":
        update_db(table="stage",user_id=user_id, data={"stage": "avto"})
        update.message.reply_text(
            text=f"Botdagi avtomobillar soni: {son['avtos']}",
            reply_markup=ReplyKeyboardMarkup(upgrade, resize_keyboard=True)
        )

    elif text == "Mototsikllar🏍":
        if Admin_id == user_id:
            update_db(table="stage", user_id=user_id, data={'stage': "moto"})
            update.message.reply_text(
                text=f"Botdagi mototsikllar soni: {son['motos']}",
                reply_markup=ReplyKeyboardMarkup(upgrade, resize_keyboard=True)
            )
        else:
            try:
                insert(table="index_moto", user_id=user_id, data={"index_moto": 5})
            except:
            # update_db(table="index", user_id=user_id, data={"index": 5})
                pass           
            update_db(table="stage",user_id=user_id, data={"stage": "moto"})
            index = get(table="index_moto",user_id=user_id)['index_moto']
            index2 = index+5
            update_db(table="index_moto", user_id=user_id, data={"index_moto": index2})
            if index < 20:
                for i in range(index, index2):
                    try:
                        data = Moto_datas[i]
                        detail = data['detail']['details']
                        detail = detail.split(", ")
                        brand = data['detail']['title']
                        price = data['unitPrice']
                        city = detail[0]
                        year = detail[1]
                        mator = detail[2]
                        more = data['detail']['more']

                        image = data['detail']['images']
                        url = data['url']
                        keyboard = [[InlineKeyboardButton("Mototsiklni ko'rish👀", url=url)]]

                        update.message.reply_photo(
                        photo=image,
                        caption=f"<b>Mototsikl brendi:</b> {brand}\n<b>Narxi:</b> {price}$\n<b>Mator:</b> {mator}\n<b>Ko'proq malumot:</b> {more}\n\n<b>Yili:</b> {year}\n<b>Manzil:</b> {city}", parse_mode=ParseMode.HTML,
                        # parse_mode='MarkdownV2',
                        reply_markup=InlineKeyboardMarkup(keyboard)
                    )
                    except:
                        print("xato!")                
                update.message.reply_text(
                        text=f"Yengil Mototsikllar: {index2}/20",
                        reply_markup=ReplyKeyboardMarkup(back_2,resize_keyboard=True)
                    )
            if index >= 20:
                update.message.reply_text(
                text="Boshqa Mototsikllar topilmadi !",
                reply_markup=ReplyKeyboardMarkup(back_3, resize_keyboard=True)
            )
            
    elif text == "Ortga⬅️":
        if Admin_id == user_id:
            update.message.reply_text(
                text="Asosiy menyu🔝",
                reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
            )
        else:
            start(update=update, context=context)
            
    elif text == "Yengil Avtomobillar🚙":

        try:
            insert(table="index", user_id=user_id, data={"index_moto": 0,"index": 5})
        except:
            # update_db(table="index", user_id=user_id, data={"index": 5})
            pass
        index = get(table="index",user_id=user_id)['index']
        index2 = index+5
        update_db(table="index", user_id=user_id, data={"index": index2})
        if index < 20:
            for i in range(index, index2):
                try:
                    data = avto_datas[i]
                    detail = data['detail']['details']
                    detail = detail.split(", ")
                    brand = data['detail']['title']
                    price = data['unitPrice']
                    city = detail[0]
                    year = detail[1]
                    mator = detail[2]
                    more = data['detail']['more']

                    image = data['detail']['images']
                    url = data['url']
                    keyboard = [[InlineKeyboardButton("Avtomobilni ko'rish👀", url=url)]]

                    update.message.reply_photo(
                        photo=image,
                        caption=f"<b>Avtomobil brendi:</b> {brand}\n<b>Narxi:</b> {price}$\n<b>Mator:</b> {mator}\n<b>Ko'proq malumot:</b> {more}\n\n<b>Yili:</b> {year}\n<b>Manzil:</b> {city}", parse_mode=ParseMode.HTML,
                        # parse_mode='MarkdownV2',
                        reply_markup=InlineKeyboardMarkup(keyboard)
                    )
                except:
            
                    print("xato!")                
            update.message.reply_text(
                        text=f"Yengil Avtomobillar: {index2}/20",
                        reply_markup=ReplyKeyboardMarkup(back_2,resize_keyboard=True)
                    )
        if index >= 20:
            update.message.reply_text(
                text="Boshqa avtomobillar topilmadi !",
                reply_markup=ReplyKeyboardMarkup(back_3, resize_keyboard=True)
            )

    elif text == "Qayta ko'rish🔄":
        update.message.reply_text(
            text="Avtomobillarni qayta ko'rish!"
        )
    


        stage = get(table="stage", user_id=user_id)

        if stage == "avto":

            update_db(table="index",user_id=user_id, data={"index": 0})
            index = get(table="index",user_id=user_id)['index']
            index2 = index+5
            update_db(table="index", user_id=user_id, data={"index": index2})
        
            if index < 20:
                for i in range(index, index2):
                    try:
                        data = avto_datas[i]
                        detail = data['detail']['details']
                        detail = detail.split(", ")
                        brand = data['detail']['title']
                        price = data['unitPrice']
                        city = detail[0]
                        year = detail[1]
                        mator = detail[2]
                        more = data['detail']['more']

                        image = data['detail']['images']
                        url = data['url']
                        keyboard = [[InlineKeyboardButton("Avtomobilni ko'rish👀", url=url)]]

                        update.message.reply_photo(
                        photo=image,
                        caption=f"<b>Avtomobil brendi:</b> {brand}\n<b>Narxi:</b> {price}$\n<b>Mator:</b> {mator}\n<b>Ko'proq malumot:</b> {more}\n\n<b>Yili:</b> {year}\n<b>Manzil:</b> {city}", parse_mode=ParseMode.HTML,
                        # parse_mode='MarkdownV2',
                        reply_markup=InlineKeyboardMarkup(keyboard)
                    )
                    except:
                        print("xato!") 

                update.message.reply_text(
                text=f"Yengil Avtomobillar: {index2}/20",
                reply_markup=ReplyKeyboardMarkup(back_2,resize_keyboard=True)
                    )   
        else:
            update_db(table="index_moto",user_id=user_id, data={"index_moto": 0})
            index = get(table="index_moto",user_id=user_id)['index_moto']
            index2 = index+5
            update_db(table="index_moto", user_id=user_id, data={"index_moto": index2})
        
            if index < 20:
                for i in range(index, index2):
                    try:
                        data = Moto_datas[i]
                        detail = data['detail']['details']
                        detail = detail.split(", ")
                        brand = data['detail']['title']
                        price = data['unitPrice']
                        city = detail[0]
                        year = detail[1]
                        mator = detail[2]
                        more = data['detail']['more']

                        image = data['detail']['images']
                        url = data['url']
                        keyboard = [[InlineKeyboardButton("Mototsiklni ko'rish👀", url=url)]]

                        update.message.reply_photo(
                        photo=image,
                        caption=f"<b>Mototsikl brendi:</b> {brand}\n<b>Narxi:</b> {price}$\n<b>Mator:</b> {mator}\n<b>Ko'proq malumot:</b> {more}\n\n<b>Yili:</b> {year}\n<b>Manzil:</b> {city}", parse_mode=ParseMode.HTML,
                        # parse_mode='MarkdownV2',
                        reply_markup=InlineKeyboardMarkup(keyboard)
                    )
                    except:
                        print("xato!") 

                update.message.reply_text(
                text=f"Mototsikllar: {index2}/20",
                reply_markup=ReplyKeyboardMarkup(back_2,resize_keyboard=True)
                    ) 


    elif text == "Keyingisi⏭":
        
        stage = get(table="stage",user_id=user_id)['stage']

        if stage == "moto":
            index = get(table="index_moto",user_id=user_id)['index_moto']
            index2 = index+5
            update_db(table="index_moto", user_id=user_id, data={"index_moto": index2})
            if index < 20:
                for i in range(index, index2):
                    try:
                        data = Moto_datas[i]
                        detail = data['detail']['details']
                        detail = detail.split(", ")
                        brand = data['detail']['title']
                        price = data['unitPrice']
                        city = detail[0]
                        year = detail[1]
                        mator = detail[2]
                        more = data['detail']['more']

                        image = data['detail']['images']
                        url = data['url']
                        keyboard = [[InlineKeyboardButton("Mototsiklni ko'rish👀", url=url)]]

                        update.message.reply_photo(
                        photo=image,
                        caption=f"<b>Mototsikl brendi:</b> {brand}\n<b>Narxi:</b> {price}$\n<b>Mator:</b> {mator}\n<b>Ko'proq malumot:</b> {more}\n\n<b>Yili:</b> {year}\n<b>Manzil:</b> {city}", parse_mode=ParseMode.HTML,
                        # parse_mode='MarkdownV2',
                        reply_markup=InlineKeyboardMarkup(keyboard)
                    )
                    except:
                        print("xato!")                
                update.message.reply_text(
                        text=f"Yengil Mototsikllar: {index2}/20",
                        reply_markup=ReplyKeyboardMarkup(back_2,resize_keyboard=True)
                    )
            if index >= 20:
                update.message.reply_text(
                text="Boshqa avtomobillar topilmadi !",
                reply_markup=ReplyKeyboardMarkup(back_3, resize_keyboard=True)
            )  
        else:
            index = get(table="index",user_id=user_id)['index']
            if index < 20:
                index_2 = index+5
                update_db(table="index", user_id=user_id, data={"index": index_2})
        
                for i in range(index, index_2):
                    try:
                        data = avto_datas[i]
                        detail = data['detail']['details']
                        detail = detail.split(", ")

                        brand = data['detail']['title']
                        price = data['unitPrice']
                        city = detail[0]
                        year = detail[1]
                        mator = detail[2]
                        more = data['detail']['more']

                        image = data['detail']['images']
                        url = data['url']
                        keyboard = [[InlineKeyboardButton("Avtomobilni ko'rish👀", url=url)]]

                        update.message.reply_photo(
                    photo=image,
                    caption=f"<b>Avtomobil brendi:</b> {brand}\n<b>Narxi:</b> {price}$\n<b>Mator:</b> {mator}\n<b>Ko'proq malumot:</b> {more}\n\n<b>Yili:</b> {year}\n<b>Manzil:</b> {city}", parse_mode=ParseMode.HTML,
                    reply_markup=InlineKeyboardMarkup(keyboard))




                    except:
                        update.message.reply_text(
                    text="Boshqa avtomobillar topilmadi !",
                    reply_markup=ReplyKeyboardMarkup(back_3, resize_keyboard=True)
                )
            if index >= 20:
                update.message.reply_text(
                text="Boshqa avtomobillar topilmadi !",
                reply_markup=ReplyKeyboardMarkup(back_3, resize_keyboard=True)
            )
            else:
                update.message.reply_text(
                text=f"Yengil Avtomobillar: {index_2}/20",
                reply_markup=ReplyKeyboardMarkup(back_2,resize_keyboard=True)
                    )





    elif text == "Statistika📊":
        counts = soni()
        aupd = get(table="avto_time")['avto_upd']
        mupd = get(table="moto_time")['moto_upd']
        if Admin_id == user_id:
            update.message.reply_text(
            text=f"Salom Admin!\nBot_members: {counts['users']}\nBot_motos: {counts['motos']}\nBot_avtos: {counts['avtos']}\n\nLast avto update: {aupd}\nLast moto update: {mupd}",)

        else:
            update.message.reply_text(
                text=f"Salom Admin!\nBot_members: {counts['users']}\nBot_motos: {counts['motos']}\nBot_avtos: {counts['avtos']}\n\nLast avto update: {aupd}\nLast moto update: {mupd}",)

    elif text == "Admin👨🏻‍💻":
        update.message.reply_text(
            text="Bot admini: @Aziz_Khujamov 👨🏻‍💻"
        )

def moto_app(update: Update, context: CallbackContext):
    pass    

def update(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    stage = get(table="stage", user_id=user_id)
    if stage["stage"] == "avto":
        update.message.reply_text(
            text="Avtomobillar parseri ishga tushdi, kuting!..."
        )
        yengil_parser()
        formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
        upd(table="avto")
        users=get(table="users")
        for us in users:
            update_db(table="index", user_id=us['user_id'], data={"index": 0})
        update.message.reply_text(
            text=f"Avtomobillar ro'yxati yangilandi!, oxirgi yangilanish vaqti: {formatted_date} ",
            reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
        )
        all_mes(category="avto")

        update.message.reply_text(
            text="Hammaga xabar jo'natildi"
        )
    elif stage['stage'] == "moto":
        update.message.reply_text(
            text="Mototsikllar parseri ishga tushdi, kuting!..."
        )
        moto_parser()
        upd(table="moto")
        users = get(table="users")
        for us in users:
            update_db(table="index", user_id=us['user_id'], data={"index": 0})
        formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
        update.message.reply_text(
            text=f"Mototsikllar ro'yxati yangilandi!, oxirgi yangilanish vaqti: {formatted_date}",
            reply_markup=ReplyKeyboardMarkup(adm_start, resize_keyboard=True)
        )
        all_mes(category="moto")
        
        update.message.reply_text(
            text="Hammaga xabar jo'natildi"
        )
    

def button_callback(update: Update, context: CallbackContext):
    pass
    
