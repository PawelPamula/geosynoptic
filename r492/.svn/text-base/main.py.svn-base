# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created: Mon Aug 19 22:12:55 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

import os
import re
import functools
import PyTango
from PyQt4 import QtCore, QtGui
from PyTango import DeviceProxy, DevFailed
from resource import icon_rc
from geosynoptictango import GeosynopticTango
from add_proper import get_device_icon, get_device_list
from taurus.qt.qtgui.panel import TaurusForm


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.resize(747, 600)
        self.layout = QtGui.QHBoxLayout()

        self.setupUi()

        self.layout.addWidget(self.MainWindow)
        self.setLayout(self.layout)

    def setupUi(self):
        self.default_property_list = []

        self.MainWindow = QtGui.QMainWindow()

        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.MainWindow.resize(747, 600)
        self.MainWindow.setStyleSheet(_fromUtf8(""))

        self.device_list = []
        self.button_list = []

        self.centralwidget = QtGui.QWidget(self.MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 40, 730, 445))
        self.widget_2.setStyleSheet(_fromUtf8("""border-image: url(:/newPrefix/GeoSynapticPanel.png)url(:/newPrefix/GeoSynapticPanel.png)\n;"""))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))

        #self.widget = QtGui.QWidget(self.widget_2)
        #self.widget.setGeometry(QtCore.QRect(10, 40, 41, 441))
        #self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton = QtGui.QToolButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(15, 45, 41, 41))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 95 , 41, 41))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setStyleSheet( "background-color: transparent;" );
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 145, 41, 41))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(15, 195, 41, 41))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(15, 245, 41, 41))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(15, 295, 41, 41))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(15, 345, 41, 41))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(15, 395, 41, 41))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QToolButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(15, 445, 41, 41))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))

        self.button_list.append(self.pushButton)
        self.button_list.append(self.pushButton_2)
        self.button_list.append(self.pushButton_3)
        self.button_list.append(self.pushButton_4)
        self.button_list.append(self.pushButton_5)
        self.button_list.append(self.pushButton_6)
        self.button_list.append(self.pushButton_7)
        self.button_list.append(self.pushButton_8)
        self.button_list.append(self.pushButton_9)

        for button in self.button_list:
            button.setVisible(False)

        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 490, 731, 151))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))

        self.pos = [(0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2),
                    (3, 0), (3, 1), (3, 2)]

        self.grid = QtGui.QGridLayout()
        self.widget_3.setLayout(self.grid)

        self.lineEdit = QtGui.QLineEdit(QtCore.QString("*/*/*"), parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 365, 25))

        self.approveDevice = QtGui.QPushButton(QtCore.QString("choose a device"), parent=self.centralwidget)
        self.approveDevice.setGeometry(QtCore.QRect(375, 10, 365, 25))
        self.approveDevice.clicked.connect(self.update_icons)
        #self.add_devices_combobox()
        #combo box signal
        #self.comboBox.currentIndexChanged.connect(self.update_icons)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

    def validate_line_edit(self, pattern):
        """
        Function validates the pattern of the device. If pattern is different from x/y/z where
        x, y, z are strings, it returns false

        :param host: pattern
        :type  host: string

        :return:    whether pattern matches x/y/z
        :rtype:     boolean
        """
        if re.match(r".*/.*/.*", pattern):
            return True
        return False

    def update_icons(self):
        """
        Draws set of icons in the application based on pattern in self.lineEdit (QLineEdit).
        In case of improper/empty pattern it displays popup window
        In case of improper icon_path it raises Exception
        """

        for button in self.button_list:
            button.setVisible(False)

        #dictionary
        self.icon_path = get_device_icon(str(self.lineEdit.text()))

        if not self.icon_path:
            ret = QtGui.QMessageBox.warning(self.centralwidget,
                                            "Warning",
                                            '''Device not found''',
                                            QtGui.QMessageBox.Ok)

        for device in self.icon_path:
            image = QtGui.QIcon(QtCore.QString(self.icon_path[device]))
            #print self.icon_path[device]
            if image.isNull():
                raise Exception('Niepoprawna ikona')
            for button in self.button_list:
                if not button.isVisible():
                    #print device
                    button.clicked.connect(functools.partial(self.show_device_info, device))
                    button.setStyleSheet("background-color: transparent;")
                    button.setIcon(image)
                    button.setIconSize(QtCore.QSize(30, 30))
                    button.setToolTip(QtCore.QString(device))
                    button.setVisible(True)
                    break

    def show_device_info(self, device):
        """
        Displays basic device attribute properties (status, state, etc.). It creates
        QWidget with GridLayout.
        """
        #czyszczenie grida
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        t = DeviceProxy(device)

        try:
            attr_list = t.get_attribute_list()

            i = 0

            attr_device = [t.read_attribute(j) for j in attr_list]
            attr_device = [x for x in attr_device if x.data_format == PyTango._PyTango.AttrDataFormat.SCALAR]

            for p in self.pos:
                if not attr_device:
                    break
                else:
                    name = attr_device[0].name
                    value = attr_device[0].value
                    del attr_device[0]
                    l = QtGui.QLabel("%s : %s" % (name, value))
                    l.setAlignment(QtCore.Qt.AlignCenter)
                    self.grid.addWidget(l, p[0], p[1])

        except DevFailed:
            ret = QtGui.QMessageBox.warning(self.centralwidget,
                                            "Warning",
                                            '''Retrieving attribute list failed''',
                                            QtGui.QMessageBox.Ok)

"""
                name = str(attr_device.name)
                value = str(attr_device.value)
                l = QtGui.QLabel("%s : %s" % (name, value))
                l.setAlignment(QtCore.Qt.AlignCenter)
                self.grid.addWidget(l, i[0], i[1])
"""

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = Ui_MainWindow()
    widget.show()
    sys.exit(app.exec_())
