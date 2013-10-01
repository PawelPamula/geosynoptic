import re
from geosynoptic import Geosynoptic
from PyTango import DeviceProxy
from taurus.core import TaurusManager


class GeosynopticTango(Geosynoptic):
    def __init__(self, host='localhost', port=10000, user='root', passwd='', db='tango'):
        super(GeosynopticTango, self).__init__(host, port, user, passwd, db)

    def get_device_list(self, device_pattern):
        """
        Function retrieves devices to which device_pattern applies. Returns a list of devices

        :param host: database host
        :type  host: string
        
        :param device_pattern: server name pattern (* available)
        :type  device_pattern: string

        :return:    list of devices
        :rtype:     list of strings in format of x/y/z
        """
        
        dbhost = '%s:%d' % (self.host, self.port)
        db = TaurusManager().getDatabase(dbhost)

        dfm = device_pattern.split('/')
        dfm = ['.*' if ch is '*' else '^' + ch + '$' for ch in dfm]
        
        domain, family, member = dfm[0], dfm[1], dfm[2]
        domains = db.getDeviceDomainNames()
        device_list = []
        
        for i in domains:
            families = db.getDeviceFamilyNames(i)
            for j in families:
                members = db.getDeviceMemberNames(i, j)
                for k in members:
                    print i, j, k
                    if re.match(domain, i) and re.match(family, j) and re.match(member, k):
                        device = '%s/%s/%s' % (i, j, k)
                        device_list.append(device)
        return device_list


    def get_device_properties(self, device_pattern):
        """
        Function retrieves properties of devices consistent with device_pattern

        :param device_pattern: server name pattern (* available)
        :type  device_pattern: string

        :return:    dictionary with devices as keys and lists of properties as values
        :rtype:     dict
        """
        device_properties = {}
        device_list = self.get_device_list(device_pattern)
        for device in device_list:
            device_proxy = DeviceProxy(device)
            
            properties_list = []
            for d in device_proxy.get_property_list('*'):
                x = device_proxy.get_property(d)
                properties_list.extend(x.items())
            if device not in device_properties:
                device_properties[device] = properties_list
        
        return device_properties    


if __name__ == '__main__':
    g = GeosynopticTango()
    print g.get_device_properties("tango/admin/*")