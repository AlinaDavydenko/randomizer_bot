import psycopg2
from datetime import datetime


class ScoreStatistics:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_total_statistics(self, group_id):
        """Get all statistics"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    select user_id, SUM(point) as sum_point from scores
                    where group_id = %s
                    group by user_id
                    order by sum_point desc;
                    """, (group_id, ), 
                )

                rows = cur.fetchall()

                return rows

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []

    def get_year_statistics(self, group_id):
        """Get all statistics"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    SELECT user_id, SUM(point) as sum_point FROM scores
                    WHERE group_id = %s and EXTRACT(YEAR FROM date) = EXTRACT(YEAR FROM CURRENT_DATE)
                    GROUP BY user_id
                    ORDER BY sum_point DESC
                    LIMIT 5;
                    """, (group_id, ), 
                )

                rows = cur.fetchall()

                return rows

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []
    
    def get_month_statistics(self, group_id):
        """ Get last month statistics """
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    SELECT user_id, SUM(point) as sum_point FROM scores
                    WHERE group_id = %s and date >= CURRENT_DATE - INTERVAL '1 month'
                    GROUP BY user_id
                    ORDER BY sum_point desc
                    limit 5;
                    """, (group_id, ), 
                )

                rows = cur.fetchall()

                return rows

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []
