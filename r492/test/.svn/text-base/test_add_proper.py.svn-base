import sys
sys.path.append("..")

import unittest
import add_proper


class TestAddProper(unittest.TestCase):
    pass


class TestGetDeviceList(TestAddProper):
    def test_get_device_list_indefinite_pattern(self):
        result = add_proper.get_device_list('*/*/*')
        self.assertTrue(len(result) > 1)

    def test_get_device_list_sys_domain(self):
        result = add_proper.get_device_list('sys/*/*')
        for r in result:
            self.assertTrue(r.startswith('sys'))

    def test_get_device_list_dserver_domain(self):
        result = add_proper.get_device_list('dserver/*/*')
        for r in result:
            self.assertTrue(r.startswith('dserver'))

    def test_get_device_list_tango_domain(self):
        result = add_proper.get_device_list('tango/*/*')
        for r in result:
            self.assertTrue(r.startswith('tango'))

    def test_get_device_list_tango_admin_family(self):
        result = add_proper.get_device_list('tango/admin/*')
        for r in result:
            self.assertTrue(r.startswith('tango/admin'))

    def test_get_device_list_non_existent_pattern(self):
        result = add_proper.get_device_list("xxx")
        self.assertEqual(len(result), 0)


class TestCheckTaurusInstallation(TestAddProper):
    def test_check(self):
        result = add_proper.check_taurus_installation()
        self.assertTrue(result is not None)

class TestGetDeviceIcon(TestAddProper):
    def test_check_sys_domain_default_path(self):
        result = add_proper.get_device_icon('sys/*/*')
        self.assertTrue(len(result) > 0)

    def test_check_sys_domain_wrong_path(self):
        #Musi sie pojawic ikona defaultowa
        result = add_proper.get_device_icon('sys/*/*', path='home')
        print result
        self.assertTrue('resource/default.png' in result.values())

if __name__ == '__main__':
    unittest.main()

