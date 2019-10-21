# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import time
# from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QMainWindow, QPushButton, QApplication, QTextEdit
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtGui import QTextCursor
import LIGGGHTSER

class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class Ui_MainWindow(object):
    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    def setupUi(self, MainWindow):
        lgs=LIGGGHTSER.read.Read('wd','0.1.0')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(370, 20, 391, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        ##########writle pushButton
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 90, 211, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.read_file(MainWindow,lgs))
        ##########writle textedit
        self.process = QTextEdit(MainWindow, readOnly=True)
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(500)
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.process.setGeometry(QtCore.QRect(30, 380, 731, 161))
        self.process.setObjectName("console")
        ###########################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
####################################################################################################
        self.change_wd = QtWidgets.QPushButton(self.centralwidget)
        self.change_wd.setGeometry(QtCore.QRect(90, 30, 211, 41))
        self.change_wd.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.change_workdir(MainWindow))
####################################################################################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        sys.stdout = Stream(newText=self.onUpdateText)

        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "Read File"))
        self.change_wd.setText(_translate("MainWindow", "Change work directory"))

    def read_file(self,Marinwindow,lgs):
        text, ok = QInputDialog.getText(Marinwindow,'Input Directory','Please Enter your Directory:')
        if ok:
            print('Reading files from',text)
            try:
                lgs.read_file(text)
            except:
                print('error:cannot read file')

    def change_workdir(self,Marinwindow,dirs):
        text, ok = QInputDialog.getText(Marinwindow,'Input Directory','Please Enter working Directory:')
        if ok:
            print('Reading files from',text)
            try:
                lgs.read_file(text)
            except:
                print('error:cannot read file')

    def test(self,text):
        print(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui.show()
    # ui.mainw()
    sys.exit(app.exec_())
