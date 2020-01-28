#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from paramiko import SSHClient
from scp import SCPClient
import time
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE

class ob:
	def __init__(self,ip,user,psd):
		# try:
		self.ssh=SSHClient()
		self.ssh.load_system_host_keys()
		print('init setting')
		self.ssh.connect(ip,port=22,username=user,password=psd)
		print('Connection successful')
		self.client=self.ssh.get_transport()
		# except:
		# 	print('Connection fail')
	def squeue(self):
		stdin,stdout,stderr = self.ssh.exec_command('squeue')
		out=stdout.read()
		outtemp=str(out)
		lines=outtemp.count('\\n')
		stdin,stdout,stderr = self.ssh.exec_command('squeue')
		outline=list()
		for i in range(lines):
			line_temp=stdout.readline()
			line_temp=str(line_temp)
			line_temp=line_temp.replace('\n','')
			outline.append(line_temp.split())
		print(outline)
		return outline

	def email_set(self,user,psd,smpt_server,port,target,test_mail=False):
		
		server = smtplib.SMTP(smpt_server,port)
		server.ehlo()
		# server.set_debuglevel(1)
		server.starttls()
		server.login(user,psd)
		if(test_mail==True):
			msg = MIMEMultipart()
			msg['From'] = 'LIGGGHTSER user'+str(user)
			# msg['To'] =  COMMASPACE.join(target)
			msg['To'] =  target
			msg['Subject'] ='Test mail'
			msg_text= MIMEText('This is a test mail from LIGGGHTSER. Mail set successfully','html','utf-8')
			msg.attach(msg_text)
			server.sendmail(user,[target],msg.as_string())
		self.user=user
		self.target=target
		return server

	def monitor(self,jobid=None,time_gap=60,email=None,file=None):
		squeue_data=self.squeue()
		check_list=[0 for i in range(len(jobid))]
		while 1:
			pass
			for i in range(len(jobid)):
				for j in range(len(squeue_data)):
					# print(jobid[i])
					# print(squeue_data[j][0])
					if(str(jobid[i])==squeue_data[j][0]):
						check_list[i]=1
						break
			for i in range(len(check_list)):
				if(check_list[i]):
					check_list[i]=0
				elif(email):
					msg = MIMEMultipart()
					msg['From'] = 'LIGGGHTSER user'+str(self.user)
					# msg['To'] =  COMMASPACE.join(target)
					msg['To'] =  self.target
					msg['Subject'] ='Job info mail'
					msg_text= MIMEText('Job '+str(jobid[i])+' down.','html','utf-8')
					msg.attach(msg_text)
					if(file):
						pass
					email.sendmail(self.user,[self.target],msg.as_string())
					del jobid[i]
				else:
					print('Job'+str(jobid[i])+'down.')
					del jobid[i]
			# print(jobid)
			if(len(jobid)==0):
				msg = MIMEMultipart()
				msg['From'] = 'LIGGGHTSER user'+str(self.user)
				# msg['To'] =  COMMASPACE.join(target)
				msg['To'] =  self.target
				msg['Subject'] ='Job info mail'
				msg_text= MIMEText('Jobs all down.','html','utf-8')
				msg.attach(msg_text)
				break
			time.sleep(time_gap)
