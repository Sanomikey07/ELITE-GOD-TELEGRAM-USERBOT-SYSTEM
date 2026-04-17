from pyrogram import Client, filters
from database import cursor, conn

app = Client("gamebot")

@app.on_message(filters.command("balance"))
async def balance(client, message):
    user = message.from_user.id

    cursor.execute("SELECT coins FROM users WHERE user_id=?", (user,))
    data = cursor.fetchone()

    coins = data[0] if data else 100

    await message.reply(f"💰 Balance: {coins}")
