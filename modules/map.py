from pyrogram import Client, filters
from database import cursor

app = Client("gamebot")

@app.on_message(filters.command("map"))
async def map(client, message):
    cursor.execute("SELECT * FROM map_tiles")
    data = cursor.fetchall()

    text = "🌍 WORLD MAP\n\n"

    for d in data:
        text += f"{d[0]},{d[1]} → {d[2]}\n"

    await message.reply(text)
