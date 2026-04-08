from aiogram.types import BotCommand

async def set_commands(bot):
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="register", description="Registration"),
        BotCommand(command="all_statistics", description="Show all statistics"),
        BotCommand(command="all_users", description="Show all users")
    ]
    await bot.set_my_commands(commands)
