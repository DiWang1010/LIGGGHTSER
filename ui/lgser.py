# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lgser.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import time
import os
# from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QInputDialog,QMainWindow, QPushButton, QApplication, QTextEdit,QFormLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt
from PyQt5.QtGui import QTextCursor, QIcon
import LIGGGHTSER

class Stream(QObject):
	"""Redirects console output to text widget."""
	newText = pyqtSignal(str)

	def write(self, text):
		self.newText.emit(str(text))

class Ui_LIGGGHTSER_ui(object):
	def setupUi(self, LIGGGHTSER_ui):
		LIGGGHTSER_ui.setObjectName("LIGGGHTSER_ui")
		LIGGGHTSER_ui.resize(1024, 720)
		LIGGGHTSER_ui.setMinimumSize(QtCore.QSize(1024, 720))
		LIGGGHTSER_ui.setMouseTracking(False)
		LIGGGHTSER_ui.setWindowIcon(QIcon('LIGGGHTSER.ico'))
		self.centralwidget = QtWidgets.QWidget(LIGGGHTSER_ui)
		self.centralwidget.setObjectName("centralwidget")
		LIGGGHTSER_ui.setCentralWidget(self.centralwidget)
		#############file system#############
		file_sys=LIGGGHTSER.files.Files(self,LIGGGHTSER_ui)
		#############console system#############
		self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 450, 441, 221))
		self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
		self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
		self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.process = QtWidgets.QTextEdit(self.verticalLayoutWidget_7, readOnly=True)
		self.process.ensureCursorVisible()
		self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
		self.process.setObjectName("console")
		self.process.setLineWrapColumnOrWidth(400)
		self.verticalLayout_7.addWidget(self.process)
		sys.stdout = Stream(newText=self.onUpdateText)
		
		# print(file_sys.filedict)





		self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 30, 471, 411))
		self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)
		self.verticalLayout_2.addWidget(self.tableWidget)

		self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(700, 0, 311, 231))
		self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget_3)
		self.graphicsView.setObjectName("graphicsView")
		self.verticalLayout_3.addWidget(self.graphicsView)

		



		self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(700, 240, 311, 201))
		self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
		self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_6.setObjectName("verticalLayout_6")

		

		self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(450, 450, 561, 221))
		self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
		self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_8)
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")
		self.verticalLayout_8.addWidget(self.tabWidget)
		
		self.menubar = QtWidgets.QMenuBar(LIGGGHTSER_ui)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
		self.menubar.setObjectName("menubar")
		self.menufile = QtWidgets.QMenu(self.menubar)
		self.menufile.setObjectName("menufile")
		self.menuedit = QtWidgets.QMenu(self.menubar)
		self.menuedit.setObjectName("menuedit")
		self.menufunction = QtWidgets.QMenu(self.menubar)
		self.menufunction.setObjectName("menufunction")
		self.menuhelp = QtWidgets.QMenu(self.menubar)
		self.menuhelp.setObjectName("menuhelp")
		LIGGGHTSER_ui.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(LIGGGHTSER_ui)
		self.statusbar.setObjectName("statusbar")
		LIGGGHTSER_ui.setStatusBar(self.statusbar)
		self.actionnew = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionnew.setObjectName("actionnew")
		self.actionopen = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionopen.setObjectName("actionopen")
		self.actionsave = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionsave.setObjectName("actionsave")
		self.actionexit = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionexit.setObjectName("actionexit")
		self.actionprint = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionprint.setObjectName("actionprint")
		self.actioncopy = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actioncopy.setObjectName("actioncopy")
		self.actionpaste = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionpaste.setObjectName("actionpaste")
		self.actionFriction = QtWidgets.QAction(LIGGGHTSER_ui)
		self.actionFriction.setObjectName("actionFriction")
		self.menufile.addAction(self.actionnew)
		self.menufile.addAction(self.actionopen)
		self.menufile.addAction(self.actionsave)
		self.menufile.addSeparator()
		self.menufile.addAction(self.actionprint)
		self.menufile.addAction(self.actionexit)
		self.menuedit.addAction(self.actioncopy)
		self.menuedit.addAction(self.actionpaste)
		self.menufunction.addAction(self.actionFriction)
		self.menubar.addAction(self.menufile.menuAction())
		self.menubar.addAction(self.menuedit.menuAction())
		self.menubar.addAction(self.menufunction.menuAction())
		self.menubar.addAction(self.menuhelp.menuAction())

		self.retranslateUi(LIGGGHTSER_ui)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(LIGGGHTSER_ui)

	def retranslateUi(self, LIGGGHTSER_ui):
		_translate = QtCore.QCoreApplication.translate
		LIGGGHTSER_ui.setWindowTitle(_translate("LIGGGHTSER_ui", "LIGGGHTSER"))
		# self.pushButton.setText(_translate("LIGGGHTSER_ui", "open"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("LIGGGHTSER_ui", "Friction"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("LIGGGHTSER_ui", "Tab 2"))
		self.menufile.setTitle(_translate("LIGGGHTSER_ui", "file"))
		self.menuedit.setTitle(_translate("LIGGGHTSER_ui", "edit"))
		self.menufunction.setTitle(_translate("LIGGGHTSER_ui", "function"))
		self.menuhelp.setTitle(_translate("LIGGGHTSER_ui", "help"))
		self.actionnew.setText(_translate("LIGGGHTSER_ui", "new"))
		self.actionopen.setText(_translate("LIGGGHTSER_ui", "open"))
		self.actionsave.setText(_translate("LIGGGHTSER_ui", "save"))
		self.actionexit.setText(_translate("LIGGGHTSER_ui", "exit"))
		self.actionprint.setText(_translate("LIGGGHTSER_ui", "print"))
		self.actioncopy.setText(_translate("LIGGGHTSER_ui", "copy"))
		self.actionpaste.setText(_translate("LIGGGHTSER_ui", "paste"))
		self.actionFriction.setText(_translate("LIGGGHTSER_ui", "Friction"))

	def onUpdateText(self, text):
		"""Write console output to text widget."""
		cursor = self.process.textCursor()
		cursor.movePosition(QTextCursor.End)
		cursor.insertText(text)
		self.process.setTextCursor(cursor)
		self.process.ensureCursorVisible()

class mainwin(QtWidgets.QMainWindow):
	def closeEvent(self, event):
	#Shuts down application on close.
	# Return stdout to defaults.
		reply = QMessageBox.question(LIGGGHTSER_ui, 'WARNING', 'Do you want to exit', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			sys.stdout = sys.__stdout__
			super().closeEvent(event)
			event.accept()		
		else:
			event.ignore()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	LIGGGHTSER_ui = mainwin()
	# MainWindow = QtWidgets.QMainWindow()
	ui = Ui_LIGGGHTSER_ui()
	ui.setupUi(LIGGGHTSER_ui)
	LIGGGHTSER_ui.show()
	# ui.show()
	# ui.mainw()
	sys.exit(app.exec_())
