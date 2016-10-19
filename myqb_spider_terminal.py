# -*- coding: utf-8 -*-

import bs4
from bs4 import BeautifulSoup
import re
import sys
import urllib2
import urllib
import requests

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class myqb_spider:

	'''
	初始化相关变量
	'''
	def __init__(self):
		self.header={ 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		self.indexpage = 0
		self.initurl = 'http://www.qiushibaike.com/text/page/'
		self.stories=[]
		self.enable=False

	'''
	使用urllib2读取网页内容
	'''
	def gethtml(self,page):
		dsturl=self.initurl+str(page)
		req =urllib2.Request(dsturl,headers=self.header)
		res=urllib2.urlopen(req)
		content = res.read().decode('utf-8')
		return content   

	'''
	使用Beautifulsoup解析段子
	'''
	def getstories(self):
		if len(self.stories)==0:			
			pagecontent=self.gethtml(self.indexpage)			
			if not pagecontent:
				print u'获取内容失败'
			soup=BeautifulSoup(pagecontent,'html.parser')	
			#将下一页所有的段子放到全局段子数组中，用extend可以增加一个列表的内容，append只能增加一个元素
			self.stories.extend(soup.find_all('div',class_='article block untagged mb15'))

	'''
	读取键盘输入决定是否输出下一条段子
	'''
	def getnextsotry(self):		
		inputa='9'			
		while inputa != '' and inputa != 'Q':
			inputa=raw_input()		
			inputa=inputa.upper()
			if inputa =='':				
				self.enable=True	
				return		
			elif inputa=='Q':
				self.enable=False
				self.stories=[]
			else:
				print u'请正确输入'

	'''
	启动爬虫
	'''
	def startspider(self):
		print  u'正在浏览糗百文字版，请按回车键读取下一条，按Q键停止浏览'

		self.enable=True
		self.indexpage=1		
		while self.enable:					
			self.printstory()
			

	'''
	输出段子,每次输出一条，按回车键输出下一条
	'''
	def printstory(self):
		
		self.getstories()	
		num=0;
		while len(self.stories)>0:
			aa=self.stories[0]			
			num+=1	
			print u'第 %d 页 - 第 %d 条\r\n' %(self.indexpage,num	)	
			#文章状态
			stat = aa.find('div',class_='stats')

			#好笑数
			smile = stat.find('span',class_='stats-vote')			
			smile_stat=smile.get_text().encode('utf-8')				
			
			#评论数						
			discus=stat.find('span',class_='stats-comments')			
			discus_stat=discus.get_text().encode('utf-8')
			#去掉字符串中的空格换行回车等
			print  u'作者:%s'% aa.div.h2.string, ''.join(smile_stat.split()),''.join(discus_stat.split())
						
			#输出文章
			content=aa.find('div',class_='content')
			for text in content:	
				if text.string !=None:
					a=text.string.encode('utf-8')
					print ''.join(a.split())+'\r\n'	

			#删除已经输出的段子
			del self.stories[0]			
			 
			# 每次输出一条，回车阅读下一条
			self.getnextsotry()
		self.indexpage+=1
			

			


if __name__ == '__main__':
	spider=myqb_spider()
	spider.startspider()