async def get_all_members(app, chat_id):
    members_list = []
    async for dialog in app.get_dialogs():
        if dialog.chat.id == chat_id:
            print(f"[DEBUG] Found chat: {dialog.chat.title}")
            break
    async for member in app.get_chat_members(chat_id):
        user = member.user
        if not user.is_bot:  # исключаем ботов
            members_list.append({
                "id": user.id,
                "name": f"{user.first_name} {user.last_name or ''}".strip(),
                "username": user.username
            })
    return members_list
