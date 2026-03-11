import os 
import sys 
import psycopg2
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import db_connection

class DatabaseConnection:
    """ Class for connection management"""
    def __init__(self):
        self.conn = None
        self.connected = False 

    def connect(self):
        """Connection to SQL database."""
        try:
            self.conn = psycopg2.connect(**db_connection)
            self.connected = True
            print('Connected to database')
            return self.conn 
        except Exception as e:
            self.conn = None   
            self.connected = False
            return f'Connection error: {e}'
    
    def disconnect(self):
        """Disconnection to SQL database."""
        if isinstance(self.conn, psycopg2.extensions.connection) and not self.conn.closed:
            self.conn.close()
            self.connected = False 
            return 'Connection is closed'
        
    def get_connection_status(self):
        """Check if connection is active"""
        if not isinstance(self.conn, psycopg2.extensions.connection):
            return 'No database connection object'
        elif self.conn.closed:
            return "Connection is closed"
        elif self.connected:
            return 'Connection is active'
        else:
            return 'Connection exists but flag is False'
