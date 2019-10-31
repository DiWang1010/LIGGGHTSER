#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt, QStringListModel
from PyQt5.QtGui import QTextCursor, QIcon
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pylab as plt

class Friction:
	def __init__(self,maintab,mainplot,input_):
		self.input=input_
		self.tabWidget_plot=mainplot
		self.tab1 = QtWidgets.QWidget()
		self.tab1.setObjectName("Friction")
		maintab.addTab(self.tab1, "Friction")
		# label1 = QLabel(self.tab1)
		# label1.setText("")
		# label1.setAlignment(Qt.AlignCenter | Qt.AlignLeft)
		layout=QVBoxLayout()
		lineEdit1 = QtWidgets.QLineEdit(self.tab1)
		lineEdit1.setObjectName("lineEdit1")
		lineEdit1.setPlaceholderText("Please Eneter time, for example: step")
		layout.addWidget(lineEdit1)
		lineEdit2 = QtWidgets.QLineEdit(self.tab1)
		lineEdit2.setObjectName("lineEdit2")
		lineEdit2.setPlaceholderText("Please Eneter Mesh Force on X aixs, for example: xForce")
		layout.addWidget(lineEdit2)
		lineEdit3 = QtWidgets.QLineEdit(self.tab1)
		lineEdit3.setObjectName("lineEdit3")
		lineEdit3.setPlaceholderText("Please Eneter Mesh Force on Y aixs, for example: yForce")
		layout.addWidget(lineEdit3)
		pushButton = QtWidgets.QPushButton(self.tab1)
		pushButton.setObjectName("pushButton")
		pushButton.clicked.connect(lambda:self.cal_friction(lineEdit1.text(),lineEdit2.text(),lineEdit3.text()))
		layout.addWidget(pushButton)
		self.tab1.setLayout(layout)

	def cal_friction(self,time,xtitle,ytitle):
		data_list=self.input.file_data
		detection_flag=0
		for i in range(len(data_list)):
			if data_list[i].type == 'ave' or data_list[i].type == 'print' or data_list[i].type == 'log':
				dirctionary=data_list[i].data
				for j in dirctionary:
					if j==time:
						time=dirctionary[j]
						detection_flag=detection_flag+1
					elif j==xtitle:
						x=dirctionary[j]
						detection_flag=detection_flag+1
					elif j==ytitle:
						y=dirctionary[j]
						detection_flag=detection_flag+1
					else:
						continue
		if detection_flag > 3:
			print("More than one parameter detected")
			return
		if detection_flag < 3:
			print("Not enough parameter are detected")
			return

		time=np.array(time)
		x=np.array(x)
		y=np.array(y)
		self.friction=np.vstack((time,x/y))
		self.plot_inner_new(time,self.friction[1,:],'Friction')

	def plot_inner_new(self,x,y,name):
		tab0=QtWidgets.QWidget()
		# tab0=plot_widget()
		tab0.setObjectName(name)
		self.tabWidget_plot.addTab(tab0, name)
		# self.tab_plot_list.append(tab0)
		layout=QVBoxLayout()
		# layout.addWidget(pushButton)
		figure = plt.figure()
		canvas = FigureCanvas(figure)
		ax=figure.add_axes([0.1,0.1,0.8,0.8])
		ax.plot(x,y)
		layout.addWidget(canvas)
		tab0.setLayout(layout)


