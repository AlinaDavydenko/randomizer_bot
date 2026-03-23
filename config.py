import os 
from dotenv import load_dotenv 

load_dotenv()

# SQL connection 
db_connection = {
    'host': os.getenv('DB_HOST'),       
    'port': os.getenv('DB_PORT'),        
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Telegram bot connection 
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')