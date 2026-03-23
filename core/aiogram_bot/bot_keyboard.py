import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from core.aiogram_bot.list_keyboard import keyboard_for_bot

def create_bot_keyboard(dp):
    """Bot inline keyboard"""
    @dp.message(Command("keyboard"))
    async def keyboard(message: types.Message):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard_for_bot)
        await message.answer(text='Choose option', reply_markup=kb)

