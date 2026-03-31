from pyrogram import Client
import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import BOT_TOKEN, API_HASH, API_ID
import asyncio

user_client = Client(
    "my_account",
    api_id=API_ID,
    api_hash=API_HASH
)