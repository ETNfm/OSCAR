#!/usr/bin/env python2.7
from sys import exit
import configargparse
from lib.mysql import MySQLConnection
from lib.show import build_show_list
from lib.ftp import build_ftp_transfer_list
from lib.utilities import LevenshteinDistance, matcher

def parse_args():
    parser = configargparse.ArgParser(default_config_files=['oscar.conf',])
    parser.add('-c',
               '--my-config',
               required=True,
               is_config_file=True,
               help='config file path')
    parser.add('-b',
               '--back-database',
               action='store',
               dest='back_database',
               help='Back-end MySQL database to use')
    parser.add('-d',
               '--front-database',
               action='store',
               dest='front_database',
               help='Front-end MySQL database to use')
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

def build_directory_list(path):
    pass

def main():
    opts = parse_args()
    front_conn = MySQLConnection(opts.host,
                                 opts.user,
                                 opts.password,
                                 opts.front_database)
    back_conn = MySQLConnection(opts.host,
                                opts.user,
                                opts.password,
                                opts.back_database)

    show_list = build_show_list(front_conn)
    ftp_list = build_ftp_transfer_list(back_conn)
    directory_list = build_directory_list(opts.data_dir)

    for transfer in ftp_list:
        ftp_file = ' '.join(transfer.filename.split('/')[3:])
        highest = 0
        match = None
        for show in show_list:
            num_sets = matcher(show.display_name, ftp_file)
            num_sets += matcher(show.name, ftp_file)
            if num_sets >= highest:
                highest = num_sets
                match = show
        print("-----------------------------------------------------")
        print("FTP File: %s" % ftp_file)
        print("Artist: %s" % match.display_name)
        print("Show Name: %s" % match.name)
        print("Total Matches: %d" % highest)
        print("-----------------------------------------------------\n")
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
