import sys
sys.path.append("..")

import unittest
from geosynopticsql import GeosynopticSQL


class TestGeosynopticSQL(unittest.TestCase):
    def setUp(self):
        self.g = GeosynopticSQL()


class TestGetDeviceList(TestGeosynopticSQL):
    def test_get_device_list_all(self):
        result = self.g.get_device_list('*/*/*')
        self.assertTrue(len(result) > 0)

    def test_get_device_list_sys_domain(self):
        result = self.g.get_device_list('sys/*/*')
        self.assertTrue(len(result) > 0)

    def test_get_device_list_dserver_domain(self):
        result = self.g.get_device_list('dserver/*/*')
        self.assertTrue(len(result) > 0)

    def test_get_device_list_tango_domain(self):
        result = self.g.get_device_list('tango/*/*')
        self.assertTrue(len(result) > 0)

    def test_get_device_list_non_existent(self):
        result = self.g.get_device_list('qqqqqqq/qqqqqqq/qqqqqqq')
        self.assertTrue(len(result) == 0)


class TestGetDeviceProperties(TestGeosynopticSQL):
    def test_get_device_properties_with_no_filter(self):
        result = self.g.get_device_properties('*/*/*', [])
        self.assertEqual(all([len(i) for i in result.values()]), 0)

    def test_get_device_properties_with_non_existent_property(self):
        result = self.g.get_device_properties('*/*/*', ['non-existent property'])
        self.assertEqual(all([len(i) for i in result.values()]), 0)


if __name__ == '__main__':
    unittest.main()
