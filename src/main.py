import wx
import gui

if __name__ == '__main__':
      
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    mainWindow = gui.MainWindow(None, -1, "")
    app.SetTopWindow(mainWindow)
    mainWindow.Show()
    app.MainLoop()