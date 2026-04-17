from pyrogram import Client, filters
import random

app = Client("gamebot")

@app.on_message(filters.command("bet"))
async def bet(client, message):
    amount = int(message.text.split()[1])

    if random.choice([True, False]):
        await message.reply(f"🎰 You WON {amount}")
    else:
        await message.reply("💀 You LOST")
