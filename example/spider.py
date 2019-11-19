# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time

class downloader(object):
    def __init__(self):
        # self.server='http://www.jjwxc.net/'
        # self.target='http://www.jjwxc.net/onebook.php?novelid=2221448'
        self.target='https://m.lewenxiaoshuo.com/books/chenghuashisinian/'
        self.read_content()
        for i in range(len(self.texts)):
            self.read_url(i)
            self.read_text()
            time.sleep(2)
            # print(len(self.texts))

    def read_content(self):
        req = requests.get(url=self.target)
        content=req.text.encode('ISO-8859-1','ignore').decode('GB18030','ignore')
        # print(content)
        html = content
        bf = BeautifulSoup(html)
        # texts = bf.find_all('table', class_="cytable") 
        # self.texts = bf.find_all('tr',itemprop='chapter')# jinjiangwenxue
        self.texts = bf.find_all('div',class_='box')
        temp=BeautifulSoup(str(self.texts))
        self.texts=temp.find_all('li')

    def read_url(self,i):
        a_bf = BeautifulSoup(str(self.texts[i]))
        a = a_bf.find_all('a')
        for each in a:
          print(each.string, each.get('href'))
        self.filename=each.string
        self.url=each.get('href')

    def read_text(self):
        # target = 'https://m.lewenxiaoshuo.com/books/chenghuashisinian/11823888.html'
        req = requests.get(url=self.url)
        content=req.text.encode('gbk').decode('GB18030','ignore')
        html = content
        bf = BeautifulSoup(html)
        # texts = bf.find_all('div', class_ = 'noveltext') 
        texts = bf.find_all('div', id = 'content') 
        strs=texts[0].text
        strs = re.sub('[!"#$%&\'()*+-/<=>?@?★、【】《》[\\]^_`{|}~\s]+', "\n",strs)
        testtext=strs
        with open(r'D:\ETH\\test\test.txt',"a",encoding='gbk') as f:
            f.write('\n\n\n\n第'+self.filename+'章'+'\n\n'+testtext)

p=downloader()