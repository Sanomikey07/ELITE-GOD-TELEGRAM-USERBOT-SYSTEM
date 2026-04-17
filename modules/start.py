from pyrogram import Client, filters

app = Client("gamebot")

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "🔥 Welcome to ELITE GAME BOT\n\n"
        "Commands:\n"
        "/balance\n"
        "/clan\n"
        "/war\n"
        "/bet\n"
        "/map\n"
        "/leaderboard"
    )
