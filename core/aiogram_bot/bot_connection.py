import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import BOT_TOKEN
from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession()
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()


def get_bot_and_dispatcher():
    """Get bot token and create dispatcher"""
    return bot, dp
