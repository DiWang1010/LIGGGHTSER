# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt, QStringListModel
from PyQt5.QtGui import QTextCursor, QIcon
from LIGGGHTSER import read


class Files(object):
	def __init__(self,lgser,Mainwindow):
		file_read = read.Read()
		self.filedict=dict()
		self.verticalLayoutWidget = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 620, 21))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName("lineEdit")
		self.verticalLayout.addWidget(self.lineEdit)
		self.lineEdit.setPlaceholderText(str(os.getcwd()))
		#button1
		self.verticalLayoutWidget_4 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(640, 0, 21, 21))
		self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(lambda:self.change_workdir(Mainwindow))
		#button2
		self.verticalLayoutWidget_5 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(670, 0, 21, 21))
		self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
		self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.pushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.pushButton2.setObjectName("pushButton2")
		self.pushButton2.clicked.connect(lambda:self.read_file(Mainwindow,file_read))
		#############filelist system#############
		self.verticalLayoutWidget_6 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 30, 190, 410))
		self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
		self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_6)
		self.tabWidget.setTabPosition(QTabWidget.West)
		self.tabWidget.setObjectName("tabWidget")
		# self.listView = QtWidgets.QListView(self.verticalLayoutWidget_6)
		# self.listView.setObjectName("listView")
		self.verticalLayout_6.addWidget(self.tabWidget)
		# self.beginInsertRows(QModelIndex(),2,4)

	def change_workdir(self,Mainwindow):
		dirname = QFileDialog.getExistingDirectory(Mainwindow,'open','./')
		if dirname:
			try:
				os.chdir(dirname)
			except:
				print('error:cannot change to this directory'+dirname)
		self.lineEdit.setPlaceholderText(str(os.getcwd()))

	def read_file(self,Marinwindow,file_read):
		# try:
		filedict=file_read.read_file('./')
		title=list()
		for i in filedict:
			title.append(str(i))

		self.tablist = [QtWidgets.QWidget() for i in range(len(filedict))]
		for i in range(len(filedict)):
			self.tablist[i].setObjectName(title[i])
			self.tabWidget.addTab(self.tablist[i], title[i])

			self.show_items(filedict,title[i],i)
		self.tabWidget.show()
		# except:
		# 	print('cannot read directory'+os.getcwd())
		# 	return

	def show_items(self,filedict,title,number):
		layout=QVBoxLayout()
		listView = QtWidgets.QListView()
		listView.setObjectName("listView")
		slm=QStringListModel()
		self.qList=filedict[title]
		slm.setStringList(self.qList)
		listView.setModel(slm)
		# listView.clicked.connect()
		layout.addWidget(listView)
		self.tablist[number].setLayout(layout)

