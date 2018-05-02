from VARDB import connect_to_db
from VARDB.DbIO import DbIO
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create database tables')
    parser.add_argument('--dbuser', default='root')
    parser.add_argument('--dbpass', default='')
    parser.add_argument('--database', default='vardb')
    args = parser.parse_args()

    connect_to_db(database=args.database, user=args.dbuser, password=args.dbpass)

    DbIO().create_db()

    print "OK"
