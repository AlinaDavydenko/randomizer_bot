import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher

bot, dp = get_bot_and_dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        """Hi! I am a petyshok bot. Once a day i will choose a gay, good luck!"""
        )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "This bot chooses a random person every day.\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help"
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
