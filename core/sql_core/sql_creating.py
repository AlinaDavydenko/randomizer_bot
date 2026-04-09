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
                        user_id BIGINT, 
                        group_id BIGINT,
                        PRIMARY KEY (user_id, group_id)
                            );
                    """)
                
                #Create table scores 
                cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS scores (
                        user_id BIGINT,
                        group_id BIGINT,
                        point INTEGER NOT NULL CHECK (point > 0),
                        date DATE DEFAULT CURRENT_DATE
                            );
                """)

                self.db.conn.commit()

        except Exception as e:
            return f'Error {e}'