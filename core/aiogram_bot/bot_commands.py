from aiogram import types
from aiogram.filters.command import Command

chat_id_storage = {"chat_id": None}

def register_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer(
            """Hi! I am a petyshok bot. Once a day i will choose a gay, good luck!"""
        )
        if message.chat.type in ("group", "supergroup"):
            chat_id = message.chat.id
            print(f"Group Chat ID: {chat_id}")
            await message.answer(f"Chat ID: `{chat_id}`", parse_mode="Markdown")
            chat_id_storage["chat_id"] = chat_id
        else:
            print(f"Private chat — user ID: {message.chat.id}")

    @dp.message(Command("help"))
    async def cmd_help(message: types.Message):
        await message.answer(
            "This bot chooses a random person every day.\n"
            "Commands:\n"
            "/start - Start the bot\n"
            "/help - Show this help\n"
            "/keyboard - Show keyboard with extra commands"
        )
