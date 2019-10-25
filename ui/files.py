# -*- coding: utf-8 -*-
import sys

class Files(object):
	def __init__(self):
		pass

	def change_workdir(self,Marinwindow):
		dirname = QFileDialog.getExistingDirectory(MainWindow,'open','./')
		if dirname:
			try:
				os.chdir(dirname)
			except:
				print('error:cannot change to this directory'+dirname)
