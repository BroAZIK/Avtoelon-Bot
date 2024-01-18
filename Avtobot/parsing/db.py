from tinydb import TinyDB, Query
from tinydb.database import Document
from pprint import pprint
import json
from datetime import datetime
current_time = datetime.now()
User = Query()


with open("parsing/moto/page_Moto.json", "r") as db:
    # Faylni o'qish va uni boshqa o'zgaruvchiga joylashtirish uchun kerak bo'lgan amallarni bajarishingiz mumkin
    # Misol uchun:
    moto_data = json.load(db)

with open("parsing/yengil/page_Avto.json", "r") as db:

    avto_data = json.load(db)

db1 = TinyDB('database/harakat.json', indent=4)
db2 = TinyDB('database/index.json', indent=4)
db3 = TinyDB('database/users.json', indent=4)


stage      = db1.table('stage')
users      = db3.table('Users')
index      = db2.table('index')
index_moto = db2.table('index_moto')
avto_time  = db2.table("avto_time")
moto_time  = db2.table("moto_time")

def upd(table):
    if table == "avto":
        uzun = len(avto_time.all())+1
        doc = Document(
            value={"avto_upd": current_time.strftime("%Y-%m-%d %H:%M:%S")},
            doc_id=uzun
        )
        avto_time.insert(doc)
    elif table == "moto":
        uzun = len(moto_time.all())+1
        doc = Document(
            value={"moto_upd": current_time.strftime("%Y-%m-%d %H:%M:%S")},
            doc_id=uzun
        )
        moto_time.insert(doc)


def soni():

    user = users.all()
    moto = moto_data
    avto = avto_data
    # pprint(avto)
    # pprint(moto)
    return {"users": len(user), "motos": len(moto), "avtos": len(avto)}
    

def get(table, user_id=None):

    if table == "stage":
        return stage.get(doc_id=user_id)
    
    elif table == "users":
        return users.all()
    
    elif table == "index":
        return index.get(doc_id=user_id)
    
    elif table == "index_moto":
        return index_moto.get(doc_id=user_id)
    
    elif table == "avtodb":
        return avto_data
    
    elif table == "motodb":
        return moto_data
    
    elif table == "avto_time":
        return avto_time.get(doc_id=len(avto_time.all()))
    
    elif table == "moto_time":
        return moto_time.get(doc_id=len(moto_time.all()))

def insert(table, user_id, data):

    if table == "stage":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        stage.insert(doc)
    
    elif table == "users":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        users.insert(doc)
    
    elif table == "index":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        index.insert(doc)

        return user_id
    elif table == "index_moto":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        index_moto.insert(doc)

        return user_id

def update_db(table, user_id, data):


    if table == "stage":
        stage.update(data, doc_ids=[user_id])
    
    elif table == "users":
        users.update(data, doc_ids=[user_id])
    
    elif table == "index":
        index.update(data, doc_ids=[user_id])
    elif table == "index_moto":
        index_moto.update(data, doc_ids=[user_id])
def delete(table, user_id):

    if table == "index":
        if index.contains(doc_id=user_id):
            doc = index.remove(doc_ids=[user_id])
            print(doc)
        else:
            print("user-not-exist")