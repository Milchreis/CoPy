import model
import wx
import logging
import optparse
import os

def fake(arg):
    pass

if __name__ == '__main__':
    
    # Set up the logger
    # ============================================================
    logger = logging.getLogger('copy')
    logger.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(ch)
    
    # Set up the logger
    # ============================================================
    parser = optparse.OptionParser('usage: CoPy <Sessionfile>')
    (options, args) = parser.parse_args()
    
    if len(args) == 0:
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
    
        copyapp = model.AppController()
        app.SetTopWindow(copyapp.view)
        
        copyapp.view.Show()
        app.MainLoop()
    
    else:
        if not os.path.exists(args[0]):
            raise ValueError("The given file does not exists")
        
        app = model.AppModel(args[0])
        app.backup(fake)