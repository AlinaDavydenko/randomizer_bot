import asyncio
from aiogram import types
from aiogram.filters.command import Command
from core.sql_core.connect_to_host import db
from core.aiogram_bot.list_keyboard import keyboard_for_bot
from core.aiogram_bot.send_messages import send_message_all_statistics, send_message_all_users

def create_bot_keyboard(dp):
    """Bot inline keyboard"""

    @dp.message(Command("keyboard"))
    async def keyboard(message: types.Message):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard_for_bot)
        await message.answer(text='Выбери опции', reply_markup=kb)

    @dp.message(lambda message: message.text == "Статистика за всё время")
    async def handle_statistics(message: types.Message):
        group_id = message.chat.id
        await send_message_all_statistics(group_id)

    @dp.message(lambda message: message.text == "Показать участников")
    async def handle_members(message: types.Message):
        group_id = message.chat.id
        await send_message_all_users(group_id)
