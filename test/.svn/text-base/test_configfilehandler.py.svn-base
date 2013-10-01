import sys
sys.path.append('..')
import unittest
import configfilehandler as cfh
from lxml import etree


class TestConfigFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler =  cfh.ConfigFileHandler('config.xml')

    def test_get_default_icon_path(self):
        result = self.file_handler.getDefaultIconPath()
        print result
        self.assertEquals(result, '../resource/icons/default.png')

if __name__ == '__main__':
    unittest.main()