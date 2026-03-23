import asyncio

async def get_all_members(app, chat_id):
    """Get all members in the chat"""
    # Get members
    async for member in app.get_chat_members(chat_id):
        print(member)
