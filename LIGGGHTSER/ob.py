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
		self.ssh.close()
		self.ip=ip
		self.user=user
		self.psd=psd
		
	def reconnect(self):
		self.ssh=SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.connect(self.ip,port=22,username=self.user,password=self.psd)
		self.client=self.ssh.get_transport()

	def squeue(self):
		self.reconnect()
		stdin,stdout,stderr = self.ssh.exec_command('squeue')
		out=stdout.read()
		outtemp=str(out)
		lines=outtemp.count('\\n')
		stdin,stdout,stderr = self.ssh.exec_command('squeue')
		outline=list()
		for i in range(lines):
			line_temp=stdout.readline()
			line_temp=str(line_temp)
			# line_temp=line_temp.replace('\n','')
			outline.append(line_temp.split())
			outline[i].append('\n')
		print(outline)
		self.ssh.close()
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
		email=[user,psd,smpt_server,port,target]
		# self.user=user
		# self.target=target
		# self.psd=psd
		# self.smpt_server=smpt_server
		# self.port=port
		return email

	def send_email(self,email,strings):
		server = smtplib.SMTP(email[2],email[3])
		server.ehlo()
		# server.set_debuglevel(1)
		server.starttls()
		server.login(email[0],email[1])

		msg = MIMEMultipart()
		msg['From'] = 'LIGGGHTSER user'+str(email[0])
		# msg['To'] =  COMMASPACE.join(target)
		msg['To'] =  email[4]
		msg['Subject'] ='Job info mail'
		msg_text= MIMEText(strings,'plain','utf-8')
		msg.attach(msg_text)
		server.sendmail(email[0],[email[4]],msg.as_string())

	def monitor(self,jobid=None,time_gap=60,email=None,file=None):
		squeue_data=self.squeue()
		strings=[' '.join(squeue_data[i]) for i in range(len(squeue_data))]
		strings='\n'.join(strings)
		self.send_email(email,strings)
		while 1:
			squeue_data=self.squeue()
			check_list=[0 for i in range(len(jobid))]
			shrink_flag=0
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
					strings='Job '+str(jobid[i])+' down.'
					self.send_email(email,strings)
					if(file):
						pass
					jobid[i]=0
					shrink_flag=1
				else:
					print('Job'+str(jobid[i])+'down.')
					jobid[i]=0
					shrink_flag=1
			if(shrink_flag==1):
				jobid=[x for x in jobid if x!=0]
			if(len(jobid)==0):
				strings='Jobs all down.Monitor terminated'
				self.send_email(email,strings)
				break
			time.sleep(time_gap)
