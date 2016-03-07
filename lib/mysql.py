import MySQLdb as mdb

class MySQLConnection:
    def __init__(self, host, user, password, database='mysql'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None

    def get_conn(self):
        conn = None
        try:
            conn = mdb.connect(self.host,
                               self.user,
                               self.password,
                               self.database)
        except Exception as exc:
                print("ERROR: %s" % exc)
        finally:
            return conn

    def close(self):
        self.conn.close()

    def query(self, sql, conn=None, read_only=True, dict_cursor=True):
        result = None
        if not self.conn:
            conn = self.get_conn()
        try:
            if dict_cursor:
                cur = conn.cursor(cursorclass=mdb.cursors.DictCursor)
            else:
                cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            conn.close()
            self.conn = None
        except Exception as exc:
            print("Error %s" % (exc))
        finally:
            return result
