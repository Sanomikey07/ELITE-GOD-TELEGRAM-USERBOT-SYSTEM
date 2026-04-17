from pyrogram import Client
import os

app = Client(
    "gamebot",
    bot_token=os.getenv("BOT_TOKEN"),
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH")
)

# auto-load modules
import os
for f in os.listdir("modules"):
    if f.endswith(".py"):
        __import__(f"modules.{f[:-3]}")

print("🤖 GAME BOT RUNNING...")
app.run()
