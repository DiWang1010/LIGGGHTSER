#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import linecache

class Read:
	def __init__(self):
		pass
		# self.name=name
		# self.version=version

	def read_file(self, dirname):
		filenames=list()
		for root, dirs, files in os.walk(dirname):
			files = [f for f in files if not f[0] == '.']
			dirs = [d for d in dirs if not d[0] == '.']
			for names in files:
				filenames.append(os.path.join(root,names))
		filedict = dict()
		filedict['dump'] = list()
		filedict['contact'] = list()
		filedict['log'] = list()
		filedict['print'] = list()
		filedict['ave'] = list()
		filedict['others'] = list()
		for name in filenames:
			try:
				filefid=open(name)
			except:
				print(['read file',name,'error'])
			try:
				line = filefid.readline()
			except:
				filedict['others'].append(name)
				filefid.close()
				continue
			if line.startswith('ITEM'):
				text = linecache.getline(name,3)
				if text.startswith('ITEM: NUMBER OF ATOM'):
					filedict['dump'].append(name)
					filefid.close()
					continue
				if text.startswith('ITEM: NUMBER OF ENTRIES'):
					filedict['contact'].append(name)
					filefid.close()
					continue
			if line.startswith('LIGGGHTS'):
				filedict['log'].append(name)
				filefid.close()
				continue
			if line.startswith('# Fix print output for fix'):
				filedict['print'].append(name)
				filefid.close()
				continue
			if line.startswith('# Time-averaged data for fix'):
				filedict['ave'].append(name)
				filefid.close()
				continue
			filedict['others'].append(name)
			filefid.close()
		print('Find dump file',len(filedict['dump']))
		print('Find contact file',len(filedict['contact']))
		print('Find log file',len(filedict['log']))
		print('Find print file',len(filedict['print']))
		print('Find ave file',len(filedict['ave']))
		print('Find others file',len(filedict['others']))
		return filedict

	def read_dump(self, fname):
		dump = open(fname)
		line = dump.readline()
		while line.startswith('ITEM') :
			snap = dict()
			if line.startswith('ITEM: TIMESTEP'):
				line = dump.readline()
				snap['TIMESTEP'] = int(line.split()[0])
				line = dump.readline()
			if line.startswith('ITEM: NUMBER OF ATOM'):
				line = dump.readline()
				snap['NUMBER_OF_ATOM'] = int(line.split()[0])
				line = dump.readline()
			if line.startswith('ITEM: BOX'):
				snap['BOUNDARY_CONDITIONN'] = line.split()[-3:]
				line = dump.readline()
				snap['BOUNDARY_X'] = [float(i)
									  for i in line.split()]
				line = dump.readline()
				snap['BOUNDARY_Y'] = [float(i)
									  for i in line.split()]
				line = dump.readline()
				snap['BOUNDARY_Z'] = [float(i)
									  for i in line.split()]
				line = dump.readline()

			if line.startswith('ITEM: ATOMS'):
				snap['HEADER'] = line.split()[2:]
				m=snap['HEADER']
				print(m)
				
			snap['DATA'] = list()
			for items in range(len(m)):
				snap[m[items]] = list()

			for line in dump:
				try:
					snap['DATA'].append([float(i) for i in line.split()])
				except:
					print('error: illegal dump file, data end with words')
					break

			for i in range(len(snap['DATA'])):
						for items in range(len(m)):
							snap[m[items]].append(snap['DATA'][i][items])
		dump.close()
		return snap

	def read_contact(self, fname):
		dump = open(fname)
		line = dump.readline()

		while line.startswith('ITEM') :
			snap = dict()
			if line.startswith('ITEM: TIMESTEP'):
				line = dump.readline()
				snap['TIMESTEP'] = int(line.split()[0])
				line = dump.readline()
			if line.startswith('ITEM: NUMBER OF ENTRIES'):
				line = dump.readline()
				snap['ITEM: NUMBER OF ENTRIES'] = int(line.split()[0])
				line = dump.readline()
			if line.startswith('ITEM: BOX BOUNDS'):
				snap['BOUNDARY_CONDITIONN'] = line.split()[-3:]
				line = dump.readline()
				snap['BOUNDARY_X'] = [float(i)
									  for i in line.split()]
				line = dump.readline()
				snap['BOUNDARY_Y'] = [float(i)
									  for i in line.split()]
				line = dump.readline()
				snap['BOUNDARY_Z'] = [float(i)
									  for i in line.split()]
				line = dump.readline()

			if line.startswith('ITEM: ENTRIES'):
				snap['HEADER'] = line.split()[2:]
				m=snap['HEADER']
				print(m)
				
			snap['DATA'] = list()
			for items in range(len(m)):
				snap[m[items]] = list()

			for line in dump:
				try:
					snap['DATA'].append([float(i) for i in line.split()])
				except:
					print('error: illegal contact file, data end with words')

			for i in range(len(snap['DATA'])):
						for items in range(len(m)):
							snap[m[items]].append(snap['DATA'][i][items])
		dump.close()
		return snap
	def read_ave(self,fname):
		with open(fname,'r') as ave:
			line = ave.readline()
			snap = dict()
			if line.startswith('#'):
				line = ave.readline()
				snap['HEADER'] = line.split()[1:]
				m=snap['HEADER']
				print(m)
			snap['DATA'] = list()
			for items in range(len(m)):
				snap[m[items]] = list()
			for line in ave:
				try:
					snap['DATA'].append([float(i) for i in line.split()])
				except:
					print('error: illegal ave file, data end with words')
					break
				
			for i in range(len(snap['DATA'])):
				for items in range(len(m)):
					snap[m[items]].append(snap['DATA'][i][items])
			ave.close()
		return snap
	def read_print(self,fname,title):
		with open(fname,'r') as printfile:
			if title==0:
				line = printfile.readline()
				snap = dict()
				snap['DATA'] = list()
				for line in printfile:
					try:
						snap['DATA'].append([float(i) for i in line.split()])
					except:
						print('error: illegal print file, data end with words')
						break
				return snap
			m=title
			line = printfile.readline()
			snap = dict()
			snap['DATA'] = list()
			for items in range(len(m)):
				snap[m[items]] = list()
			for line in printfile:
				try:
					snap['DATA'].append([float(i) for i in line.split()])
				except:
					print('error: illegal print file, data end with words')
					break
			for i in range(len(snap['DATA'])):
				for items in range(len(m)):
					snap[m[items]].append(snap['DATA'][i][items])
			printfile.close()
			return snap

	def read_in_output(self,fname):
		with open(fname,'r',encoding="gbk") as in_output:
			filedict= dict()
			filedict['ave']=list()
			filedict['print']=list()
			filedict['ave_title']=list()
			filedict['print_title']=list()
			filedict['thermo_title']=list()
			print('reading in file')
			for line in in_output:
				line.encode(encoding='utf-8',errors='ignore')
				if line.startswith('#'):
					continue
				if line.startswith('fix'):
					temparg=line.split()[3:]
					if temparg[0] == 'ave/time':
						print('Detected print:',line)
						for i in range(len(temparg)):
							if temparg[i]=='file':
								filedict['ave'].append(temparg[i+1])
								endvalue=i
						filedict['ave_title'].append(temparg[4:endvalue])
					if temparg[0] == 'print':
						print('Detected print:',line)
						for i in range(len(temparg)):
							if temparg[i]=='file':
								filedict['print'].append(temparg[i+1])
								endvalue=i
						print(temparg)
						temparg[2]=temparg[2][1:]
						temparg[endvalue]=temparg[endvalue][:-1]
						filedict['print_title'].append(temparg[2:endvalue])
				if line.startswith('thermo_style'):
					print('Detected print:',line)
					temparg=line.split()[1:]
					if temparg[0] == 'one' or temparg[0] == 'multi':
						filedict['thermo_title']=['step','atoms','ke','cpu']
					elif temparg[0] == 'custom':
						filedict['thermo_title'].append(temparg[1:])
					else:
						print('error: illegal thermo_style')
			in_output.close()
			return filedict
	def read_log_thermo(self,fname):
		with open(fname,'r',encoding="gbk") as lglog:
			index=0
			read_data_flag=0
			thermo=dict()
			thermo_title='thermo_title'+str(index)
			print(thermo_title)
			thermo[thermo_title]=list()
			thermo[thermo_title].append('#')
			for line in lglog:
				line.encode(encoding='utf-8',errors='ignore')
				if read_data_flag == 1:
					try:
						thermo[data].append([float(i) for i in line.split()])
					except:
						if line.startswith('Loop time'):
							read_data_flag=0
							continue
						if line.startswith('WARNING'):
							continue
						print('error: illegal thermo_data')
				if line.startswith('#'):
					continue
				if line.startswith('thermo_style'):
					index=index+1
					thermo_title='thermo_title'+str(index)
					thermo[thermo_title]=list()
					print('Detected thermo:',line)
					temparg=line.split()[1:]
					if temparg[0] == 'one' or temparg[0] == 'multi':
						thermo[thermo_title]=['step','atoms','ke','cpu']
					elif temparg[0] == 'custom':
						thermo[thermo_title].append(temparg[1:])
					else:
						print('error: illegal thermo_style')
				if line.startswith(str.title(thermo[thermo_title][0][0])):
					read_data_flag=1
					data='data'+str(index)
					thermo[data]=list()
			lglog.close()
			return thermo

	def data2dict(self,data,title):
		data_dict=dict()
		for i in data:
			print(i)