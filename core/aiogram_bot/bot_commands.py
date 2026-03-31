from aiogram import types
from aiogram.filters.command import Command
from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import Utils


def register_handlers(dp, user_client):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        if message.chat.type in ("group", "supergroup"):
            chat_id = message.chat.id
            print(f"[DEBUG] Chat type: {message.chat.type}, chat_id: {chat_id}")

            # Add chat_id into PostgreSQL
            utils_object = Utils(db)
            utils_object.insert_chat_id(chat_id)
            await message.answer(
                """Привет! Я - петушок бот. Один раз в день под восход солнца прокукарекает один петушок, удачи!
                Ps: Важное правило, кто хочет учавствовать в игре, важно написать боту, чтобы он увидел тебя!
                Просто нажми команду /lets_play или другие команды
                Посмотри /help"""
            )
            await message.answer(f"Chat ID: `{chat_id}`", parse_mode="Markdown")
        else:
            print(f"Private chat — user ID: {message.chat.id}")

    @dp.message(Command("lets_play"))
    async def cmd_lets_play(message: types.Message):
        await message.answer("""Я увидел тебя!""")

    @dp.message(Command("help"))
    async def cmd_help(message: types.Message):
        await message.answer(
            "This bot chooses a random person every day.\n"
            "Commands:\n"
            "/start - Start the bot\n"
            "/help - Show this help\n"
            "/keyboard - Show keyboard with extra commands\n"
            "/lets_play - I wanna play with you, gays"
        )
