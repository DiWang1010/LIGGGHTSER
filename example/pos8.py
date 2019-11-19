#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import LIGGGHTSER
import numpy as np
import matplotlib
import pylab as plt
# import seaborn as sns
read = LIGGGHTSER.read.Read()

plt.figure(figsize=(20,12))
font1={'weight':'normal','size':18,}
fontlabel={'weight':'normal','size':18,}
xlow=2e7
xhigh=10e7
linewidth_set=2.0

os.chdir(r'D:\ETH\origin_speed36\DEM')
top1=read.read_ave('./ave_force_top.txt')
os.chdir(r'D:\ETH\break_120\DEM')
top2=read.read_ave('./ave_force_top.txt')
number2=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_100\DEM')
top3=read.read_ave('./ave_force_top.txt')
number3=read.read_log_thermo('./log.liggghts')

timestep2=list()
atoms2=list()
for i in number2['data2']:
	timestep2.append(i[0])
	atoms2.append(i[1])

break_atom2=list()
sum_break2=list()
sum_break2.append(0)
for i in range(len(atoms2)-1):
	break_atom2.append(round((atoms2[i+1]-atoms2[i])/13))
	sum_break2.append(break_atom2[i]+sum_break2[i])
break_atom2.append(0)

timestep3=list()
atoms3=list()
for i in number3['data2']:
	timestep3.append(i[0])
	atoms3.append(i[1])

break_atom3=list()
for i in range(len(atoms3)-1):
	break_atom3.append(round((atoms3[i+1]-atoms3[i])/13))
break_atom3.append(0)

# ax211=plt.subplot(211)
# x=top1['v_xForce']
# y=top1['v_yForce']
# x=np.array(x)
# y=np.array(y)
# friction=x/y
# l11=plt.plot(top1['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Unbreakable')
# x=top2['v_xForce']
# y=top2['v_yForce']
# x=np.array(x)
# y=np.array(y)
# friction=x/y
# l12=plt.plot(top2['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='breakable s=120MPa')
# for i in range(min(len(break_atom2),len(top1['TimeStep']))):
#     # print(i/len(break_atom3))
#     if(break_atom2[i]==0):
#         continue
#     plt.scatter(timestep2[i],friction[i+26880], s=break_atom2[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
# plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.xlim((xlow,xhigh))
# plt.ylim((0.2,0.51))
# plt.yticks(np.arange(0.2,0.51,0.1))
# ax=plt.gca()
# ax211.spines['bottom'].set_linewidth(3)
# ax211.spines['top'].set_linewidth(3)
# ax211.spines['left'].set_linewidth(3)
# ax211.spines['right'].set_linewidth(3)
# plt.ylabel('Friction',fontlabel)
# ax211y2=ax211.twinx()
binsize=100
timestep_break2=list()
break_atom_sum2=list()
for i in range(0,len(break_atom2)-binsize,binsize):
    timestep_break2.append(timestep2[i])
    break_atom_sum2.append(sum(break_atom2[i:i+binsize]))
    # print(timestep2[i])
    # print(sum(break_atom2[i:i+binsize]))
# l13=ax211y2.plot(timestep2,break_atom2,linewidth=linewidth_set,color='blue',linestyle='-',alpha=0.3,label='broken particle number')
# l13=ax211y2.bar(timestep2,break_atom2,width = 0.35,facecolor = 'lightskyblue',label='broken particle number')
# l13=ax211y2.bar(timestep_break2,break_atom_sum2,width = 0.35,facecolor = 'lightskyblue',label='broken particle number')
x=np.array(timestep_break2)
y=np.array(break_atom_sum2)
# x=[1,2,3]
# y=[10,0,2]
# plt.bar(x,y)
print(timestep_break2[0:2])
print(break_atom_sum2[0:2])
plt.bar(timestep_break2[0:2],break_atom_sum2[0:2])
# plt.hist(break_atom2,bins=20,color='red',histtype='stepfilled',alpha=0.75)
# plt.ylabel('Particle Number',fontlabel)
# plt.ylim((0.5,3.5))
# plt.yticks(np.arange(1,3.1,1))
# plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
# ls=l11+l12
# # ls=l11+l12+l13
# labs=[l.get_label() for l in ls]
# ax.legend(ls,labs,loc='lower right',prop=font1)
plt.show()