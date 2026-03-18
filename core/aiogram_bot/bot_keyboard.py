import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher

bot, dp = get_bot_and_dispatcher()

