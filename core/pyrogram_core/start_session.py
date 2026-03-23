from pyrogram import Client, filters
import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import BOT_TOKEN, API_HASH, API_ID
import asyncio

app = Client(
    "my_bot",
    api_id=API_ID, 
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)



async def main():
    stop_event = asyncio.Event()  # ✅ Created inside the loop

    @app.on_message(filters.all)  # ✅ Handler defined here — uses same stop_event
    async def get_id(client, message):
        print(f"Chat ID:    {message.chat.id}")
        print(f"Chat Title: {message.chat.title}")
        stop_event.set()  # ✅ Sets the correct event

    await app.start()
    print("Bot started. Send a message to the chat to get the ID...")
    await stop_event.wait()
    await app.stop()
    print("Bot stopped.")

asyncio.run(main())

# async def search_channel_id(chat_name: str) -> int:
#     """Get channel id using this name"""
#     async for dialog in app.get_dialogs():
#         if chat_name in dialog.chat.title:
#             return dialog.chat.id
#     return None 

async def get_all_members(app, chat_id):
    """Get all members in the chat"""
    # Get members
    members = []
    async for member in app.get_chat_members(chat_id):
        members.append(member)
    return members
    

# async def main():
#     await app.start()
#     name_channel = 'Воскрешение пидер бота'

    
    # all_members = await get_all_members(app, chat_id)
    # return all_members


    # await app.stop()

# asyncio.run(main())

# curl "https://api.telegram.org/bot8195985447:AAFLLaeY2UxvgOnLyuyHJRh2FQGwvRGPkUk/getUpdates"