from bot_instance import bot
import os
from threading import Thread

# load modules
for file in os.listdir("modules"):
    if file.endswith(".py"):
        __import__(f"modules.{file[:-3]}")

# control bot
from control_bot.bot import app as control_app
Thread(target=control_app.run).start()

print("🔥 ELITE SYSTEM RUNNING")

bot.run_until_disconnected()
