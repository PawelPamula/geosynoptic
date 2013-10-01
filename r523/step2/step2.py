from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Step2(QtGui.QWidget):
    def __init__(self, parent):
        super(Ui_Step2, self).__init__(parent)
        self.setupUi()
        self.layout = QtGui.QHBoxLayout() 
        self.label = QtGui.QLabel("Sample text")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def setupUi(self):
        self.resize(621, 411)
        self.setStyleSheet(_fromUtf8("border-image: url(background.jpeg)"))