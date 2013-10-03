# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step3.ui'
#
# Created: Sun Sep 29 23:13:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Step3(QtGui.QWidget):
    def __init__(self, parent):
        super(Ui_Step3, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName(_fromUtf8("Step3"))
        self.resize(621, 411)
        self.setMinimumSize(QtCore.QSize(621, 411))
        self.setMaximumSize(QtCore.QSize(621, 411))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 160, 31, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 171, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 359))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 171, 361))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(230, 10, 171, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(230, 40, 171, 281))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.listWidget_2 = QtGui.QListWidget(self.widget)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 171, 281))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 330, 171, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(480, 10, 71, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 250, 171, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.widget_2 = QtGui.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(440, 40, 171, 201))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.listWidget_3 = QtGui.QListWidget(self.widget_2)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 171, 201))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))

        self.listWidget.setStyleSheet("""QListWidget:item:selected:active {
                                            background: blue;
                                         }
                                         QListWidget:item:selected:!active {
                                            background: gray;
                                         }
                                         QListWidget:item:selected:disabled {
                                            background: gray;
                                         }
                                         QListWidget:item:selected:!disabled {
                                            background: blue;
                                         }
                                       """
                                     )

        self.listWidget_2.setStyleSheet("""QListWidget:item:selected:active {
                                            background: blue;
                                         }
                                         QListWidget:item:selected:!active {
                                            background: gray;
                                         }
                                         QListWidget:item:selected:disabled {
                                            background: gray;
                                         }
                                         QListWidget:item:selected:!disabled {
                                            background: blue;
                                         }
                                       """
                                     )

        self.listWidget_3.setStyleSheet("""QListWidget:item:selected:active {
                                            background: blue;
                                         }
                                         QListWidget:item:selected:!active {
                                            background: white;
                                         }
                                         QListWidget:item:selected:disabled {
                                            background: white;
                                         }
                                         QListWidget:item:selected:!disabled {
                                            background: blue;
                                         }
                                       """
                                     )

        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 200, 31, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 370, 171, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 290, 171, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 330, 171, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 370, 171, 31))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Step3", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Step3", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Step3", "Add devices", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Step3", "Group list", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Step3", "Add group", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Step3", "Available devices", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Step3", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Step3", "Clear list", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Step3", "Edit group", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Step3", "Delete icon", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Step3", "Change icon", None, QtGui.QApplication.UnicodeUTF8))

