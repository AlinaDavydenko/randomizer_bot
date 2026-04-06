import psycopg2
from datetime import datetime


class ManipulateUsers:
    def __init__(self, db_connection):
        self.db = db_connection

    def insert_user_to_table(self, tg_user_id, tg_group_id):
        """Insert one user into table user"""
        try:
            with self.db.conn.cursor() as cur:
                # User registration
                cur.execute(
                    """
                    INSERT INTO users (user_id, group_id)
                    VALUES (%s, %s)
                    ON CONFLICT (user_id, group_id) DO NOTHING;
                """,
                    (tg_user_id, tg_group_id),
                )

                self.db.conn.commit()

        except Exception as e:
            return f"Error {e}"

    def get_all_users(self, tg_group_id):
        """Get all users from users table"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    SELECT user_id FROM users
                    WHERE group_id = %s;
                """, (tg_group_id,), 
                )

                rows = cur.fetchall()
                return [row[0] for row in rows]

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return [] 


class ManipulateScores:
    def __init__(self, db_connection):
        self.db = db_connection

    def insert_scores(self, user_id, group_id, point, date):
        try:
            with self.db.conn.cursor() as cur:
                # User registration
                cur.execute(
                    """
                    INSERT INTO scores (user_id, group_id, point, date)
                    VALUES (%s, %s, %s, %s), 
                    ON CONFLICT (user_id, group_id, date) DO NOTHING;
                """,
                    (user_id, group_id, point, date),
                )

                self.db.conn.commit()

        except Exception as e:
            self.db.conn.rollback()
            return f"Error {e}"
