import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

# ==========================
# СКРИПТЫ
# ==========================
scripts = {
    "mm2": """```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/xv3gasx/Murder-Mystery-2/refs/heads/main/Release.lua"))()
```""",

    "script2": """```lua
-- Вставь сюда второй скрипт.
```""",

    "script3": """```lua
-- Вставь сюда третий скрипт
```"""
}

# ==========================
# /start
# ==========================
@bot.message_handler(commands=["start"])
def start(message):
    args = message.text.split(maxsplit=1)

    if len(args) > 1 and args[1] in scripts:

        keyboard = InlineKeyboardMarkup()
        keyboard.add(
            InlineKeyboardButton(
                "📢 Наш Telegram-канал",
                url="https://t.me/DeltaWScripts"
            )
        )

        bot.send_message(
            message.chat.id,
            f"✅ Вот твой скрипт:\n\n{scripts[args[1]]}",
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(
            InlineKeyboardButton(
                "📢 Наш Telegram-канал",
                url="https://t.me/DeltaWScripts"
            )
        )

        bot.send_message(
            message.chat.id,
            "👋 Добро пожаловать!\n\nПерейди в канал и нажми кнопку «Получить скрипт».",
            reply_markup=keyboard
        )

print("Бот запущен!")
bot.infinity_polling()
