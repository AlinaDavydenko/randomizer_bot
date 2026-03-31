import psycopg2
from datetime import datetime


class ScoreStatistics:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_all_statistics(self):
        """Get all statistics"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    select user_id, SUM(point) as sum_point from scores
                    group by user_id
                    order by sum_point desc;
                    """
                )

                rows = cur.fetchall()
                all_stat_list = []
                for row in rows:
                    all_stat_list.append(row)

                return all_stat_list

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []

    def get_year_statistics(self):
        """Get all statistics"""
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    SELECT user_id, SUM(point) as sum_point FROM scores
                    WHERE EXTRACT(YEAR FROM date) = EXTRACT(YEAR FROM CURRENT_DATE)
                    GROUP BY user_id
                    ORDER BY sum_point DESC
                    LIMIT 5;
                    """
                )

                rows = cur.fetchall()
                all_stat_list = []
                for row in rows:
                    all_stat_list.append(row)

                return all_stat_list

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []
    
    def get_month_statistics(self):
        """ Get last month statistics """
        try:
            with self.db.conn.cursor() as cur:
                # Getting users
                cur.execute(
                    """
                    SELECT user_id, SUM(point) as sum_point FROM scores
                    WHERE date >= CURRENT_DATE - INTERVAL '1 month'
                    GROUP BY user_id
                    ORDER BY sum_point desc
                    limit 5;
                    """
                )

                rows = cur.fetchall()
                all_stat_list = []
                for row in rows:
                    all_stat_list.append(row)

                return all_stat_list

        except Exception as e:
            print(f"Error get_all_users: {e}")
            return []