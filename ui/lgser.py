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
		self.file_sys=LIGGGHTSER.files.Files(self,LIGGGHTSER_ui)
		self.cal_sys=LIGGGHTSER.calculation.Calculation(self,LIGGGHTSER_ui,self.file_sys)
		self.variable_sys=LIGGGHTSER.variable.Variable(self,LIGGGHTSER_ui,self.file_sys)
		#############console system#############
		self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 450, 441, 221))
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
		QtCore.QMetaObject.connectSlotsByName(LIGGGHTSER_ui)

	def retranslateUi(self, LIGGGHTSER_ui):
		_translate = QtCore.QCoreApplication.translate
		LIGGGHTSER_ui.setWindowTitle(_translate("LIGGGHTSER_ui", "LIGGGHTSER"))
		# self.pushButton.setText(_translate("LIGGGHTSER_ui", "open"))
		
		self.menufile.setTitle(_translate("LIGGGHTSER_ui", "File"))
		self.menuedit.setTitle(_translate("LIGGGHTSER_ui", "Edit"))
		self.menufunction.setTitle(_translate("LIGGGHTSER_ui", "Function"))
		self.menuhelp.setTitle(_translate("LIGGGHTSER_ui", "Help"))
		self.actionnew.setText(_translate("LIGGGHTSER_ui", "New"))
		self.actionopen.setText(_translate("LIGGGHTSER_ui", "Open"))
		self.actionsave.setText(_translate("LIGGGHTSER_ui", "Save"))
		self.actionexit.setText(_translate("LIGGGHTSER_ui", "Exit"))
		self.actionprint.setText(_translate("LIGGGHTSER_ui", "Print"))
		self.actioncopy.setText(_translate("LIGGGHTSER_ui", "Copy"))
		self.actionpaste.setText(_translate("LIGGGHTSER_ui", "Paste"))
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
