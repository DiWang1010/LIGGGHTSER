#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import linecache

def read_file(dirname):
	filenames=os.listdir(dirname)
	filedict = dict()
	filedict['dump'] = list()
	filedict['contact'] = list()
	filedict['log'] = list()
	filedict['print'] = list()
	filedict['ave'] = list()
	for name in filenames:
		with open(name,'r') as file:
		# file=open(name)
			line = file.readline()
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
				break
			if line.startswith('# Fix print output for fix'):
				filedict['print'].append(name)
				break
			if line.startswith('# Time-averaged data for fix'):
				filedict['ave'].append(name)
				break
		# file.close()
	return filedict



