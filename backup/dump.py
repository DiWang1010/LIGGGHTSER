#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__auther__ = 'Roy Kid'

# A middle teir that can easily format data of lammps's dump
# and provide a serise of interfaces to access.
#


import re
import glob

oneline = 'Read LAMMPS dump files and extract position data'
docstr = """
    This module is used to extract position data from lammps dump.
"""

# Variables
# _properties : store box properties
#		[pro1, pro2...]
#                pro1 : {TIMESTEP:1000, NUBER_OF_ATOM:1000, ...}
#
# _field : store header
#	   [fie1, fie2...]
#          fie1 : {id:0, mol:1, type:2, ...}
#
# _data : store position
#	  [snap1, snap2,...]
#         snap1 : [[x0,y0,z0,...],
#                  [x1,y1,z1,...],...]

# Imports and external programs

# Class definition


class Dump:
    def __init__(self, fpath, every=1):
        self._fname = glob.glob(fpath)[0]
        self._every = every

    def __iter__(self):
        return self._read_data(self._fname, self._every)

    def _read_data(self, fname, every):
        snap_index = 0
        mode = str()
        dump = open(fname)
        line = dump.readline()

        while line.startswith('ITEM') :
            if snap_index % every == 0:
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


                snap['DATA'] = list()

                for line in dump:
                    try:
                        snap['DATA'].append([float(i) for i in line.split()])
                    except:
                        snap_index += 1
                        yield snap
                        break
            else:
                for line in dump:
                    line = dump.readline()
                    if line.startswith('ITEM: TIMESTEP'):
                        snap_index += 1
                        mode = 'every'
                        break
        
        if mode != 'every':
            yield snap


               
