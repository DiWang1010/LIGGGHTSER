#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt, QStringListModel
from PyQt5.QtGui import QTextCursor, QIcon
from LIGGGHTSER import read


class Files:
	def __init__(self,lgser,Mainwindow):
		self.lg=lgser
		file_read = read.Read()
		self.file_data = list()
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
		#button_dir
		# self.verticalLayoutWidget_4 = QtWidgets.QWidget(lgser.centralwidget)
		# self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(640, 0, 21, 21))
		# self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
		# self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
		# self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		# self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.pushButton = QtWidgets.QPushButton(lgser.centralwidget)
		self.pushButton.setGeometry(640, 0, 21, 21)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setIcon(QIcon("open.png")) 
		self.pushButton.setFlat(True)
		self.pushButton.clicked.connect(lambda:self.change_workdir(Mainwindow))
		#button_readfile
		# self.verticalLayoutWidget_5 = QtWidgets.QWidget(lgser.centralwidget)
		# self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(670, 0, 21, 21))
		# self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
		# self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
		# self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
		# self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.pushButton2 = QtWidgets.QPushButton(lgser.centralwidget)
		self.pushButton2.setGeometry(670, 0, 21, 21)
		self.pushButton2.setObjectName("pushButton2")
		self.pushButton2.setIcon(QIcon("preview.png")) 
		self.pushButton2.setFlat(True)
		self.pushButton2.clicked.connect(lambda:self.read_file(Mainwindow,file_read))
		#button3_readdata
		# self.verticalLayoutWidget_9 = QtWidgets.QWidget(lgser.centralwidget)
		# self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 30, 190, 130))
		# self.verticalLayoutWidget_9.setMaximumSize(370, 150)
		# self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
		# self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
		# self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
		# self.verticalLayout_9.setObjectName("verticalLayout_9")
		self.pushButton3 = QtWidgets.QPushButton(lgser.centralwidget)
		self.pushButton3.setGeometry(10, 30, 90, 30)
		self.pushButton3.setObjectName("pushButton3")
		self.pushButton3.setIcon(QIcon("file.png")) 
		self.pushButton3.setFlat(True)
		self.pushButton3.clicked.connect(self.read_data)
		self.pushButton3.show()
		#button4_clear
		# self.verticalLayoutWidget_11 = QtWidgets.QWidget(lgser.centralwidget)
		# self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(110, 30, 190, 130))
		# self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
		# self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
		# self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
		# self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.pushButton4 = QtWidgets.QPushButton(lgser.centralwidget)
		self.pushButton4.setGeometry(110, 30, 90, 30)
		self.pushButton4.setObjectName("pushButton3")
		self.pushButton4.setIcon(QIcon("clear.png")) 
		self.pushButton4.setFlat(True)
		self.pushButton4.clicked.connect(self.clear_data)
		#############filelist system#############
		self.verticalLayoutWidget_10 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 70, 190, 370))
		self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
		self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_10)
		self.tabWidget.setTabPosition(QTabWidget.West)
		self.tabWidget.setObjectName("tabWidget")
		self.verticalLayout_10.addWidget(self.tabWidget)

		# self.verticalLayoutWidget.show()
		# self.verticalLayoutWidget_9.show()
		# self.verticalLayoutWidget_10.show()

	def change_workdir(self,Mainwindow):
		dirname = QFileDialog.getExistingDirectory(Mainwindow,'open','../test_data')
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
		slm.title=title
		slm.qList=filedict[title]
		slm.setStringList(slm.qList)
		self.listView[number].setModel(slm)
		self.listView[number].clicked.connect(self.get_file)
		layout.addWidget(self.listView[number])
		self.tablist[number].setLayout(layout)

	def clear_tab(self,index):
		try:
			for i in self.tablist:
				self.tabWidget.removeTab(index)
		except:
			print('Delete table fail')

	def get_file(self,qModelIndex):
		self.selected_file = (qModelIndex.data())
		self.selected_title = (qModelIndex.model().title)

	def read_data(self):
		# try:
		file_data_temp = read.Read()
		self.file_data.append(file_data_temp)
		num = len(self.file_data)-1
		self.file_data[num].type = self.selected_title
		self.file_data[num].fname = self.selected_file
		if self.selected_title=='dump':
			self.file_data[num].data=self.file_data[num].read_dump(self.selected_file)
		elif self.selected_title=='contact':
			self.file_data[num].data=self.file_data[num].read_contact(self.selected_file)
		elif self.selected_title=='ave':
			self.file_data[num].data=self.file_data[num].read_ave(self.selected_file)
		elif self.selected_title=='print':
			self.file_data[num].data=self.file_data[num].read_print(self.selected_file)
		elif self.selected_title=='log':
			self.file_data[num].data=self.file_data[num].read_log_thermo(self.selected_file)
		print(str(len(self.file_data))+' files in temporary space')
		self.lg.variable_sys.catch_data(self.file_data)
		# except:
		# 	print("No target to read!")
	
	def clear_data(self):
		try:
			for i in range(len(self.file_data)):
				del self.file_data[len(self.file_data)-1-i]
		except:
			print("No target to clear")