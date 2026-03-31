import asyncio
from core.sql_core.connect_to_host import db
from core.sql_core.sql_creating import CreateTables
from core.sql_core.sql_requests import Utils, ManipulateUsers
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.aiogram_bot.bot_commands import register_handlers
from core.aiogram_bot.bot_keyboard import create_bot_keyboard
from core.aiogram_bot.send_messages import (
    send_message_random,
    send_message_year_statistics,
    send_message_month_statistics
)
from core.pyrogram_core.start_session import user_client
from core.pyrogram_core.scan_users import get_all_members
from core.utils.get_from_dictionary import get_params_from_dict
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

    """ Pyrogram client """
    # Create client for pyrogram
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

    """Shedule"""
    # Scan people
    scheduler.add_job(get_all_members, "cron", hour=9, minute=0, id="scan_users", args=[user_client])
    # Send messages
    scheduler.add_job(send_message_random, "cron", hour=9, minute=10, id="random_user")
    # Send month statistics 
    scheduler.add_job(send_message_month_statistics, "cron", day=1, hour=11, minute=0, id='month_statistics')
    # Send statistics
    scheduler.add_job(send_message_year_statistics, "cron", month=1, day=1, hour=10, minute=25, id="year_statistics")

    scheduler.start()

    # Start bot
    await dp.start_polling(bot)

    db.disconnect()
    print(db.get_connection_status())


if __name__ == "__main__":
    asyncio.run(main())
