from aiogram import types, Router
from aiogram.filters.command import Command
from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import ManipulateUsers
from core.aiogram_bot.send_messages_keyboard import send_message_all_statistics, send_message_all_users


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.chat.type in ("group", "supergroup"):

        await message.answer(
            "Привет! Я - петушок бот.\n\nОдин раз в день под восход солнца прокукарекает один петушок, удачи!\n\n"
            "Добавься в игру! /register\n\n"
        )
    else:
        print(f"Private chat — user ID: {message.chat.id}")


@router.message(Command("register"))
async def cmd_register(message: types.Message):
    user_id = message.from_user.id
    group_id = message.chat.id

    manipulate_user = ManipulateUsers(db)
    manipulate_user.insert_user_to_table(user_id, group_id)

    await message.answer(text=f"{message.from_user.full_name}, ты добавлен в игру 🐓")


@router.message(Command("all_statistics"))
async def cmd_all_statistics(message: types.Message):
    group_id = message.chat.id
    await send_message_all_statistics(group_id)


@router.message(Command("all_users"))
async def handle_members(message: types.Message):
    group_id = message.chat.id
    await send_message_all_users(group_id)
