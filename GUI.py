import PutingAllTogether
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys 


class Ui_MainWindow(QMainWindow,object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Yossi's Project")
        self.setWindowIcon(QIcon('D:\meet\Y2_Project\icon.png'))
        MainWindow.resize(305, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(60, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.Website = QtWidgets.QLineEdit(self.centralwidget)
        self.Website.setGeometry(QtCore.QRect(160, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Website.setFont(font)
        self.Website.setObjectName("Website")
        self.Topic = QtWidgets.QLineEdit(self.centralwidget)
        self.Topic.setGeometry(QtCore.QRect(30, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Topic.setFont(font)
        self.Topic.setObjectName("Topic")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.adjustSize
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 340, 281, 41))
        self.label2.setObjectName("label2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.b1.clicked.connect(self.Cliked)
        self.label2.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b1.setText(_translate("MainWindow", "Get resullts"))
        self.Website.setText(_translate("MainWindow", "website"))
        self.Topic.setText(_translate("MainWindow", "topic"))
        self.label.setText(_translate("MainWindow", "Please enter topic and website"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
    def Cliked(self):
        topic = self.Topic.text()
        website = self.Website.text()
        if(topic == "topic" or website == "website"):
            self.label2.setText("Don't leave it the same")
        else:
            self.label2.setText(PutingAllTogether.GetResults(topic,website))
        self.label2.adjustSize()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
