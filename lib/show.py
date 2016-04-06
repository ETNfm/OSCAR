from mysql import MySQLConnection

class RadioShow:
    def __init__(self, user_id, show_id, name, station, display_name,
                 day, time, frequency):
        self.user_id = user_id
        self.show_id = show_id
        self.name = name
        self.station = station
        self.display_name = display_name
        self.day = day
        self.time = time
        self.frequency = frequency

def build_show_list(mysql_conn):
    shows = []
    sql = ("SELECT user_id, show_id, name, type, display_name, day, time, "
           "frequency FROM shows JOIN shows_users ON "
           "shows.id = shows_users.show_id JOIN users ON "
           "shows_users.user_id = users.id")
    results = mysql_conn.query(sql)
    for result in results:
        shows.append(RadioShow(result['user_id'],
                               result['day'],
                               result['display_name'],
                               result['frequency'],
                               result['name'],
                               result['show_id'],
                               result['time'],
                               result['type']))
    return shows