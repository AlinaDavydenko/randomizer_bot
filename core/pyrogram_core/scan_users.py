from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import ManipulateUsers, Utils
from core.utils.get_from_dictionary import get_params_from_dict


async def get_all_members(app):
    """Scan all members"""

    # Create objects
    utils_object = Utils(db)
    manipulate_users = ManipulateUsers(db)

    # Get chat id
    chat_id = utils_object.get_chat_id()

    if not chat_id:
        print('Not chat_id')
        return []
    
    members_list = []
    async for dialog in app.get_dialogs():
        if dialog.chat.id == chat_id:
            print(f"[DEBUG] Found chat: {dialog.chat.title}")
            break

    async for member in app.get_chat_members(chat_id):
        user = member.user
        if not user.is_bot:  # исключаем ботов
            members_list.append(
                {
                    "id": user.id,
                    "name": f"{user.first_name} {user.last_name or ''}".strip(),
                    "username": user.username,
                }
            )

    for element in members_list:
        user_name, user_id = get_params_from_dict(element)
        manipulate_users.insert_user_to_table(user_id, user_name)
    
    print(members_list)

    return members_list
