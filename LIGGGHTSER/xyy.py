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

class XYY:
	def __init__(self,maintab,mainplot,input_):
		self.input=input_
		self.tabWidget_plot=mainplot
		self.tab2 = QtWidgets.QWidget()
		self.tab2.setObjectName("XYY")
		maintab.addTab(self.tab2, "XYY")
		layout=QVBoxLayout()
		lineEdit1 = QtWidgets.QLineEdit(self.tab2)
		lineEdit1.setObjectName("lineEdit1")
		lineEdit1.setPlaceholderText("Please Eneter X, for example: step")
		layout.addWidget(lineEdit1)
		lineEdit2 = QtWidgets.QLineEdit(self.tab2)
		lineEdit2.setObjectName("lineEdit2")
		lineEdit2.setPlaceholderText("Please Eneter Y1, for example: xForce")
		layout.addWidget(lineEdit2)
		lineEdit3 = QtWidgets.QLineEdit(self.tab2)
		lineEdit3.setObjectName("lineEdit3")
		lineEdit3.setPlaceholderText("Please Eneter Y2, for example: yForce")
		layout.addWidget(lineEdit3)
		lineEdit4 = QtWidgets.QLineEdit(self.tab2)
		lineEdit4.setObjectName("lineEdit4")
		lineEdit4.setPlaceholderText("Please Eneter Y3, for example: zForce")
		layout.addWidget(lineEdit4)
		lineEdit5 = QtWidgets.QLineEdit(self.tab2)
		lineEdit5.setObjectName("lineEdit5")
		lineEdit5.setPlaceholderText("Please Eneter Y4, Zero mean ignore this")
		layout.addWidget(lineEdit5)
		pushButton = QtWidgets.QPushButton(self.tab2)
		pushButton.setObjectName("pushButton")
		pushButton.clicked.connect(lambda:self.cal_xyy(lineEdit1.text(),lineEdit2.text(),lineEdit3.text(),lineEdit4.text(),lineEdit5.text()))
		layout.addWidget(pushButton)
		self.tab2.setLayout(layout)

	def cal_xyy(self,x,y1,y2,y3,y4):
		data_list=self.input.file_data
		detection_flag=0
		for i in range(len(data_list)):
			dirctionary=data_list[i].data
			for j in dirctionary:
				if j==x:
					x=dirctionary[j]
					detection_flag=detection_flag+1
				elif j==y1:
					y1=dirctionary[j]
					detection_flag=detection_flag+1
				elif j==y2:
					y2=dirctionary[j]
					detection_flag=detection_flag+1
				elif j==y3:
					y3=dirctionary[j]
					detection_flag=detection_flag+1
				elif j==y4:
					y4=dirctionary[j]
					detection_flag=detection_flag+1
				else:
					continue
		if detection_flag > 5:
			print("More than one parameter detected")
			return
		if detection_flag < 2:
			print("Not enough parameter are detected")
			return
		self.plot_inner_xyy(x,y1,y2,y3,y4,'XYY')

	def plot_inner_xyy(self,x,y1,y2,y3,y4,name):
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
		if y1:
			ax.plot(x,y1)
		if y2:
			ax.plot(x,y2)
		if y3:
			ax.plot(x,y3)
		if y4:
			ax.plot(x,y4)
		layout.addWidget(canvas)
		tab0.setLayout(layout)