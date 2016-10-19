# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyQBSpider
###########################################################################

class MyQBSpider ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 14, 74, 90, 90, False, "宋体" ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text_Story = wx.TextCtrl( self, wx.ID_ANY, u"欢迎使用糗百文字版，按任意键开始查看段子\nHave Fun ! ^_^", wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH|wx.NO_BORDER )
		self.Text_Story.SetFont( wx.Font( 13, 70, 90, 90, False, "宋体" ) )
		self.Text_Story.SetBackgroundColour( wx.Colour( 231, 231, 231 ) )
		
		bSizer2.Add( self.Text_Story, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 4, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Text_Story.Bind( wx.EVT_KEY_DOWN, self.on_btn_read_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_btn_read_click( self, event ):
		event.Skip()
	

