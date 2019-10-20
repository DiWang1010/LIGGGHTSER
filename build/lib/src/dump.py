#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A middle teir that can easily format data of lammps's dump
# and provide a serise of interfaces to access.
#


import re
import glob

def read_data(fname):
    mode = str()
    dump = open(fname)
    line = dump.readline()

    print("function strat")
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
            

        
        snap['DATA'] = list()
        for items in range(len(m)):
            snap[m[items]] = list()

        for line in dump:
            try:
                snap['DATA'].append([float(i) for i in line.split()])
            except:
                for i in range(len(snap['DATA'])):
                    for items in range(len(m)):
                        snap[m[items]].append(snap['DATA'][i][items])
                return snap
                break


               
