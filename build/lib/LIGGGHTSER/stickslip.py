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

class stickslip:
	def __init__(self,maintab,mainplot,input_):
		self.input=input_
		self.tabWidget_plot=mainplot
		self.tab3 = QtWidgets.QWidget()
		self.tab3.setObjectName("Stick slip")
		maintab.addTab(self.tab3, "Stick slip")
		layout=QVBoxLayout()
		lineEdit1 = QtWidgets.QLineEdit(self.tab3)
		lineEdit1.setObjectName("lineEdit1")
		lineEdit1.setPlaceholderText("Please Eneter ave_force_top directory")
		layout.addWidget(lineEdit1)
		lineEdit3 = QtWidgets.QLineEdit(self.tab3)
		lineEdit3.setObjectName("lineEdit3")
		lineEdit3.setPlaceholderText("Please Eneter KE directory")
		layout.addWidget(lineEdit3)
		pushButton = QtWidgets.QPushButton(self.tab3)
		pushButton.setObjectName("pushButton")
		pushButton.clicked.connect(lambda:self.cal_plot(lineEdit1.text(),lineEdit3.text()))
		layout.addWidget(pushButton)
		self.tab3.setLayout(layout)
	def plot(self,dir1,dir2):
		read = LIGGGHTSER.read.Read()
		top=read.read_ave(dir1)
		ke=read.read_ave(dir2)
		plt.figure(figsize=(20,15))
		font1={'weight':'normal','size':18,}
		fontlabel={'weight':'normal','size':18,}

		ax411=plt.subplot(411)
		x=top['v_xForce']
		y=top['v_yForce']
		x=np.array(x)
		y=np.array(y)
		friction=x/y
		l11=plt.plot(top['TimeStep'],friction,linewidth=5.0,linestyle='-')
		# plt.xlim((3e7,6e7))
		# plt.ylim((0.1,0.51))
		# plt.xticks(np.arange(3e7,6e7,0.5e7))
		# plt.yticks(np.arange(0.1,0.5,0.1))
		plt.tick_params(labelsize=18,direction='in',pad=15)
		ax411.spines['bottom'].set_linewidth(3)
		ax411.spines['top'].set_linewidth(3)
		ax411.spines['left'].set_linewidth(3)
		ax411.spines['right'].set_linewidth(3)
		plt.title('Friction',loc='right',fontsize=24,pad=10)
		# ax411.set_title('Friction',fontsize=18)
		# plt.xlabel('TimeStep')
		plt.ylabel('Friciton ratio',fontlabel)


		ax412=plt.subplot(412)
		l21=plt.plot(top['TimeStep'],top['v_yPos'],linewidth=5.0,linestyle='-')
		# plt.xlim((3e7,6e7))
		# plt.ylim((0.148,0.150))
		# plt.xticks(np.arange(3e7,6e7,0.5e7))
		# plt.yticks(np.arange(1.48e-1,1.5e-1,5e-4))
		plt.tick_params(labelsize=18,direction='in',pad=15)
		ax412.spines['bottom'].set_linewidth(3)
		ax412.spines['top'].set_linewidth(3)
		ax412.spines['left'].set_linewidth(3)
		ax412.spines['right'].set_linewidth(3)
		plt.title('Mesh Position',loc='right',fontsize=24,pad=10)
		# plt.xlabel('TimeStep')
		plt.ylabel('Topmesh Position',fontlabel)

		ax413=plt.subplot(413)
		l31=plt.plot(ke['TimeStep'],ke['c_2'],linewidth=5.0,linestyle='-',zorder=30)
		# plt.xlim((3e7,6e7))
		# plt.ylim((0,10000))
		# plt.xticks(np.arange(3e7,6e7,0.5e7))
		# plt.yticks(np.arange(0,10000,1000))
		plt.tick_params(labelsize=18,direction='in',pad=15)
		ax413.spines['bottom'].set_linewidth(3)
		ax413.spines['top'].set_linewidth(3)
		ax413.spines['left'].set_linewidth(3)
		ax413.spines['right'].set_linewidth(3)
		# ax413.set_yscale("log")
		# plt.title('Energy',loc='right',fontsize=24,pad=10)
		# plt.xlabel('TimeStep')
		plt.ylabel('Kinetic Energy',fontlabel)
		plt.subplots_adjust(left=0.1,right=0.97,bottom=0.05,top=0.95, wspace= 0.1,hspace=0.4)
		plt.show()
