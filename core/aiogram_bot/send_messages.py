import asyncio
from core.sql_core.connect_to_host import db
from core.sql_core.sql_requests import ManipulateUsers, Utils
from core.utils.randomizer import get_random_user
from core.aiogram_bot.bot_connection import get_bot_and_dispatcher


async def send_message():
    """Send a message to the chat"""
    # Determine bot and dispetcher 
    bot, dp = get_bot_and_dispatcher()

    # Get users from database 
    utils_object = Utils(db)
    manipulate_object = ManipulateUsers(db)

    # Get all users
    users_list = manipulate_object.get_all_users()

    # Get chat_id from database
    my_chat_id = utils_object.get_chat_id()

    while True:
        try:
            # Determine random person id 
            random_user_id = get_random_user(users_list)[0]

            # Add insert to table score and user_id
            # ------ ======= ------

            print(random_user_id)
            user = await bot.get_chat(random_user_id)

            await bot.send_message(
                chat_id=my_chat_id,
                text=f"The ASS of the day is: {user.full_name}"
            )
            break

        except Exception as e:
            print(f'Error: {e}')

