import psycopg2

class CreateTables:
    """Class for user's score manage"""

    def __init__(self, db_connection):
        self.db = db_connection 

    def create_tables(self):
        """Create tables USERS and SCORES"""
        try:
            with self.db.conn.cursor() as cur:
                # Create table users 
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY, 
                        username VARCHAR(50) NOT NULL
                            );
                    """)
                
                #Create table scores 
                cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,  
                        point INTEGER NOT NULL CHECK (point > 0),
                        date DATE DEFAULT CURRENT_DATE
                            );
                """)

                self.db.conn.commit()

        except Exception as e:
            return f'Error {e}'