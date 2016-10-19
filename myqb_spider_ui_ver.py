# -*- coding: utf-8 -*-

import bs4
from bs4 import BeautifulSoup
import re
import sys
import urllib2
import urllib
import requests
import string

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class QB_Spider:

	'''
	初始化一些需要用到的数据
	'''
	def __init__(self):
		self.header={ 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		self.indexpage = 1
		self.initurl = 'http://www.qiushibaike.com/text/page/'
		self.stories=[]
		self.enable=False
		self.onestory=''
		self.author=''
		self.smile=''
		self.dis=''
		self.nowpage=''
		self.indexstory=0

	'''
	使用urllib2打开网页并得到网页内容
	'''
	def gethtml(self,page):
		dsturl=self.initurl+str(page)
		req =urllib2.Request(dsturl,headers=self.header)
		res=urllib2.urlopen(req)
		content = res.read().decode('utf-8')
		return content   

	'''
	利用beautifulsoup解析网页，得到段子列表
	'''
	def getstories(self):
					
		pagecontent=self.gethtml(self.indexpage)			
		if not pagecontent:
			print u'获取内容失败'
		soup=BeautifulSoup(pagecontent,'html.parser')	
		#将下一页所有的段子放到全局段子数组中，用extend可以增加一个列表的内容，append只能增加一个元素
		self.stories.extend(soup.find_all('div',class_='article block untagged mb15'))
	
	'''
	启动爬虫
	'''
	def startspider(self):
		#print  u'正在浏览糗百文字版，请按回车键读取下一条，按Q键停止浏览'

		self.enable=True
		self.indexpage=1		
		if self.enable:					
			self.getstories()
			
	'''
	输出段子
	'''
	def printstory(self):

		currentpage=0
		currentstory=0
		if len(self.stories)<5:
			#print u'段子数为0，读取下一页\r\n'
			self.indexpage+=1
			self.getstories()			
			self.indexstory=0

		if len(self.stories):
			aa=self.stories[0]	

			self.indexstory+=1
			self.nowpage=u'第 %d 页 第 %d 条 ' % (self.indexpage,self.indexstory)

			#文章状态
			stat = aa.find('div',class_='stats')			

			#好笑数
			smile = stat.find('span',class_='stats-vote')			
			smile_stat=smile.get_text()			
			self.smile=''.join(smile_stat.split())

			#评论数						
			discus=stat.find('span',class_='stats-comments')			
			discus_stat=discus.get_text()
			self.dis=''.join(discus_stat.split())+'\r\n\r\n'

			#去掉字符串中的空格换行回车等
			#print  u'作者:%s'% aa.div.h2.string, ''.join(smile_stat.split()),''.join(discus_stat.split())
			#作者
			self.author=u'作者: '+aa.div.h2.string+'--'	

			#输出段子
			content=aa.find('div',class_='content')
			a=''
			for text in content:	
				if text.string !=None:
					a+=text.string					
					#print ''.join(b.split())+'\r\n'					
					self.onestory=''.join(a.split())+'\r\n'

			#删除已经输出的段子
			del self.stories[0]				 
			
		
		



if __name__ == '__main__':
	spider=QB_Spider()
	spider.startspider()
