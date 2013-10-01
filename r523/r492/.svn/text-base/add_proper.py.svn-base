#!usr/bin/python
import argparse
import re
import os
from PyTango import DeviceProxy
from taurus.core import TaurusManager

def get_device_list(device_pattern):
    """
    Function retrieves devices to which device_pattern applies. Returns a list of devices

    :param device_pattern:  device pattern in form a/b/c
    :type  device_pattern:  string

    :return:    list of devices
    :rtype:     list of strings in format of x/y/z
    """
    dfm = device_pattern.split('/')
    dfm = ['^.*$' if ch is '*' else '^' + ch + '$' for ch in dfm]

    device_list = []

    db = TaurusManager().getDatabase('localhost:10000')
    for domain in db.getDeviceDomainNames():
        for family in db.getDeviceFamilyNames(domain):
            for member in db.getDeviceMemberNames(domain, family):
                if re.match(dfm[0], domain) and re.match(dfm[1], family) and re.match(dfm[2], member):
                    device = '%s/%s/%s' % (domain, family, member)                
                    device_list.append(device)
    
    return device_list


def check_taurus_installation():
    """
    Checks installation of Taurus library. If taurus is found it returns path to the library

    :return: path to taurus installation
    :rtype:  String/None
    """
    try:
        import taurus
        return taurus.__file__
    except ImportError:
        return None


def get_device_icon(device_pattern, path=None):
    """
    Function searches for appropriate icon in specified folder and returns the list of the paths

    :param path:    path to root folder
    :type path:     string

    :param device_pattern:    device pattern in form a/b/c
    :type  device_pattern:    string

    :return paths:    dictionary {family: path_to_icon}
    :rtype paths:     dict
    """
    
    if not path:
        path = os.path.join(os.path.dirname(check_taurus_installation()), 'qt', 'qtgui', 'resource', 'tango-icons')

    devices = get_device_list(device_pattern)
    #print devices
    paths = {}
    for device in devices:
        family = device.split('/')[1]
        for root, dirs, files in os.walk(path):
#            print path
            for f in files:
                if family in f and device not in paths:
                    paths[device] = os.path.join(root, f)
#                else:
#                    print 'Nie znaleziono pliku w ' + path

        #jesli nie znajdziemy w sciezce path danej ikony, szukamy w aktualnym folderze w resources/
        if device not in paths:
            print 'Folder resources' 
            for root, dirs, files in os.walk('resource'):
                for f in files:
                    if family in f and device not in paths:
                            paths[device] = os.path.join(root, f)

        #jesli nie znajdziemy zadnej ikony -> wstawia defaultowa
        if device not in paths:
            print 'Ikona domyslna \n'
            paths[device] = 'resource/default.png'
    print paths
    return paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sample usage: python geosynoptic.py sys/tg_test/*')
    parser.add_argument("device", help="name of the device")
    parser.add_argument('-i', '--icon', help="Icon property") 
    parser.add_argument('-g', '--gui', help="GUI property") 
    parser.add_argument('-l', '--layer', help="Layer property") 
    parser.add_argument('-y', '--layout', help="Layout property")
    parser.add_argument('-c', default=False, action='store_true', help="check taurus installation")
    args = parser.parse_args()

    if not re.match(r".*/.*/.*", args.device):
        print 'Format nazwy urzadzenia niepoprawny'
    elif args.c:
        if check_taurus_installation():
            path_to_icons = find_device_icon(path, args.device)
            print path_to_icons        
    else:
        device_list = get_device_list(args.device)
        device_proxies = [DeviceProxy(dev) for dev in device_list]

        print device_proxies
        print args

        if args.icon:
            for dev_proxy in device_proxies:
                dev_proxy.put_property({'Icon': args.icon})
        
        if args.gui:
            for dev_proxy in device_proxies:
                dev_proxy.put_property({'Gui': args.gui})
        
        if args.layer:
            for dev_proxy in device_proxies:
                dev_proxy.put_property({'Layer': args.layer})
                
        if args.layout:
            for dev_proxy in device_proxies:
                dev_proxy.put_property({'Layout': args.layout})
