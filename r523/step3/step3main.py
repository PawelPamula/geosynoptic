# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')
import os
from config.configfilehandler import ConfigFileHandler
from geosynoptictango import GeosynopticTango
from step3 import Ui_Step3
from PyQt4 import QtCore, QtGui


class Step3Widget(QtGui.QWidget):
    def __init__(self, parent):
        super(Step3Widget, self).__init__()

        self.confighandler = ConfigFileHandler(configFilePath='config.xml')
        self.gtango = GeosynopticTango()

        self.resize(640, 480)
        self.layout = QtGui.QHBoxLayout()
        self.mainWidget = Ui_Step3(self)
        self.layout.addWidget(self.mainWidget)
        self.setLayout(self.layout)

        self.mainWidget.listWidget_3.setEnabled(False)
        self.mainWidget.pushButton_7.setEnabled(False)
        self.mainWidget.pushButton_8.setEnabled(False)
        self.show_devices_in_list_view()
        self.show_groups_in_combo()
        self.show_groups_with_icons()

        #Signals
        self.connect(self.mainWidget.pushButton, QtCore.SIGNAL('clicked()'), self.on_add_device_clicked)
        self.connect(self.mainWidget.pushButton_2, QtCore.SIGNAL('clicked()'), self.on_add_devices_clicked)
        self.connect(self.mainWidget.pushButton_4, QtCore.SIGNAL('clicked()'), self.on_remove_highlighted_device_clicked)
        self.connect(self.mainWidget.pushButton_3, QtCore.SIGNAL('clicked()'), self.on_add_group)
        self.connect(self.mainWidget.pushButton_5, QtCore.SIGNAL('clicked()'), self.on_clear_list_clicked)
        self.connect(self.mainWidget.pushButton_6, QtCore.SIGNAL('clicked()'), self.on_edit_group_clicked)

        self.show()

    def show_devices_in_list_view(self):
        """
        Prints available devices in listWidget
        """
        output = self.gtango.get_device_list('*/*/*')
        qStringOutput = [QtCore.QString(i) for i in output]
        self.mainWidget.listWidget.addItems(qStringOutput)

    def show_groups_in_combo(self):
        """
        Retrieves available groups from config.xml
        """
        self.mainWidget.comboBox.clear()
        groups = self.confighandler.getGroups()
        groups = [QtCore.QString(s) for s in groups]
        self.mainWidget.comboBox.addItems(groups)

    def show_groups_with_icons(self):
        """
        Displays availble groups with corresponding icon
        """
        self.mainWidget.listWidget_3.clear()
        groups = self.confighandler.getGroupsWithIcons()

        for i, j in groups:
            item = QtGui.QListWidgetItem(i)
            item.setIcon(QtGui.QIcon(j))
            self.mainWidget.listWidget_3.addItem(item)
       #print groups

    def on_add_group(self):
        inputter = InputDialog(self, 
                               title="Add Group of Devices", 
                               label="Name of the group", 
                               text="", 
                               buttonText='Add')
        inputter.exec_()
        self.confighandler.addGroup(str(inputter.text.text()), str(inputter.icon_path))
        self.show_groups_in_combo()
        self.show_groups_with_icons()

    def on_remove_highlighted_device_clicked(self):
        item = self.mainWidget.listWidget_2.takeItem(self.mainWidget.listWidget_2.currentRow())
        item = None

    def on_clear_list_clicked(self):
        while(self.mainWidget.listWidget_2.count()>0):
            self.mainWidget.listWidget_2.takeItem(0)

    def on_edit_group_clicked(self):
        inputter = InputDialog2(self, 
                                title="Change name of the group", 
                                label="Old name of the group", 
                                text="", 
                                label2="New name of the group",
                                text2="",
                                buttonText='Edit!')
        inputter.exec_()
        old_name = str(inputter.text.text())
        new_name = str(inputter.text2.text())
        new_path = str(inputter.icon_path)
        if old_name != '' and new_name != '':
            self.confighandler.editGroupName(old_name=old_name, new_name=new_name, new_path=new_path)
        self.show_groups_in_combo()
        self.show_groups_with_icons()

    def on_add_device_clicked(self):
        current_item = self.mainWidget.listWidget.currentItem()
        all_items = []
        for index in xrange(self.mainWidget.listWidget_2.count()):
            all_items.append(self.mainWidget.listWidget_2.item(index).text())


        print all_items
        if current_item and current_item.text() not in all_items:
            self.mainWidget.listWidget_2.addItem(QtCore.QString(current_item.text()))

    def on_add_devices_clicked(self):
        device_list = []
        group_name = str(self.mainWidget.comboBox.currentText())
        while(self.mainWidget.listWidget_2.count()>0):
            device_list.append(self.mainWidget.listWidget_2.takeItem(0))
        
        device_list = [str(d.text()) for d in device_list]

        #print device_list, group_name

        if group_name == '' or (not device_list):
            ret = QtGui.QMessageBox.warning(self,
                                            "Warning",
                                            '''Incorrect data''',
                                            QtGui.QMessageBox.Ok)

        else:
            flag = True
            for d in device_list:    
                result = self.confighandler.addDevice(device_name=d, group_name=group_name)
                if not result:
                    flag = result

            if not flag:
                ret = QtGui.QMessageBox.information(self,
                                                    "Info",
                                                    '''There were repeated devices in the group''',
                                                    QtGui.QMessageBox.Ok)


class InputDialog(QtGui.QDialog):
    '''
    this is for when you need to get some user input text
    '''
    def __init__(self, parent=None, title='', label='', text='', buttonText=''):
        QtGui.QWidget.__init__(self, parent)

        self.icon_path = ''

        #--Layout Stuff---------------------------#
        mainLayout = QtGui.QVBoxLayout()

        self.layout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel()
        self.label.setText(label)
        self.layout.addWidget(self.label)

        self.icon_label = QtGui.QLabel()
        self.icon_label.setText('Icon')

        self.browse_button = QtGui.QPushButton('Browse')        
        self.connect(self.browse_button, QtCore.SIGNAL("clicked()"), self.on_browse_clicked)

        self.text = QtGui.QLineEdit(text)
        self.layout.addWidget(self.text)

        mainLayout.addLayout(self.layout)

        self.layout = QtGui.QVBoxLayout()

        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.browse_button)

        self.button = QtGui.QPushButton(buttonText) #string or icon
        self.button.setEnabled(False)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.close)
        self.layout.addWidget(self.button)

        mainLayout.addLayout(self.layout)
        self.setLayout(mainLayout)

        self.resize(300, 100)
        self.setWindowTitle(title)

    def on_browse_clicked(self):
        self.icon_path = fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if self.icon_path != '':
            self.button.setEnabled(True)

class InputDialog2(InputDialog):
    def __init__(self, parent=None, title='', label='', text='', label2='', text2='', buttonText=''):
        QtGui.QWidget.__init__(self, parent)

        self.icon_path = ''

        #--Layout Stuff---------------------------#
        mainLayout = QtGui.QVBoxLayout()

        self.layout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel()
        self.label.setText(label)
        self.layout.addWidget(self.label)

        self.icon_label = QtGui.QLabel()
        self.icon_label.setText('Icon')

        self.browse_button = QtGui.QPushButton('Browse')        
        self.connect(self.browse_button, QtCore.SIGNAL("clicked()"), self.on_browse_clicked)

        self.text = QtGui.QLineEdit(text)
        self.layout.addWidget(self.text)

        self.label2 = QtGui.QLabel()
        self.label2.setText(label2)
        self.layout.addWidget(self.label2)

        self.text2 = QtGui.QLineEdit(text2)
        self.layout.addWidget(self.text2)

        mainLayout.addLayout(self.layout)

        self.layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton(buttonText) #string or icon
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.close)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.browse_button)

        mainLayout.addLayout(self.layout)
        self.setLayout(mainLayout)

        self.resize(300, 150)
        self.setWindowTitle(title)


    def on_browse_clicked(self):
        self.icon_path = fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

def main():
    app = QtGui.QApplication(sys.argv)
    w = Step3Widget(None)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


