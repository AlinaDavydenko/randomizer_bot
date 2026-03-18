import asyncio
from core.sql_core.connect_to_host import DatabaseConnection
from core.sql_core.sql_creating import CreateTables
from core.aiogram_bot.bot_commands import start_command


def main():
    # Create connection 
    db = DatabaseConnection()
    db.connect()
    print(db.get_connection_status())

    tables_manager = CreateTables(db)
    result = tables_manager.create_tables()

    db.disconnect()
    print(db.get_connection_status())


if __name__ == '__main__':
    asyncio.run(start_command())
