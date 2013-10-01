"""
Script updates Tango Database by adding necessary entries in database.
Sample usage: python geosynoptic.py sys/tg_test/* -flag
With flags one can specify relevant information to access database.
    --host
    --port
    --user
    --passwd
    --db

Otherwise script will use default values (localhost:10000, user='root', passwd='', db='tango')
"""
import argparse
import MySQLdb as sql


parser = argparse.ArgumentParser(description='Sample usage: python geosynoptic.py sys/tg_test/*')
parser.add_argument("--host", default='localhost')
parser.add_argument("--port", type=int, default=10000)
parser.add_argument("--user", default='root')
parser.add_argument("--passwd", default='')
parser.add_argument("--db", default='tango')
args = parser.parse_args()

db = sql.connect(host=args.host, port=args.port, user=args.user, passwd=args.passwd, db=args.db)
cur = db.cursor()

device_list = []
cur.execute("SELECT name FROM device")
for row in cur.fetchall():
    device_list.append(row[0])
print device_list

properties = {'Device Name':'', 'Device Server': '', '_Location': '', '_Layer': '', '_Gui': '', '_Icon': ''}

for device in device_list:
    for prop in properties:
        query = "REPLACE INTO property_device (device, name, value) values ('%s', '%s', '%s')" % (device, prop, properties[prop])
        cur.execute(query)
