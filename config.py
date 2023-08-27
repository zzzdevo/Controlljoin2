from pyrogram import Client
from asBASE import asJSON

db = asJSON("as.json")
###


SUDORS = [833360381] # ايديات المطورين
API_ID = 12962251
API_HASH = "b51499523800add51e4530c6f552dbc8"
TOKEN = "6370078303:AAEK7Q0XNR-jHG3ntVrYpf7lClBDV_hQzw0" # التوكن
bot = Client("control",API_ID,API_HASH,bot_token=TOKEN,in_memory=True)
bot_id = TOKEN.split(":")[0]
