import asyncio
import datetime
from aiogram import types
from aiogram.types import InputFile
from aiogram.types import BufferedInputFile
from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import ManipulateUsers, ManipulateScores
from core.sql_core.sql_statistics import ScoreStatistics
from core.utils.randomizer import get_random
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.chart_core.create_chart import create_chart, create_chart_month
from core.dictionaries.emojie_dict import emojie
from core.dictionaries.random_user_addition import random_user_edition

# Determine bot and dispetcher
bot, dp = get_bot_and_dispatcher()


async def send_message_all_statistics(group_id):
    """Send all statistics keyboard"""
    score_statistics = ScoreStatistics(db)

    all_stat_list = score_statistics.get_total_statistics(group_id)

    try:
        ready_message = "*** Статистика за всё время игры ***\nИмя - очки\n\n"

        for element in all_stat_list:
            user = await bot.get_chat(element[0])

            message_string = f"{user.username} - {element[1]}\n"
            ready_message += message_string
            print(ready_message)

        await bot.send_message(chat_id=group_id, text=ready_message)

    except Exception as e:
        print(f"Error: {e}")


async def send_message_all_users(group_id):
    """Send all users keyboard"""
    manihulate_users = ManipulateUsers(db)
    users_list = manihulate_users.get_all_users(group_id)

    try:
        ready_message = "*** Список всех игроков ***\n\n"

        for element in users_list:
            # Get random object
            random_emojie = get_random(emojie)

            user = await bot.get_chat(element)

            message_string = f"{user.username} {random_emojie}\n"
            ready_message += message_string

        await bot.send_message(chat_id=group_id, text=ready_message)

    except Exception as e:
        print(f"Error: {e}")
