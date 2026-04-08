import asyncio
from core.sql_core.connect_to_host import db
from core.sql_core.sql_creating import CreateTables
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.scheduler.scheduler_jobs import scheduler
from core.logs_core.logger import setup_logger
from core.aiogram_bot.bot_commands import router
from core.aiogram_bot.list_commands import set_commands


async def main():
    """Logging"""
    # setup_logger()

    """ Connections """
    # Create bot connections
    bot, dp = get_bot_and_dispatcher()

    dp.include_router(router)

    # Create databese connection
    db.connect()

    print(db.get_connection_status())

    """ SQL core """
    # Create tables
    tables_manager = CreateTables(db)
    tables_manager.create_tables()

    """Shedule"""
    scheduler.start()

    # Start bot
    await set_commands(bot)
    await dp.start_polling(bot)

    db.disconnect()
    print(db.get_connection_status())


if __name__ == "__main__":
    asyncio.run(main())
