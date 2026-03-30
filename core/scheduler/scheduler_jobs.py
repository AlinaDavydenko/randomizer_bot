from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from core.aiogram_bot.send_messages import (
    send_message_random,
    send_message_all_statistics,
)

scheduler = AsyncIOScheduler()

""" Add jobs to scheduler """

# Scan people


# Send messages
random_func = scheduler.add_job(
    send_message_random, "cron", hour=9, minute=10, id="random_user"
)

# Send statistics
all_statistics = scheduler.add_job(
    send_message_all_statistics,
    "cron",
    month=1,
    day=1,
    hour=9,
    minute=0,
    id="all_statistics",
)

# test
# all_statistics = scheduler.add_job(
#     send_message_all_statistics,
#     "cron",
#     month=3,
#     day=30,
#     hour=23,
#     minute=28,
#     id="all_statistics",
# )
