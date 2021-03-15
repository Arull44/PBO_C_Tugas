# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class tampilan_awal
###########################################################################

class tampilan_awal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 450,380 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"HELLO WX" ), wx.VERTICAL )

		self.welcome = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Welcome, Aula Fajrun Khalilurahman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.welcome.Wrap( -1 )

		self.welcome.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		sbSizer3.Add( self.welcome, 0, wx.ALL, 5 )

		self.nim = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"192410101044", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nim.Wrap( -1 )

		self.nim.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.nim, 0, wx.ALL, 5 )

		self.dataAkun = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Lengkapi Data Akun!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataAkun.Wrap( -1 )

		sbSizer3.Add( self.dataAkun, 0, wx.ALL, 5 )

		self.m_panel1 = wx.Panel( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.email = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )

		fgSizer1.Add( self.email, 0, wx.ALL, 5 )

		self.text_email = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.text_email, 0, wx.ALL, 5 )

		self.usia = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usia.Wrap( -1 )

		fgSizer1.Add( self.usia, 0, wx.ALL, 5 )

		self.text_usia = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer1.Add( self.text_usia, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		fgSizer1.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer1.Add( self.m_staticText25, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.btn_male = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Laki-laki", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btn_male, 0, wx.ALL, 5 )

		self.btn_female = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Perempuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btn_female, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		sbSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Save = wx.Button( sbSizer3.GetStaticBox(), wx.ID_SAVE )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
		self.m_sdbSizer1Cancel = wx.Button( sbSizer3.GetStaticBox(), wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		sbSizer3.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnCancelButtonClick )
		self.m_sdbSizer1Save.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_sdbSizer1OnCancelButtonClick( self, event ):
		event.Skip()

	def m_sdbSizer1OnSaveButtonClick( self, event ):
		event.Skip()


