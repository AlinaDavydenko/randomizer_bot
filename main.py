import asyncio
from core.sql_core.connect_to_host import db
from core.sql_core.sql_creating import CreateTables
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.aiogram_bot.bot_commands import register_handlers
from core.aiogram_bot.bot_keyboard import create_bot_keyboard
from core.scheduler.scheduler_jobs import scheduler
from core.logs_core.logger import setup_logger


async def main():
    """Logging"""
    # setup_logger()

    """ Connections """
    # Create bot connections
    bot, dp = get_bot_and_dispatcher()

    # Create databese connection
    db.connect()

    print(db.get_connection_status())

    """ SQL core """
    # Create tables
    tables_manager = CreateTables(db)
    tables_manager.create_tables()

    """ Bot core """
    # Commands /start and /help
    register_handlers(dp)
    create_bot_keyboard(dp)

    """Shedule"""
    scheduler.start()

    # Start bot
    await dp.start_polling(bot)

    db.disconnect()
    print(db.get_connection_status())


if __name__ == "__main__":
    asyncio.run(main())
