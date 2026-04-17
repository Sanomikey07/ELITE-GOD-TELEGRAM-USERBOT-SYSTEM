from pyrogram import Client, filters
from database import cursor, conn

app = Client("gamebot")

@app.on_message(filters.command("createclan"))
async def create(client, message):
    name = message.text.split(" ",1)[1]
    user = message.from_user.id

    cursor.execute("INSERT OR IGNORE INTO clans VALUES (?,?,1000)", (name,user))
    conn.commit()

    await message.reply(f"⚔️ Clan {name} created!")
