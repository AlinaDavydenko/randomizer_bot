from core.aiogram_bot.send_messages import (
    send_message_random,
    send_message_year_statistics,
    send_message_month_statistics,
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

# Send messages
# scheduler.add_job(send_message_random, "cron", hour=9, minute=10, id="random_user")

# Send month statistics
# scheduler.add_job(
#     send_message_month_statistics,
#     "cron",
#     day=1,
#     hour=11,
#     minute=0,
#     id="month_statistics",
# )
# Send statistics
# scheduler.add_job(
#     send_message_year_statistics,
#     "cron",
#     month=1,
#     day=1,
#     hour=10,
#     minute=25,
#     id="year_statistics",
# )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

scheduler.add_job(send_message_random, "interval", seconds=30, id="random_user")

# scheduler.add_job(
#     send_message_month_statistics,
#     "interval",
#     seconds=30,
#     id="month_statistics",
# )

# scheduler.add_job(
#     send_message_year_statistics,
#     "interval",
#     seconds=30,
#     id="year_statistics",
# )
