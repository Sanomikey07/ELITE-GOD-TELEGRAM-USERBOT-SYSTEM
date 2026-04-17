from pyrogram import Client, filters
from database import cursor

app = Client("gamebot")

@app.on_message(filters.command("leaderboard"))
async def lb(client, message):
    cursor.execute("SELECT user_id,xp FROM users ORDER BY xp DESC LIMIT 5")
    data = cursor.fetchall()

    text = "🏆 LEADERBOARD\n\n"

    for i,d in enumerate(data,1):
        text += f"{i}. {d[0]} - {d[1]} XP\n"

    await message.reply(text)
