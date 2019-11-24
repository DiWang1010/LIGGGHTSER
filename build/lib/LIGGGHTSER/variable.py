#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt, QStringListModel
from PyQt5.QtGui import QTextCursor, QIcon
import numpy as np
class Variable:
	def __init__(self,lgser,Mainwindow,Files):
		self.input = Files
		self.verticalLayoutWidget_6 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(650, 30, 360, 410))
		self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
		self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_6)
		self.tabWidget.setObjectName("tabWidget")
		self.verticalLayout_6.addWidget(self.tabWidget)
	
	def catch_data(self,data):
		self.variables = data
		self.clear_tab(0)
		# try:
		title=list()
		for i in self.variables:
			title.append(i.fname)

		self.tablist = [QtWidgets.QWidget() for i in range(len(self.variables))]
		self.listView = [QtWidgets.QListView() for i in range(len(self.variables))]
		# self.qList=list()
		for i in range(len(self.variables)):
			self.tablist[i].setObjectName(title[i])
			self.tabWidget.addTab(self.tablist[i], title[i])
			self.show_items(self.variables[i].data,i)
		self.tabWidget.show()
		# except:
		# 	print('cannot read directory'+os.getcwd())
		# 	return

	def clear_tab(self,index):
		try:
			for i in self.tablist:
				self.tabWidget.removeTab(index)
		except:
			print('Delete variable fail')

	def show_items(self,filedict,number):
		layout=QVBoxLayout()
		self.listView[number] = QtWidgets.QListView()
		self.listView[number].setObjectName("listView"+str(number))
		slm=QStringListModel()
		slm.title=number
		name=list()
		# print(filedict)
		for i in filedict:
			name.append(i)
		slm.qList=name
		slm.setStringList(slm.qList)
		slm.data=filedict
		self.listView[number].setModel(slm)
		self.listView[number].clicked.connect(self.show_detail)
		layout.addWidget(self.listView[number])
		self.tablist[number].setLayout(layout)

	def show_detail(self,qModelIndex):
		self.newtable = QtWidgets.QWidget()
		self.newtable.setObjectName("newtable")
		self.newtable.setGeometry(300,300,300,300)
		layout = QGridLayout()
		data=qModelIndex.model().data[qModelIndex.data()]
		data=np.array(data)
		x=data.shape[0]
		try:
			y=data.shape[1]
		except:
			y=1
		heretable=QTableWidget(x,y)
		# heretable.setHorizontalHeaderLabels(['FileName','size/KB'])
		# heretable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		# heretable.setColumnWidth(0,220)
		# heretable.setColumnWidth(1,132)
		if y==1:
			for i in range(x):
				newitem = QTableWidgetItem(str(data[i]))
				heretable.setItem(i,0,newitem)
		else:
			for i in range(x):
				for j in range(y):
					newitem = QTableWidgetItem(str(data[i][j]))
					heretable.setItem(i,j,str(newitem))
				# newitem.setTextAlignment(Qt.AlignRight)
		layout.addWidget(heretable,0,0)
		self.newtable.setLayout(layout)
		self.newtable.show()
		# layout.show()
		# self.tablist[number].setLayout(layout)