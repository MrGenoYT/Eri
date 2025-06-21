import random
from ai.gemini_ai import ai_client
from db import mongo
from utils import checks, helpers

async def handle_message(bot, message):
    if message.author.bot: return

    await mongo.log_message(str(message.guild.id), str(message.author.id), message.content)
    
    should_reply = await checks.should_reply_logic(message)
    if should_reply or bot.user in message.mentions or helpers.is_inactive(message):
        history = await mongo.fetch_history(str(message.guild.id), str(message.author.id))
        reply = await ai_client.chat(message.content, history)
        await message.channel.send(reply)

        if random.randint(1, 100) == 1:
            await helpers.send_random_meme(message.channel)

        if 'draw' in message.content.lower():
            image_url = await ai_client.generate_image(message.content)
            await message.channel.send(image_url)
