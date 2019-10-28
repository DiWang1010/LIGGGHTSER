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

class Calculation:
	def __init__(self,lgser,Mainwindow,Files):
		self.input = Files
				#############plot system#############
		self.verticalLayoutWidget_8 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(450, 450, 561, 221))
		self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
		self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_8)
		self.tabWidget.setObjectName("tabWidget")
		self.verticalLayout_8.addWidget(self.tabWidget)
		# self.tab_2 = QtWidgets.QWidget()
		# self.tab_2.setObjectName("tab_2")
		# self.tabWidget.addTab(self.tab_2, "")
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Friction")
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Tab 2")
		# self.tabWidget.setCurrentIndex(0)
		self.verticalLayoutWidget_3 = QtWidgets.QWidget(lgser.centralwidget)
		self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(220, 30, 410, 410))
		self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.tabWidget_plot = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
		self.tabWidget_plot.setObjectName("tabWidget_plot")
		self.verticalLayout_3.addWidget(self.tabWidget_plot)

		self.tab_plot_list=list()

		self.initial_friction()
		self.verticalLayoutWidget_3.show()

	def initial_friction(self):
		self.tab1 = QtWidgets.QWidget()
		self.tab1.setObjectName("Friction")
		self.tabWidget.addTab(self.tab1, "Friction")
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
						time=x=dirctionary[j]
						detection_flag=detection_flag+1
					if j==xtitle:
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
		tab0.setObjectName(name)
		self.tabWidget_plot.addTab(tab0, name)
		self.tab_plot_list.append(tab0)
		layout=QVBoxLayout()
		# layout.addWidget(pushButton)
		figure = plt.figure()
		canvas = FigureCanvas(figure)
		ax=figure.add_axes([0.1,0.1,0.8,0.8])
		ax.plot(x,y)
		layout.addWidget(canvas)
		tab0.setLayout(layout)
		# tab0.setCentralWidget(cavans)
		# canvas.draw()

		# pl.show()



