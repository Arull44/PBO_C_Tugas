import wx
from noname import tampilan_awal

class home(tampilan_awal):
    def __init__(self, parent):
        tampilan_awal.__init__(self, parent)
        self.SetIcon(wx.Icon('pesan.ico'))
        self.SetTitle('Program Hello WX')
        
app = wx.App()
homeland = home(parent=None)
homeland.Show()
app.MainLoop()