import os
import LIGGGHTSER
import numpy as np
read = LIGGGHTSER.read.Read()
write = LIGGGHTSER.write.Write()
os.chdir('/home/wd/ETHproject/temp/DEM2')

filedict = read.read_file('./')
for i in filedict['dump']:
	print(i)
	dump=read.read_dump(i)
	write.write_dump(dump,'test.txt')

