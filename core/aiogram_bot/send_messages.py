import asyncio
import datetime
from aiogram.types import InputFile
from aiogram.types import BufferedInputFile
from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import ManipulateUsers, Utils, ManipulateScores
from core.sql_core.sql_statistics import ScoreStatistics
from core.utils.randomizer import get_random_user
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher
from core.chart_core.create_chart import create_chart

# Determine bot and dispetcher
bot, dp = get_bot_and_dispatcher()
utils_object = Utils(db)


async def send_message_random():
    """Send a message to the chat"""

    # Get users from database
    manipulate_object = ManipulateUsers(db)
    manipulate_scores = ManipulateScores(db)

    # Get all users
    users_list = manipulate_object.get_all_users()
    # Get chat_id from database
    my_chat_id = utils_object.get_chat_id()

    while True:
        try:
            # Determine random person id
            random_user_id = get_random_user(users_list)[0]

            # Add insert to table score and user_id
            current_date = datetime.date.today()
            manipulate_scores.insert_csores(
                user_id=random_user_id, point=1, date=current_date
            )

            print(random_user_id)
            user = await bot.get_chat(random_user_id)

            await bot.send_message(
                chat_id=my_chat_id, text=f"The ASS of the day is: {user.full_name}"
            )
            break

        except Exception as e:
            print(f"Error: {e}")


async def send_message_all_statistics():
    """Send all statistics"""

    score_statistics = ScoreStatistics(db)
    all_stat_list = score_statistics.get_all_statistics()

    # Get chat_id from database
    my_chat_id = utils_object.get_chat_id()

    try:
        # Lists for charts
        users_list = []
        scores_list = []

        ready_message = "*** Статистика за всё время ***\nИмя - очки\n\n"
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
            chat_id=my_chat_id,
            photo=BufferedInputFile(chart_bytes, filename="statistics.png"),
            caption=ready_message,
        )
        # await bot.send_message(chat_id=my_chat_id, text=ready_message)

    except Exception as e:
        print(f"Error: {e}")
