#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import LIGGGHTSER
import numpy as np
import matplotlib
import pylab as plt

read = LIGGGHTSER.read.Read()

plt.figure(figsize=(28,15))
font1={'weight':'normal','size':18,}
fontlabel={'weight':'normal','size':18,}
xlow=2e7
xhigh=10e7
linewidth_set=2.0
binsize=300
breakhigh=11

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

ax411=plt.subplot(411)
x=top1['v_xForce']
y=top1['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l11=plt.plot(top1['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Unbreakable')
x=top2['v_xForce']
y=top2['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l12=plt.plot(top2['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=120MPa')
for i in range(min(len(break_atom2),len(top1['TimeStep']))):
    if(break_atom2[i]==0):
        continue
    plt.scatter(timestep2[i],friction[i+26880], s=break_atom2[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
y=max(break_atom2)
x=break_atom2.index(y)
plt.annotate('Beakage model inserted \nInitially '+str(y)+' particles break',xy=(timestep2[x],friction[x+26880]),xytext=(3e7,0.45),arrowprops=dict(facecolor='black',shrink=0.02),fontsize=14)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
plt.xlim((xlow,xhigh))
plt.ylim((0.2,0.51))
plt.yticks(np.arange(0.2,0.51,0.1))
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.ylabel('Friction',fontlabel)
ax411y2=ax411.twinx()
timestep_break2=list()
break_atom_sum2=list()
for i in range(0,len(break_atom2)-binsize,binsize):
    timestep_break2.append(timestep2[i])
    break_atom_sum2.append(sum(break_atom2[i:i+binsize]))
l13=ax411y2.bar(timestep_break2,break_atom_sum2,width = binsize*1000,facecolor = 'lightskyblue',alpha=0.5,label='Broken particle number',zorder=4)
plt.ylabel('Particle Number',fontlabel)
plt.ylim((0,breakhigh))
plt.yticks(np.arange(0,breakhigh,2))
plt.legend(loc='upper right',prop=font1)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
plt.title('Friction & Broken Particles',fontsize=24,pad=10)
ls=l11+l12
labs=[l.get_label() for l in ls]
ax.legend(ls,labs,loc='lower right',prop=font1)

ax412=plt.subplot(412)
x=top1['v_xForce']
y=top1['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l21=plt.plot(top1['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Unbreakable')
x=top3['v_xForce']
y=top3['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l22=plt.plot(top3['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=100MPa')
for i in range(len(break_atom3)):
    # print(i/len(break_atom3))
    if(break_atom3[i]==0):
        continue
    plt.scatter(timestep3[i],friction[i+26880], s=break_atom3[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
y=max(break_atom3)
x=break_atom3.index(y)
plt.annotate('Beakage model inserted \nInitially '+str(y)+' particles break',xy=(timestep2[x],friction[x+26880]),xytext=(3e7,0.45),arrowprops=dict(facecolor='black',shrink=0.02),fontsize=14)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
plt.xlim((xlow,xhigh))
plt.ylim((0.2,0.51))
plt.yticks(np.arange(0.2,0.51,0.1))
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.ylabel('Friction',fontlabel)
ax412y2=ax412.twinx()
timestep_break3=list()
break_atom_sum3=list()
for i in range(0,len(break_atom3)-binsize,binsize):
    timestep_break3.append(timestep3[i])
    break_atom_sum3.append(sum(break_atom3[i:i+binsize]))
l23=ax412y2.bar(timestep_break3,break_atom_sum3,width = binsize*1000,facecolor = 'lightskyblue',alpha=0.5,label='Broken particle number')
plt.ylabel('Particle Number',fontlabel)
plt.ylim((0,breakhigh))
plt.yticks(np.arange(0,breakhigh,2))
plt.legend(loc='upper right',prop=font1)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
# plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
ls=l21+l22
labs=[l.get_label() for l in ls]
ax.legend(ls,labs,loc='lower right',prop=font1)

ax413=plt.subplot(413)
x=top1['v_xForce']
y=top1['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l31=plt.plot(top1['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Unbreakable')
x=top4['v_xForce']
y=top4['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l32=plt.plot(top4['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=80MPa')
for i in range(len(break_atom4)):
    # print(i/len(break_atom3))
    if(break_atom4[i]==0):
        continue
    plt.scatter(timestep4[i],friction[i+26880], s=break_atom4[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
y=max(break_atom4)
x=break_atom4.index(y)
plt.annotate('Beakage model inserted \nInitially '+str(y)+' particles break',xy=(timestep2[x],friction[x+26880]),xytext=(3e7,0.45),arrowprops=dict(facecolor='black',shrink=0.02),fontsize=14)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
plt.xlim((xlow,xhigh))
plt.ylim((0.2,0.51))
plt.yticks(np.arange(0.2,0.51,0.1))
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.ylabel('Friction',fontlabel)
ax413y2=ax413.twinx()
timestep_break4=list()
break_atom_sum4=list()
for i in range(0,len(break_atom4)-binsize,binsize):
    timestep_break4.append(timestep4[i])
    break_atom_sum4.append(sum(break_atom4[i:i+binsize]))
l33=ax413y2.bar(timestep_break4,break_atom_sum4,width = binsize*1000,facecolor = 'lightskyblue',alpha=0.5,label='Broken particle number')
plt.ylabel('Particle Number',fontlabel)
plt.ylim((0,breakhigh))
plt.yticks(np.arange(0,breakhigh,2))
plt.legend(loc='upper right',prop=font1)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
# plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
ls=l31+l32
labs=[l.get_label() for l in ls]
ax.legend(ls,labs,loc='lower right',prop=font1)
# plt.xlabel('TimeStep',fontlabel)


ax414=plt.subplot(414)
x=top1['v_xForce']
y=top1['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l41=plt.plot(top1['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Unbreakable')
x=top5['v_xForce']
y=top5['v_yForce']
x=np.array(x)
y=np.array(y)
friction=x/y
l42=plt.plot(top5['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Breakable $ \ q_{crit} $=60MPa')
for i in range(len(break_atom5)):
    # print(i/len(break_atom3))
    if(break_atom5[i]==0):
        continue
    plt.scatter(timestep5[i],friction[i+26880], s=break_atom5[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
y=max(break_atom5)
x=break_atom5.index(y)
plt.annotate('Beakage model inserted \nInitially '+str(y)+' particles break',xy=(timestep2[x],friction[x+26880]),xytext=(3e7,0.45),arrowprops=dict(facecolor='black',shrink=0.02),fontsize=14)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
plt.xlim((xlow,xhigh))
plt.ylim((0.2,0.51))
plt.yticks(np.arange(0.2,0.51,0.1))
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.ylabel('Friction',fontlabel)
plt.xlabel('TimeStep',fontlabel)
ax414y2=ax414.twinx()
timestep_break5=list()
break_atom_sum5=list()
for i in range(0,len(break_atom5)-binsize,binsize):
    timestep_break5.append(timestep5[i])
    break_atom_sum5.append(sum(break_atom5[i:i+binsize]))
l43=ax414y2.bar(timestep_break5,break_atom_sum5,width = binsize*1000,facecolor = 'lightskyblue',alpha=0.5,label='Broken particle number')
plt.ylabel('Particle Number',fontlabel)
plt.ylim((0,breakhigh))
plt.yticks(np.arange(0,breakhigh,2))
plt.legend(loc='upper right',prop=font1)
plt.tick_params(labelsize=18,direction='in',width=2,length=10,pad=15)
# plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
ls=l41+l42
labs=[l.get_label() for l in ls]
ax.legend(ls,labs,loc='lower right',prop=font1)








plt.subplots_adjust(left=0.1,right=0.9,bottom=0.1,top=0.95, wspace= 0.1,hspace=0.3)
# plt.show()


fig = plt.gcf()
fig.savefig('../../FIG/break.png',dpi=300)
