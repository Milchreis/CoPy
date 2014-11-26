import model
import wx
import logging

if __name__ == '__main__':
    
    # Set up the logger
    # ============================================================
    logger = logging.getLogger('copy')
    logger.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(ch)
    
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()

    copyapp = model.AppController()
    app.SetTopWindow(copyapp.view)
    
    copyapp.view.Show()
    app.MainLoop()