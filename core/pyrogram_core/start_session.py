from pyrogram import Client
import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import BOT_TOKEN, API_HASH, API_ID
import asyncio

def create_user_client():
    return Client(
        "my_account",
        api_id=API_ID,
        api_hash=API_HASH
    )