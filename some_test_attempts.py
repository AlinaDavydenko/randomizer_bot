from core.sql_core.sql_statistics import ScoreStatistics
from core.sql_core.connect_to_host import db

db.connect()
score_statistics = ScoreStatistics(db)
all_stat_list = score_statistics.get_all_statistics()

# print(all_stat_list)
db.disconnect()

# Get stat
for element in all_stat_list:
    print(f'{element[0]}, {element[1]}, {element[2]}')
