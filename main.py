import asyncio
from core.sql_core.connect_to_host import DatabaseConnection
from core.sql_core.sql_creating import CreateTables
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.aiogram_bot.bot_commands import register_handlers, chat_id_storage
from core.aiogram_bot.bot_keyboard import create_bot_keyboard
# from core.pyrogram_core.start_session import app, sss
# from core.scheduler.daily_scan import daily_scan


async def main():
    """ Shedule """
    
    """ Connections """
    # Create bot connections
    bot, dp = get_bot_and_dispatcher()

    # Create databese connection
    db = DatabaseConnection()
    db.connect()

    print(db.get_connection_status())

    """ SQL core """
    # Create tables 
    tables_manager = CreateTables(db)
    result = tables_manager.create_tables()

    """ Bot core """
    # Commands /start and /help
    register_handlers(dp)
    create_bot_keyboard(dp)

    # Start bot
    await dp.start_polling(bot)

    # Get chat_id
    chat_id = chat_id_storage
    print(chat_id)

    db.disconnect()
    print(db.get_connection_status())


if __name__ == '__main__':
    asyncio.run(main())
