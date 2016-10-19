# -*- coding: utf-8 -*-

import qbspiderui
import wx
from myqb_spider_ui_ver import QB_Spider


class mainwindow(qbspiderui.MyQBSpider):

	def _init_main_window(self):
		
		self.spider=QB_Spider()	
		self.spider.startspider()	

	def on_btn_read_click( self, event ):	

		self.Text_Story.Clear()
		self.spider.printstory()			
		self.Text_Story.SetValue(self.spider.nowpage+self.spider.author+self.spider.smile+self.spider.dis+self.spider.onestory)
			
	
def main():		
	app=wx.App()
	main_win=mainwindow(None)
	main_win._init_main_window()
	main_win.Show()
	app.MainLoop()

if __name__ == '__main__':
	main()
