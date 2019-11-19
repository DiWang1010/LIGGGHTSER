#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import LIGGGHTSER
import numpy as np
import matplotlib
import pylab as plt
import seaborn as sns
read = LIGGGHTSER.read.Read()

plt.figure(figsize=(20,12))
font1={'weight':'normal','size':18,}
fontlabel={'weight':'normal','size':18,}
xlow=2e7
xhigh=10e7
linewidth_set=2.0
binsize=300

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

ax211=plt.subplot(211)
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
l12=plt.plot(top2['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='breakable s=120MPa')
for i in range(min(len(break_atom2),len(top1['TimeStep']))):
    # print(i/len(break_atom3))
    if(break_atom2[i]==0):
        continue
    plt.scatter(timestep2[i],friction[i+26880], s=break_atom2[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
plt.tick_params(labelsize=18,direction='in',pad=15)
plt.xlim((xlow,xhigh))
plt.ylim((0.2,0.51))
plt.yticks(np.arange(0.2,0.51,0.1))
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.ylabel('Friction',fontlabel)
ax211y2=ax211.twinx()
timestep_break2=list()
break_atom_sum2=list()
for i in range(0,len(break_atom2)-binsize,binsize):
    timestep_break2.append(timestep2[i])
    break_atom_sum2.append(sum(break_atom2[i:i+binsize]))
# l13=ax211y2.plot(timestep2,break_atom2,linewidth=linewidth_set,color='blue',linestyle='-',alpha=0.3,label='broken particle number')
# l13=ax211y2.bar(timestep2,break_atom2,width = 1e5,facecolor = 'lightskyblue',label='broken particle number')
l13=ax211y2.bar(timestep_break2,break_atom_sum2,width = binsize*1000,facecolor = 'lightskyblue',alpha=0.5,label='broken particle number',zorder=4)
# plt.hist(break_atom2,bins=20,color='red',histtype='stepfilled',alpha=0.75)
plt.ylabel('Particle Number',fontlabel)
plt.ylim((0,15))
plt.yticks(np.arange(0,15,2))
# plt.ylim((0.5,3.5))
# plt.yticks(np.arange(1,3.1,1))
plt.tick_params(labelsize=18,direction='in',pad=15)
plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
ls=l11+l12
# ls=l11+l12+l13
labs=[l.get_label() for l in ls]
ax.legend(ls,labs,loc='lower right',prop=font1)

ax212=plt.subplot(212)
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
l22=plt.plot(top3['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='breakable s=100MPa')
for i in range(len(break_atom3)):
    # print(i/len(break_atom3))
    if(break_atom3[i]==0):
        continue
    plt.scatter(timestep3[i],friction[i+26880], s=break_atom3[i]*50,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
plt.tick_params(labelsize=18,direction='in',pad=15)
plt.xlim((xlow,xhigh))
plt.ylim((0.2,0.51))
plt.yticks(np.arange(0.2,0.51,0.1))
ax=plt.gca()
ax.spines['bottom'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.ylabel('Friction',fontlabel)
ax212y2=ax212.twinx()
timestep_break3=list()
break_atom_sum3=list()
for i in range(0,len(break_atom3)-binsize,binsize):
    # print(break_atom3[i:i+binsize])
    timestep_break3.append(timestep3[i])
    break_atom_sum3.append(sum(break_atom3[i:i+binsize]))
# print(len(timestep_break3))
# print(len(break_atom_sum3))
# print(timestep_break3)
# print(break_atom_sum3)
# l23=ax212y2.plot(timestep3,break_atom3,linewidth=linewidth_set,color='blue',linestyle='-',alpha=0.3,label='broken particle number')
l23=ax212y2.bar(timestep_break3,break_atom_sum3,width = binsize*1000,facecolor = 'lightskyblue',alpha=0.5,label='broken particle number')
plt.ylabel('Particle Number',fontlabel)
plt.ylim((0,15))
plt.yticks(np.arange(0,15,2))
# plt.ylim((0.5,3.5))
# plt.yticks(np.arange(1,3.1,1))
plt.tick_params(labelsize=18,direction='in',pad=15)
plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
ls=l21+l22
# ls=l11+l12+l13
labs=[l.get_label() for l in ls]
ax.legend(ls,labs,loc='lower right',prop=font1)
# ax412=plt.subplot(412)
# x=top1['v_xForce']
# y=top1['v_yForce']
# x=np.array(x)
# y=np.array(y)
# friction=x/y
# l21=plt.plot(top1['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='Unbreakable')
# x=top3['v_xForce']
# y=top3['v_yForce']
# x=np.array(x)
# y=np.array(y)
# friction=x/y
# l22=plt.plot(top3['TimeStep'],friction,linewidth=linewidth_set,linestyle='-',label='breakable s=100MPa')
# plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.xlim((xlow,xhigh))
# plt.ylim((0.2,0.51))
# plt.yticks(np.arange(0.2,0.51,0.1))
# ax412.spines['bottom'].set_linewidth(3)
# ax412.spines['top'].set_linewidth(3)
# ax412.spines['left'].set_linewidth(3)
# ax412.spines['right'].set_linewidth(3)
# plt.ylabel('Friction',fontlabel)
# # print((timestep3[0]-top3['TimeStep'][0])/1000)
# # print(top3['TimeStep'][0])
# for i in range(len(break_atom3)):
#     # print(i/len(break_atom3))
#     if(break_atom3[i]==0):
#         continue
#     plt.scatter(timestep3[i],friction[i+26880], s=break_atom3[i]*30,color='blue',edgecolors='black',linewidth=0.5,zorder=3,alpha=0.3)
# ax412y2=ax412.twinx()
# l23=ax412y2.plot(timestep3,break_atom3,linewidth=linewidth_set,color='blue',linestyle='-',alpha=0.3,label='broken particle number')
# plt.ylabel('Particle Number',fontlabel)
# plt.ylim((0.5,3.5))
# plt.yticks(np.arange(1,3.1,1))
# plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
# ls=l21+l22
# # ls=l21+l22+l23
# labs=[l.get_label() for l in ls]
# ax412.legend(ls,labs,loc='lower right',prop=font1)


# ax413=plt.subplot(413)
# l31=plt.plot(top1['TimeStep'],top1['v_yPos'],linewidth=linewidth_set,linestyle='-')
# l32=plt.plot(top2['TimeStep'],top2['v_yPos'],linewidth=linewidth_set,linestyle='-')
# l33=plt.plot(top3['TimeStep'],top3['v_yPos'],linewidth=linewidth_set,linestyle='-')
# plt.xlim((xlow,xhigh))
# plt.ylim((0.1485,0.1505))
# plt.yticks(np.arange(1.485e-1,1.505e-1,5e-4))
# plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.ylabel('Topmesh Position (cm)',fontlabel)
# plt.legend([l31,l32,l33],labels=['Unbreakable','breakable s=120MPa','breakable s=100MPa'],loc='lower right',prop=font1)
# ax413.spines['bottom'].set_linewidth(3)
# ax413.spines['top'].set_linewidth(3)
# ax413.spines['left'].set_linewidth(3)
# ax413.spines['right'].set_linewidth(3)
# plt.title('Mesh Position',loc='right',fontsize=24,pad=10)
# plt.ylabel('Topmesh Position(cm)',fontlabel)

# ax414=plt.subplot(414)
# l41=plt.plot(ke1['TimeStep'],ke1['c_2'],linewidth=linewidth_set,linestyle='-',zorder=3)
# l42=plt.plot(ke2['TimeStep'],ke2['c_2'],linewidth=linewidth_set,linestyle='-',zorder=2)
# l43=plt.plot(ke3['TimeStep'],ke3['c_2'],linewidth=linewidth_set,linestyle='-',zorder=1)
# plt.xlim((xlow,xhigh))
# plt.ylim((0,12000))
# plt.yticks(np.arange(0,12000,2000))
# ax414.spines['bottom'].set_linewidth(3)
# ax414.spines['top'].set_linewidth(3)
# ax414.spines['left'].set_linewidth(3)
# ax414.spines['right'].set_linewidth(3)
# plt.tick_params(labelsize=18,direction='in',pad=15)
# plt.ylabel('Kinetic Energy (1e-7 J)',fontlabel)
# plt.title('Energy',loc='right',fontsize=24,pad=10)
# plt.legend([l41,l42,l43],labels=['Unbreakable','breakable s=120MPa','breakable s=100MPa'],loc='lower right',prop=font1)
plt.xlabel('TimeStep',fontlabel)

# # plt.xlim((3e7,6e7))
# # plt.ylim((0,10000))
# # plt.xticks(np.arange(3e7,6e7,0.5e7))
# # plt.yticks(np.arange(0,10000,1000))
# plt.tick_params(labelsize=18,direction='in',pad=15)
# ax413.spines['bottom'].set_linewidth(3)
# ax413.spines['top'].set_linewidth(3)
# ax413.spines['left'].set_linewidth(3)
# ax413.spines['right'].set_linewidth(3)
# # ax413.set_yscale("log")
# # plt.title('Energy',loc='right',fontsize=24,pad=10)
# # plt.xlabel('TimeStep')
# plt.ylabel('Kinetic Energy',fontlabel)


# os.chdir(r'D:\ETH\break_100\DEM')
# top=read.read_ave('./ave_force_top.txt')
# ke=read.read_ave('./KE.txt')
# number=read.read_log_thermo('./log.liggghts')

# plt.subplot(411)
# x=top['v_xForce']
# y=top['v_yForce']
# x=np.array(x)
# y=np.array(y)
# friction=x/y
# l12=plt.plot(top['TimeStep'],friction,linewidth=5.0,linestyle='-')
# plt.xlim((xlow,xhigh))
# plt.ylim((0.2,0.51))
# # plt.xticks(np.arange(3e7,6e7,0.5e7))
# plt.yticks(np.arange(0.2,0.51,0.1))
# # plt.title('Friction',loc='right')
# # plt.xlabel('TimeStep')
# plt.ylabel('Friciton ratio',fontlabel)

# plt.legend([l11,l12],labels=['Unbreakable','breakable'],loc='lower right',prop=font1)

# plt.subplot(412)
# l22=plt.plot(top['TimeStep'],top['v_yPos'],linewidth=5.0,linestyle='-')
# plt.xlim((xlow,xhigh))
# plt.ylim((0.1485,0.1505))
# # plt.xticks(np.arange(3e7,6e7,0.5e7))
# plt.yticks(np.arange(1.485e-1,1.505e-1,5e-4))
# # plt.title('Mesh Position',loc='right')
# # plt.xlabel('TimeStep')
# plt.ylabel('Topmesh Position (cm)',fontlabel)
# plt.legend([l21,l22],labels=['Unbreakable','breakable'],loc='lower left',prop=font1)

# plt.subplot(413)
# l32=plt.plot(ke['TimeStep'],ke['c_2'],linewidth=5.0,linestyle='-',zorder=20)
# plt.xlim((xlow,xhigh))
# plt.ylim((0,8000))
# # plt.xticks(np.arange(3e7,6e7,0.5e7))
# plt.yticks(np.arange(0,13000,2000))
# plt.title('Energy',loc='right',fontsize=24,pad=10)
# # plt.xlabel('TimeStep')
# plt.ylabel('Kinetic Energy (1e-7 J)',fontlabel)
# plt.legend([l31,l32],labels=['Unbreakable','breakable'],loc='upper left',prop=font1)

# timestep=list()
# atoms=list()
# for i in number['data2']:
# 	timestep.append(i[0])
# 	atoms.append(i[1])

# break_atom=list()
# for i in range(len(atoms)-1):
# 	break_atom.append(round((atoms[i+1]-atoms[i])/13))
# break_atom.append(0)

# ax414=ax411.twinx()
# # ax414=plt.subplot(414)
# l41=ax414.plot(timestep,break_atom,linewidth=5.0,color='blue',linestyle='-',alpha=0.3)
# plt.xlim((xlow,xhigh))
# plt.ylim((0.5,3.5))
# # plt.xticks(np.arange(3e7,6e7,0.5e7))
# plt.yticks(np.arange(1,3.1,1))
# plt.tick_params(labelsize=18,direction='in',pad=15)
# ax414.spines['bottom'].set_linewidth(3)
# ax414.spines['top'].set_linewidth(3)
# ax414.spines['left'].set_linewidth(3)
# ax414.spines['right'].set_linewidth(3)
# plt.title('Friction & Broken Particles',loc='right',fontsize=24,pad=10)
# plt.xlabel('TimeStep',fontlabel)
# plt.ylabel('Particle Number',fontlabel)

# os.chdir(r'D:\ETH\break_loss2\DEM')
# top=read.read_ave('./ave_force_top.txt')
# ke=read.read_ave('./KE.txt')
# number=read.read_log_thermo('./log.liggghts')


# plt.subplot(411)
# x=top['v_xForce']
# y=top['v_yForce']
# x=np.array(x)
# y=np.array(y)
# friction=x/y
# l13=plt.plot(top['TimeStep'],friction,linewidth=5.0,linestyle='-')
# plt.xlim((xlow,xhigh))
# plt.ylim((0.1,0.51))
# # plt.xticks([3e7,3.5e7,4e7,4.5e7,5e7,5.5e7,6e7])
# plt.yticks(np.arange(0.1,0.51,0.1))
# # plt.title('Friction',loc='right')
# # plt.xlabel('TimeStep')
# plt.ylabel('Friciton ratio',fontlabel)
# plt.legend([l11,l12,l13],labels=['Unbreakable','Breakable','Breakable with mass loss'],loc='lower right',prop=font1)

# plt.subplot(412)
# l23=plt.plot(top['TimeStep'],top['v_yPos'],linewidth=5.0,linestyle='-')
# plt.xlim((xlow,xhigh))
# plt.ylim((0.148,0.152))
# # plt.xticks([3e7,3.5e7,4e7,4.5e7,5e7,5.5e7,6e7])
# plt.yticks(np.arange(1.48e-1,1.52e-1,5e-4))
# # plt.title('Mesh Position',loc='right')
# # plt.xlabel('TimeStep')
# plt.ylabel('Topmesh Position',fontlabel)
# plt.legend([l21,l22,l23],labels=['Unbreakable','Breakable','Breakable with mass loss'],loc='upper left',prop=font1)

# plt.subplot(413)
# l33=plt.plot(ke['TimeStep'],ke['c_2'],linewidth=5.0,linestyle='-',zorder=10)
# plt.xlim((xlow,xhigh))
# plt.ylim((0,10000))
# # plt.xticks(np.arange(xlow,xhigh,0.5e7))
# # plt.xticks([3e7,3.5e7,4e7,4.5e7,5e7,5.5e7,6e7])
# plt.yticks(np.arange(0,10000,2000))
# # plt.title('Energy',loc='right')
# # plt.xlabel('TimeStep')
# plt.ylabel('Kinetic Energy',fontlabel)
# plt.legend([l31,l32,l33],labels=['Unbreakable','Breakable','Breakable with mass loss'],loc='upper right',prop=font1)

# timestep=list()
# atoms=list()
# for i in number['data2']:
# 	timestep.append(i[0])
# 	atoms.append(i[1])

# break_atom=list()
# for i in range(len(atoms)-1):
# 	break_atom.append((atoms[i+1]-atoms[i])/13)

# break_atom.append(0)
# break_atom[0]=break_atom[0]-1# one particle outside the system broken
# plt.subplot(414)
# l42=plt.plot(timestep,break_atom,linewidth=5.0,color='lime',linestyle='-')
# plt.xlim((xlow,xhigh))
# plt.ylim((0.5,3.5))
# # plt.xticks([3e7,3.5e7,4e7,4.5e7,5e7,5.5e7,6e7])
# plt.yticks(np.arange(1,3.1,1))
# # plt.title('Particles',loc='right')
# plt.xlabel('TimeStep',fontlabel)
# plt.ylabel('Particle Number',fontlabel)
# plt.legend([l41,l42],labels=['Breakable','Breakable with mass loss'],loc='upper left',prop=font1)



plt.subplots_adjust(left=0.1,right=0.9,bottom=0.1,top=0.95, wspace= 0.1,hspace=0.3)
# plt.show()




fig = plt.gcf()
fig.savefig('../../FIG/break.png',dpi=300)
