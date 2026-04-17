from pyrogram import Client, filters
import random

app = Client("gamebot")

@app.on_message(filters.command("war"))
async def war(client, message):
    c1 = message.text.split()[1]
    c2 = message.text.split()[2]

    winner = random.choice([c1, c2])

    await message.reply(f"⚔️ Winner: {winner}")
