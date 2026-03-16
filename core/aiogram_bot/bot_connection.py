import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import BOT_TOKEN
from aiogram import Dispatcher, Bot 

def get_bot_and_dispatcher():
    """Get bot token and create dispatcher"""
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    return bot, dp
