import asyncio
from core.sql_core.connect_to_host import db
from core.sql_core.sql_creating import CreateTables
from core.sql_core.sql_requests import Utils, ManipulateUsers
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.aiogram_bot.bot_commands import register_handlers
from core.aiogram_bot.bot_keyboard import create_bot_keyboard
from core.pyrogram_core.start_session import create_user_client
from core.pyrogram_core.scan_users import get_all_members
from core.utils.get_from_dictionary import get_params_from_dict
from core.scheduler.scheduler_jobs import scheduler
from core.logs_core.logger import setup_logger


async def main():
    """ Logging """
    # setup_logger()

    """ Connections """
    # Create bot connections
    bot, dp = get_bot_and_dispatcher()

    # Create databese connection
    db.connect()

    print(db.get_connection_status())

    """ Pyrogram client """
    # Create client for pyrogram
    user_client = create_user_client()
    await user_client.start()

    """ SQL core """
    # Create tables
    tables_manager = CreateTables(db)
    utils_object = Utils(db)
    manipulate_users = ManipulateUsers(db)

    tables_manager.create_tables()
    utils_object.create_table_chat_id()

    """ Bot core """
    # Commands /start and /help
    register_handlers(dp, user_client)
    create_bot_keyboard(dp)

    # Get chat_id
    chat_id = utils_object.get_chat_id()
    if chat_id:
        members = await get_all_members(user_client, chat_id)

        # Get all members and insert them into table
        for element in members:
            user_name, user_id = get_params_from_dict(element)
            manipulate_users.insert_user_to_table(user_id, user_name)

    else:
        print("No chat_id")

    """Shedule"""
    scheduler.start()

    # Start bot
    await dp.start_polling(bot)

    db.disconnect()
    print(db.get_connection_status())


if __name__ == "__main__":
    asyncio.run(main())
