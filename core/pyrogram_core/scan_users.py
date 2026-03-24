async def get_all_members(app, chat_id):
    """Get all members in the chat"""
    # Get members
    members_list = []
    async for member in app.get_chat_members(chat_id):
        members_list.append(member)
        return members_list
