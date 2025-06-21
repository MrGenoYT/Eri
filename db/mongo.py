from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['eri_database']

async def log_message(guild_id, user_id, content):
    db['chat_logs'].insert_one({"guild": guild_id, "user": user_id, "msg": content})

async def fetch_history(guild_id, user_id):
    return list(db['chat_logs'].find({"guild": guild_id, "user": user_id}))

async def clear_data(guild_id):
    db['chat_logs'].delete_many({"guild": guild_id})

async def update_persona(data):
    db['config'].update_one({"_id": "persona"}, {"$set": data}, upsert=True)
