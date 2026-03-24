import psycopg2
from datetime import datetime


class ManipulateUsers:
    def __init__(self, db_connection):
        self.db = db_connection

    def insert_user_to_table(self, tg_user_id, tg_user_name):
        """Insert one user into table user"""
        try:
            with self.db.conn.cursor() as cur:
                # User registration
                cur.execute(
                    """
                    INSERT INTO users (user_id, username)
                    VALUES (%s, %s);
                """,
                    (tg_user_id, tg_user_name),
                )

                self.db.conn.commit()

        except Exception as e:
            return f"Error {e}"

    def get_all_users(self):
        """Get all users from users table"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    SELECT username FROM users
                    ORDER BY username;
                """
                )

                rows = cur.fetchall()
                users_list = []
                for row in rows:
                    users_list.append(row)

                return users_list

        except Exception as e:
            return f"Error {e}"


class ManipulateScores:
    def __init__(self, db_connection):
        self.db = db_connection

    def insert_csores(self):
        pass

    def get_statistics(self):
        pass


class Utils:
    """Some extra requests"""

    def __init__(self, db_connection):
        self.db = db_connection

    def create_table_chat_id(self):
        try:
            with self.db.conn.cursor() as cur:
                # Create table users
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS chat_id (
                        chat_id BIGINT PRIMARY KEY
                            );
                    """
                )
                self.db.conn.commit()

        except Exception as e:
            return f"Error {e}"

    def insert_chat_id(self, id):
        try:
            with self.db.conn.cursor() as cur:
                # Create table users
                cur.execute(
                    """
                    INSERT INTO chat_id (chat_id)
                    VALUES (%s)
                    ON CONFLICT (chat_id) DO NOTHING;
                    """,
                    (id,),
                )
                self.db.conn.commit()
                print(f"[DEBUG] Successfully inserted chat_id: {id}")

        except Exception as e:
            print(f"[DEBUG] Error inserting chat_id: {e}")
            return f"Error {e}"

    def get_chat_id(self):
        """Get last id """
        try:
            with self.db.conn.cursor() as cur:
                # Create table users
                cur.execute(
                    """
                    SELECT chat_id FROM chat_id
                    ORDER BY chat_id DESC
                    LIMIT 1;
                    """
                )

                row = cur.fetchone()
                return row[0] if row else None 

        except Exception as e:
            print(f"[DEBUG] Error inserting chat_id: {e}")
            return f"Error {e}"



