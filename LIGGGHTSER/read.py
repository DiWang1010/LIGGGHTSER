#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import linecache

class Read:
	def __init__(self, name, version):
		self.name=name
		self.version=version

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
			with open(name,'r') as file:
				try:
					line = file.readline()
				except:
					filedict['others'].append(name)
					continue
				if line.startswith('ITEM'):
					text = linecache.getline(name,3)
					if text.startswith('ITEM: NUMBER OF ATOM'):
						filedict['dump'].append(name)
						continue
					if text.startswith('ITEM: NUMBER OF ENTRIES'):
						filedict['contact'].append(name)
						continue
				if line.startswith('LIGGGHTS'):
					filedict['log'].append(name)
					continue
				if line.startswith('# Fix print output for fix'):
					filedict['print'].append(name)
					continue
				if line.startswith('# Time-averaged data for fix'):
					filedict['ave'].append(name)
					continue
				filedict['others'].append(name)
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


