from core.sql_core.connect_to_host import DatabaseConnection

def main():
    pass

db = DatabaseConnection()

db.connect()
print(db.get_connection_status())

db.disconnect()
print(db.get_connection_status())
