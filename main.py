#!/usr/bin/env python2.7
from sys import exit
from pprint import pprint
from lib.mysql import MySQLConnection
import configargparse

def parse_args():
    parser = configargparse.ArgParser(default_config_files=['oscar.conf',])
    parser.add('-c',
               '--my-config',
               required=True,
               is_config_file=True,
               help='config file path')
    parser.add('-d',
               '--database',
               action='store',
               dest='database',
               help='MySQL database to use')
    parser.add('-H',
               '--host',
               action='store',
               dest='host',
               help='MySQL host to connect to')
    parser.add('-p',
               '--password',
               action='store',
               dest='password',
               help='MySQL password to use')
    parser.add('-u',
               '--user',
               action='store',
               dest='user',
               help='MySQL username to user')
    opts = parser.parse_args()
    return opts

def main():
    opts = parse_args()
    mysql = MySQLConnection(opts.host,
                            opts.user,
                            opts.password,
                            opts.database)
    conn = mysql.get_conn()
    sql = ("SELECT user_id, show_id, name, type, user_id, show_id, "
           "display_name, day, time, frequency FROM shows JOIN shows_users ON "
           "shows.id = shows_users.show_id JOIN users ON "
           "shows_users.user_id = users.id")
    results = mysql.query(sql, conn=conn)
    pprint(results)
    conn.close()
    return True


if __name__ == "__main__":
    # Change to BASH return codes:
    # 0   -> True
    # 1   -> False
    # > 1 -> That value
    val = main()
    if val == 'False' or val == '0':
        exit(1)
    elif val == 'True' or val == '1':
        exit(0)
    else:
        exit(int(val))
