#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# from cStringIO import StringIO
class pdfreader:
	def init(self):
		pass
	def pdf_converter_PYPDF(self,path):
		import PyPDF2
		pdfFileObj = open(path, 'rb') 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
		author=PyPDF2.DocumentInformation().author
		# print(pdfReader.numPages) 
		self.str=list()
		for i in pdfReader.numPages:
			pageObj = pdfReader.getPage(i) 
			str_temp=pageObj.extractText()
			self.str=self.str+str_temp
		print(self.str) 
		pdfFileObj.close() 
	def pdf_converter(self,path):
		# rsrcmgr = PDFResourceManager()
		# retstr = StringIO()
		# codec = 'utf-8'
		# laparams = LAParams()
		# device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		# fp = file(path, 'rb')
		# interpreter = PDFPageInterpreter(rsrcmgr, device)
		# password = ""
		# maxpages = 0
		# caching = True
		# pagenos=set()
		# for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
		# 	interpreter.process_page(page)
		# fp.close()
		# device.close()
		# self.str = retstr.getvalue()
		# retstr.close()
	def write_txt(self,save_name):
		try:
			with open("%s"%save_name,"w") as f:#格式化字符串还能这么用！
				for i in str:
					f.write(i)
			print (save_name+" Writing Succeed!")
		except:
			print ("Writing Failed!")
	def give_str(self):
		return self.str

p=pdfreader()
p.pdf_converter('./test.pdf')
print(p.give_str())
# convert_pdf_to_txt('C:\\pdfminer-master\\chapter1.pdf',"c.txt")
