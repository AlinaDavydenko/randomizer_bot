from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from core.aiogram_bot.send_messages import send_message

scheduler = AsyncIOScheduler()

# Add jobs to scheduler
random_func = scheduler.add_job(
    send_message, "cron", hour=22, minute=2, id="random_user"
)
