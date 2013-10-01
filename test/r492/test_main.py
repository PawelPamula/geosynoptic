# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

import unittest
import main


class TestMain(unittest.Testcase):
    pass


class TestValidateLineEdit(TestMain):
    def setUp(self):
        self.widget = main.Ui_MainWindow()

    def test_empty_line(self):
        line = ''
        self.assertFalse(self.widget.validate_line_edit(line))

    def test_incorrect_line(self):
        line = 'aaa'
        self.assertFalse(self.widget.validate_line_edit(line))

    def test_correct_line(self):
        line = 'a/b/c'
        self.assertFalse(self.widget.validate_line_edit(line))
