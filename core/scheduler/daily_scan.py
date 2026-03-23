from core.aiogram_bot.bot_commands import chat_id_storage
from core.pyrogram_core.scan_users import scan_members

async def daily_scan(db):
    chat_id = chat_id_storage["chat_id"]

    if chat_id is None:
        print("Scheduler: no chat ID yet, skipping...")
        return

    print("Scheduler: starting daily scan...")
    members = await scan_members(chat_id)

    for member in members:
        db.insert_user_to_table(member["id"], member["username"])

    print(f"Scheduler: saved {len(members)} members")