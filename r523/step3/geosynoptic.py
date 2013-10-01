from abc import ABCMeta, abstractmethod

class Geosynoptic(object):    
    __metaclass__ = ABCMeta

    def __init__(self, host='localhost', port=10000, user='root', passwd='', db='tango'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

    @abstractmethod
    def get_device_list(self, device_pattern):
        raise NotImplementedError("get_device_list() is not implemented")

    @abstractmethod
    def get_device_properties(self, device_pattern, filter_properties):
        raise NotImplementedError("get_device_properties() is not implemented")
