import asyncio
import datetime
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


async def send_message_random():
    """Send a message to the chat"""

    # Get users from database
    manipulate_users = ManipulateUsers(db)
    manipulate_scores = ManipulateScores(db)

    # Get all groups
    all_groups_id = manipulate_users.get_all_groups()

    # Send message to every group
    for group_id in all_groups_id:

        # Get all users
        users_list = manipulate_users.get_all_users(group_id)

        if not users_list:
            print(f"No users in group {group_id}, skipping")
            continue

        try:
            # Determine random person id
            random_user_id = get_random(users_list)

            # Add insert to table score and user_id
            current_date = datetime.date.today()
            manipulate_scores.insert_scores(
                user_id=random_user_id, group_id=group_id, point=1, date=current_date
            )

            # Get user data
            user = await bot.get_chat(random_user_id)

            # Random phrase 
            fun_phrase = get_random(random_user_edition)

            await bot.send_message(
                chat_id=group_id, text=f"🏳️‍🌈{fun_phrase}\n\n<b>Пидорас дня</b> <span class=\"tg-spoiler\">{user.full_name}</span>", parse_mode="HTML"
            )

        except Exception as e:
            print(f"Error: {e}")


async def send_message_year_statistics():
    """Send all statistics"""

    score_statistics = ScoreStatistics(db)
    manipulate_users = ManipulateUsers(db)

    # Get all groups
    all_groups_id = manipulate_users.get_all_groups()

    # Send message to every group
    for group_id in all_groups_id:
        all_stat_list = score_statistics.get_year_statistics(group_id)

        try:
            # Lists for charts
            users_list = []
            scores_list = []

            ready_message = "*** С новым годом, пидорасы! ***\nСтатистика - топ 5 - за год подъехала\nИмя - очко\n\n"
            # Replace id with user's name
            for element in all_stat_list:
                user = await bot.get_chat(element[0])

                users_list.append(user.full_name)
                scores_list.append(element[1])

                print(users_list)
                print(scores_list)

                message_string = f"{user.username} - {element[1]}\n"
                ready_message += message_string
                print(ready_message)

            # Create chart
            chart_buffer = create_chart(users_list, scores_list)
            chart_bytes = chart_buffer.getvalue()

            await bot.send_photo(
                chat_id=group_id,
                photo=BufferedInputFile(chart_bytes, filename="statistics.png"),
                caption=ready_message,
            )

        except Exception as e:
            print(f"Error: {e}")


async def send_message_month_statistics():
    """Send month statistics"""
    
    score_statistics = ScoreStatistics(db)
    manipulate_users = ManipulateUsers(db)

    # Get all groups
    all_groups_id = manipulate_users.get_all_groups()

    # Send message to every group
    for group_id in all_groups_id:
        all_stat_list = score_statistics.get_month_statistics(group_id)

        try:
            # Lists for charts
            users_list = []
            scores_list = []

            ready_message = "*** Статистика за месяц, топ 5 ***\nИмя - очки\n\n"
            # Replace id with user's name
            for element in all_stat_list:
                user = await bot.get_chat(element[0])

                users_list.append(user.full_name)
                scores_list.append(element[1])

                print(users_list)
                print(scores_list)

                message_string = f"{user.username} - {element[1]}\n"
                ready_message += message_string
                print(ready_message)

            # Create chart
            chart_buffer = create_chart_month(users_list, scores_list)
            chart_bytes = chart_buffer.getvalue()

            await bot.send_photo(
                chat_id=group_id,
                photo=BufferedInputFile(chart_bytes, filename="statistics.png"),
                caption=ready_message,
            )

        except Exception as e:
            print(f"Error: {e}")
