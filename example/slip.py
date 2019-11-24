#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import LIGGGHTSER
import numpy as np
import matplotlib
import pylab as plt

read = LIGGGHTSER.read.Read()

plt.figure(figsize=(20,15))
font1={'weight':'normal','size':28,}
fontlabel={'weight':'normal','size':28,}
xlow=3e7
xhigh=13e7
linewidth_set=2.0

os.chdir(r'D:\ETH\origin_speed36\DEM')
top1=read.read_ave('./ave_force_top.txt')
os.chdir(r'D:\ETH\break_120\DEM')
top2=read.read_ave('./ave_force_top.txt')
number2=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_100\DEM')
top3=read.read_ave('./ave_force_top.txt')
number3=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_80\DEM')
top4=read.read_ave('./ave_force_top.txt')
number4=read.read_log_thermo('./log.liggghts')
os.chdir(r'D:\ETH\break_60\DEM')
top5=read.read_ave('./ave_force_top.txt')
number5=read.read_log_thermo('./log.liggghts')

timelist=list()
for i in range(len(top1['TimeStep'])):
	if top1['TimeStep'][i]<xhigh and top1['TimeStep'][i]>xlow:
		timelist.append(top1['TimeStep'][i])
	if top1['TimeStep'][i]==xlow:
		start=i
	if top1['TimeStep'][i]==xhigh:
		end=i-1

timestep2=list()
atoms2=list()
for i in number2['data2']:
	timestep2.append(i[0])
	atoms2.append(i[1])
break_atom2=list()
for i in range(len(atoms2)-1):
	break_atom2.append(round((atoms2[i+1]-atoms2[i])/13))
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

timestep4=list()
atoms4=list()
for i in number4['data2']:
	timestep4.append(i[0])
	atoms4.append(i[1])
break_atom4=list()
for i in range(len(atoms4)-1):
	break_atom4.append(round((atoms4[i+1]-atoms4[i])/13))
break_atom4.append(0)

timestep5=list()
atoms5=list()
for i in number5['data2']:
    timestep5.append(i[0])
    atoms5.append(i[1])
break_atom5=list()
for i in range(len(atoms5)-1):
    break_atom5.append(round((atoms5[i+1]-atoms5[i])/13))
break_atom5.append(0)

x=top1['v_xForce']
y=top1['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
slip_t1=list()
slip1=list()
for i in range(start,end):
	diff=friction[i]-friction[i+1]
	if diff>0.005:
		slip_t1.append(top1['TimeStep'][i])
		slip1.append(diff)
count_slip1=len(slip1)
count_bslip1=0

x=top2['v_xForce']
y=top2['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
slip_t2=list()
slip2=list()
slip_bt2=list()
slip_b2=list()
for i in range(start,end):
	diff=friction[i]-friction[i+1]
	if diff>0.005:
		slip_t2.append(top2['TimeStep'][i])
		slip2.append(diff)
		if break_atom2[i-26880]>0:
			slip_bt2.append(top2['TimeStep'][i])
			slip_b2.append(diff)
count_slip2=len(slip2)
count_bslip2=len(slip_bt2)

x=top3['v_xForce']
y=top3['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
slip_t3=list()
slip3=list()
slip_bt3=list()
slip_b3=list()
for i in range(start,end):
	diff=friction[i]-friction[i+1]
	if diff>0.005:
		slip_t3.append(top3['TimeStep'][i])
		slip3.append(diff)
		if break_atom3[i-26880]>0:
			slip_bt3.append(top2['TimeStep'][i])
			slip_b3.append(diff)
count_slip3=len(slip3)
count_bslip3=len(slip_bt3)

x=top4['v_xForce']
y=top4['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
slip_t4=list()
slip4=list()
slip_bt4=list()
slip_b4=list()
for i in range(start,end):
	diff=friction[i]-friction[i+1]
	if diff>0.005:
		slip_t4.append(top4['TimeStep'][i])
		slip4.append(diff)
		if break_atom4[i-26880]>0:
			slip_bt4.append(top2['TimeStep'][i])
			slip_b4.append(diff)
count_slip4=len(slip4)
count_bslip4=len(slip_bt4)

x=top5['v_xForce']
y=top5['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
slip_t5=list()
slip5=list()
slip_bt5=list()
slip_b5=list()
for i in range(start,end):
	diff=friction[i]-friction[i+1]
	if diff>0.005:
		slip_t5.append(top5['TimeStep'][i])
		slip5.append(diff)
		if break_atom5[i-26880]>0:
			slip_bt5.append(top2['TimeStep'][i])
			slip_b5.append(diff)
count_slip5=len(slip5)
count_bslip5=len(slip_bt5)

labels=['Unbreakable','$ \ q_{crit} $==120MPa','$ \ q_{crit} $==100MPa','$ \ q_{crit} $==80MPa','$ \ q_{crit} $==60MPa']
bar1=plt.bar(range(5),[count_slip1,count_slip2,count_slip3,count_slip4,count_slip5],width=0.35)
bar2=plt.bar([0.35,1.35,2.35,3.35,4.35],[count_bslip1,count_bslip2,count_bslip3,count_bslip4,count_bslip5],width=0.35)
plt.bar([0.175,1.175,2.175,3.175,4.175],[0,0,0,0,0],tick_label=labels)
plt.legend([bar1,bar2],['Number of slip event','Number of slip event with particle breakage'],loc='upper left',prop=font1)
plt.title('Number of slip events versus particle strength',fontsize=24,pad=10)
plt.ylabel('Number of slip events',fontlabel)
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.show()

fig = plt.gcf()
fig.savefig('../../FIG/slip.png',dpi=300)

