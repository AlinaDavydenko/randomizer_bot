import psycopg2
from datetime import datetime


class ScoreStatisticsChart:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_all_statistics(self, group_id):
        """Get all statistics"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    select user_id, SUM(point) as sum_point, date from scores
                    WHERE group_id = %s
                    group by date, user_id
                    order by sum_point desc;
                    """, (group_id, ), 
                )

                rows = cur.fetchall()
                return rows

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []
