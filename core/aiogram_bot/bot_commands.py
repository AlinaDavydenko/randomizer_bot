from aiogram import types
from aiogram.filters.command import Command
from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import ManipulateUsers


def register_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        if message.chat.type in ("group", "supergroup"):
            chat_id = message.chat.id

            await message.answer(
                "Привет! Я - петушок бот.\nОдин раз в день под восход солнца прокукарекает один петушок, удачи!\n\n"
                "Добавься в игру! /register\n\n"
                "Посмотри /help"
            )
        else:
            print(f"Private chat — user ID: {message.chat.id}")

    @dp.message(Command("register"))
    async def cmd_register(message: types.Message):
        user_id = message.from_user.id
        group_id = message.chat.id

        manipulate_user = ManipulateUsers(db)
        manipulate_user.insert_user_to_table(user_id, group_id)

        await message.answer(text=f"{message.from_user.full_name}, ты добавлен в игру 🐓")

    @dp.message(Command("help"))
    async def cmd_help(message: types.Message):
        await message.answer(
            "This bot chooses a random person every day.\n"
            "Commands:\n"
            "/register - Registration\n"
            "/start - Start the bot\n"
            "/help - Show this help\n"
            "/keyboard - Show keyboard with extra commands\n"
        )
