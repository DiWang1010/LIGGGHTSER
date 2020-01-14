#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import linecache

class Write:
	def __init__(self):
		pass
	def write_dump(self,dumpdata,filename):
		f = open(filename,'w')
		f.writelines('ITEM: TIMESTEP\n')
		f.writelines(str(dumpdata['TIMESTEP'])+'\n')
		f.writelines('ITEM: NUMBER OF ATOMS\n')
		f.writelines(str(dumpdata['NUMBER_OF_ATOM'])+'\n')
		f.writelines('ITEM: BOX BOUNDS ')
		f.writelines(dumpdata['BOUNDARY_CONDITIONN'][0]+' '+dumpdata['BOUNDARY_CONDITIONN'][1]+' '+dumpdata['BOUNDARY_CONDITIONN'][2]+'\n')
		f.writelines(str(dumpdata['BOUNDARY_X'][0])+' '+str(dumpdata['BOUNDARY_X'][1])+'\n')
		f.writelines(str(dumpdata['BOUNDARY_Y'][0])+' '+str(dumpdata['BOUNDARY_Y'][1])+'\n')
		f.writelines(str(dumpdata['BOUNDARY_Z'][0])+' '+str(dumpdata['BOUNDARY_Z'][1])+'\n')
		f.writelines('ITEM: ATOMS ')
		for i in dumpdata['HEADER']:
			f.writelines(i+' ')
		f.writelines('\n')
		for i in dumpdata['DATA']:
			for j in i:
				f.writelines(str(j)+' ')
			f.writelines('\n')
		f.close()
	def write_vector(self,name,vector):
		pass