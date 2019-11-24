#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import LIGGGHTSER
import numpy as np
import matplotlib
import pylab as plt
read = LIGGGHTSER.read.Read()

plt.figure(figsize=(24,16))
font1={'weight':'normal','size':18,}
font2={'weight':'normal','size':16,}
fontlabel={'weight':'normal','size':18,}
xlow=2e7
xhigh=10e7
linewidth_set=5.0
binsize=300
matplotlib.rcParams['axes.prop_cycle']
angles=[(0,90)]

os.chdir(r'D:\ETH\origin_speed36\DEM')
top1=read.read_ave('./ave_force_top.txt')
os.chdir(r'D:\ETH\break_120\DEM')
top2=read.read_ave('./ave_force_top.txt')
number2=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_100\DEM')
top3=read.read_ave('./ave_force_top.txt')
number3=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_80-2\DEM')
top4=read.read_ave('./ave_force_top.txt')
number4=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_60\DEM')
top5=read.read_ave('./ave_force_top.txt')
number5=read.read_log_thermo('./log.liggghts')

l1=plt.plot(top1['TimeStep'],top1['v_yPos'],linewidth=linewidth_set,linestyle='-',label='Unbreakable')
l2=plt.plot(top2['TimeStep'],top2['v_yPos'],linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=120MPa')
l3=plt.plot(top3['TimeStep'],top3['v_yPos'],linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=100MPa')
l4=plt.plot(top4['TimeStep'],top4['v_yPos'],linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=80MPa')
l5=plt.plot(top5['TimeStep'],top5['v_yPos'],linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=60MPa')
plt.title('Thickness',loc='right',fontsize=24,pad=10)
plt.legend(loc='upper right',prop=font1)
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
plt.ylabel('Thickness(cm)',fontlabel)
plt.xlabel('TimeStep',fontlabel)
plt.xlim((xlow,xhigh))
plt.ylim((0.1460,0.151))

# plt.show()
fig = plt.gcf()
fig.savefig('../../FIG/Thickness.png',dpi=300)