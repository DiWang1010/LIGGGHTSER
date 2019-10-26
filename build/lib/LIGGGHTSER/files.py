# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt, QStringListModel
from PyQt5.QtGui import QTextCursor, QIcon
from LIGGGHTSER import read


class Files:
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
		self.verticalLayout_6.addWidget(self.tabWidget)

	def change_workdir(self,Mainwindow):
		dirname = QFileDialog.getExistingDirectory(Mainwindow,'open','./')
		if dirname:
			try:
				os.chdir(dirname)
			except:
				print('error:cannot change to this directory'+dirname)
		self.lineEdit.setPlaceholderText(str(os.getcwd()))

	def read_file(self,Marinwindow,file_read):
		self.clear_tab(0)
		try:
			filedict=file_read.read_file('./')
			title=list()
			for i in filedict:
				title.append(str(i))

			self.tablist = [QtWidgets.QWidget() for i in range(len(filedict))]
			self.listView = [QtWidgets.QListView() for i in range(len(filedict))]
			# self.qList=list()
			for i in range(len(filedict)):
				self.tablist[i].setObjectName(title[i])
				self.tabWidget.addTab(self.tablist[i], title[i])
				self.show_items(filedict,title[i],i)
			self.tabWidget.show()
		except:
			print('cannot read directory'+os.getcwd())
			return

	def show_items(self,filedict,title,number):
		layout=QVBoxLayout()
		self.listView[number] = QtWidgets.QListView()
		self.listView[number].setObjectName("listView"+str(number))
		slm=QStringListModel()
		self.qList=filedict[title]
		slm.setStringList(self.qList)
		self.listView[number].setModel(slm)
		self.listView[number].clicked.connect(self.read_data)
		layout.addWidget(self.listView[number])
		self.tablist[number].setLayout(layout)

	def clear_tab(self,index):
		try:
			for i in self.tablist:
				self.tabWidget.removeTab(index)
		except:
			print('Delete table fail')

	def read_data(self,qModelIndex):
		print(self.qList[qModelIndex.row()])