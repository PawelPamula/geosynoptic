# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Aug 28 22:52:29 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

import shlex
import subprocess
import sys
sys.path.append('../../config/')
sys.path.append('../..')
sys.path.append('..')
from step1.step1 import Ui_Step1
from step2.step2 import Ui_Step2
from step3.step3 import Ui_Step3
from r492.main import Ui_MainWindow as GeosynapticWidget
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = QtGui.QMainWindow()
        self.setupUi(self.MainWindow)
        
        self.currentWidgetIndex = 0
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.step1 = Ui_Step1(None)
        self.step2 = Ui_Step2(None)
        self.step3 = Ui_Step3(None)
        self.stepList = [self.step1, self.step2, self.step3]

        self.stackedWidget.addWidget(self.step1)
        self.stackedWidget.addWidget(self.step2)
        self.stackedWidget.addWidget(self.step3)

        self.verticalLayout.addWidget(self.stackedWidget)

        ### QPushButton SIGNALS
        self.MainWindow.connect(self.nextButton, QtCore.SIGNAL('clicked()'), self.getNextWidget)
        self.MainWindow.connect(self.previousButton, QtCore.SIGNAL('clicked()'), self.getPreviousWidget)
        self.MainWindow.connect(self.nextButton, QtCore.SIGNAL('clicked()'), self.updateProgressBar)
        self.MainWindow.connect(self.previousButton, QtCore.SIGNAL('clicked()'), self.updateProgressBar)
        self.step1.configureButton.clicked.connect(self.nextButton.clicked)

        ### Signals from step1 widget
        self.MainWindow.connect(self.step1.testApplicationButton, QtCore.SIGNAL('clicked()'), self.triggerGeosynopticPanel)

        self.MainWindow.show()

    def triggerGeosynopticPanel(self):
        self.MainWindow.close()

        self.MainWindow = QtGui.QMainWindow()
        self.geosynapticpanel = GeosynapticWidget()
        self.geosynapticpanel.setupUi(self.MainWindow)
        self.MainWindow.show()
#        self.geosynapticpanel.show()

    def updateProgressBar(self):
        value = self.stackedWidget.currentIndex() * 100/(len(self.stackedWidget) - 1)
        self.progressBar.setValue(value)

    def getNextWidget(self):
            index = self.stackedWidget.currentIndex()
            if index + 1 < len(self.stepList):
                self.stackedWidget.setCurrentIndex(index+1)

    def getPreviousWidget(self):
            index = self.stackedWidget.currentIndex()
            if index - 1 >= 0:
                self.stackedWidget.setCurrentIndex(index-1)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(840, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 430, 621, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(130, 10, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.previousButton = QtGui.QPushButton(self.widget)
        self.previousButton.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.nextButton = QtGui.QPushButton(self.widget)
        self.nextButton.setGeometry(QtCore.QRect(500, 10, 111, 21))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 621, 411))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.widget_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 621, 411))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit_2.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())

