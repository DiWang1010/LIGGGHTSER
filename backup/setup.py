#!/usr/bin/env python
# -*- coding: utf-8 -*-

#compiled as pyc
#import py_compile
#py_compile.compile(r'./src/main.py',r'./src/main.pyc')

#compiled as so
from distutils.core import setup
from cPython.Build import cythonize
setup(ext_module = cythonize(["./src/main.py"]))