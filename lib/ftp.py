from mysql import MySQLConnection

class FTPFile:
    def __init__(self,
                 id,
                 username,
                 filename,
                 size,
                 host,
                 ip,
                 action,
                 duration,
                 localtime,
                 success):
        self.id = id
        self.username = username
        self.filename = filename
        self.size = size
        self.host = host
        self.ip = ip
        self.action = action
        self.duration = duration
        self.localtime = localtime
        self.success = success


def build_ftp_transfer_list(mysql_conn):
    transfers = []
    sql = ("SELECT * FROM ftpxferlog")
           #"" WHERE ftpxferlog.localtime "
           #">= timestamp(NOW() - INTERVAL 90 DAY);")
    results = mysql_conn.query(sql)
    print results
    for result in results:
        transfers.append(FTPFile(result['id'],
                                 result['username'],
                                 result['filename'],
                                 result['size'],
                                 result['host'],
                                 result['ip'],
                                 result['action'],
                                 result['duration'],
                                 result['localtime'],
                                 result['success']))
    return transfers