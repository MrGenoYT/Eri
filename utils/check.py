import time

user_last_reply = {}

async def should_reply_logic(message):
    uid = str(message.author.id)
    now = time.time()
    last = user_last_reply.get(uid, 0)
    user_last_reply[uid] = now
    if now - last > 300: return True
    return random.choice([True, False])
