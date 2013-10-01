import argparse
import re
import subprocess
import MySQLdb as sql
from geosynoptic import Geosynoptic

class GeosynopticSQL(Geosynoptic):
    def __init__(self, host='localhost', port=10000, user='root', passwd='', db='tango'):
        super(GeosynopticSQL, self).__init__(host, port, user, passwd, db)
        self.db = sql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        self.cur = self.db.cursor()

    def get_device_list(self, device_pattern):
        """
        Function retrieves devices to which device_pattern applies. Returns a list of devices

        :param host: database host
        :type  host: string
            
        :param port: database port
        :type  port: integer
        
        :param user: database user
        :type  user: string   
        
        :param passwd: database host
        :type  passwd: string

        :param device_pattern: server name pattern (* available)
        :type  device_pattern: string

        :return:    list of devices
        :rtype:     list of strings in format of x/y/z
        """
        self.cur.execute("SELECT name FROM device")

        dfm = device_pattern.split('/')
        dfm = ['.*' if ch is '*' else '^' + ch + '$' for ch in dfm]
    
        domain, family, member = dfm[0], dfm[1], dfm[2]
        device_list = []

        for row in self.cur.fetchall():
            device_name = row[0].split('/')
            if re.match(domain, device_name[0]) and re.match(family, device_name[1]) and re.match(member, device_name[2]):
                device = '%s/%s/%s' % (device_name[0], device_name[1], device_name[2])
                device_list.append(device)

        return device_list


    def get_device_properties(self, device_pattern, filter_properties):
        """
        Function retrieves properties of devices consistent with device_pattern

        :param device_pattern: server name pattern (* available)
        :type  device_pattern: string

        :param filter_properties: list of properties
        :type  filter_properties: list

        :return:    dictionary with devices as keys and list of tuples (property, value)
        :rtype:     dict
        """
        
        self.cur.execute("SELECT device, name, value FROM property_device WHERE device LIKE '%s'" % device_pattern.replace('*', '%'))
            
        device_properties = {}
        for row in self.cur.fetchall():
            device, prop, value = row[0], row[1], row[2]

            if device in device_properties and prop in filter_properties:
                device_properties[device].append((prop, value))
            else:
                device_properties[device] = []
        return device_properties
    

def trigger_taurus_form(device_list):
    cmd = ['taurusform']
    cmd.extend(device_list)
    cmd = ' '.join(cmd)
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sample usage: python geosynoptic.py sys/tg_test/*')
    parser.add_argument("device", help="name of the device")
    parser.add_argument("-d", default=False, action='store_true', help="triggers ATKPanel for device") 
    args = parser.parse_args()

    filter_properties = ['DeviceName', 'DeviceServer', 'Location', 'Layer', 'Icon', 'Gui']
    
    g = GeosynopticSQL()
    
    if args.d:
        device_list = g.get_device_list(args.device)
        if not device_list:
            print 'Device list is empty'
        elif len(device_list) > 1:
            c = raw_input('Warning, multiple (d) taurusforms will be trigged. Proceed? (y/n) ')
            if c.lower() == 'y':
                trigger_taurus_form(device_list)
            else:
                print 'Process interrupted.'
        else:
            trigger_taurus_form(device_list)
    else:
        device_properties = g.get_device_properties(args.device, filter_properties)
        for device in device_properties:
            print device
            for i in device_properties[device]:
                print '\t', i
    
