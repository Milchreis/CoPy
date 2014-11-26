import wx
import lang
import main

class HeadPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent

        self.SetBackgroundColour((11, 11, 11))


class SourcePanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent
    
        self.sourclist = wx.ListBox(self, 500)
        self.Bind(wx.EVT_LISTBOX, self.onSelect, id = 500)
        
        self.addSource = wx.Button(self, -1, lang.BUTTON_ADD_SOURCE)
        self.addSource.Bind(wx.EVT_BUTTON, self.onAddSource)
        
        self.removeSource = wx.Button(self, -1, lang.BUTTON_REMOVE_SOURCE)
        self.removeSource.Bind(wx.EVT_BUTTON, self.onRemoveSource)
        
        self.removeAll = wx.Button(self, -1, lang.BUTTON_REMOVE_ALL)
        self.removeAll.Bind(wx.EVT_BUTTON, self.onRemoveAll)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.addSource,    0, wx.EXPAND | wx.BOTTOM, 5)
        vbox.Add(self.removeSource, 0, wx.EXPAND | wx.BOTTOM, 5)
        vbox.Add(self.removeAll,    0, wx.EXPAND | wx.BOTTOM, 5)
        
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.sourclist,    2, wx.EXPAND | wx.ALL, 5)
        hbox.Add(vbox,              2, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(hbox)
        
        
    def updateList(self, list):
        self.sourclist.Clear()
        
        for e in list:
            self.sourclist.Append(e)


    def onRemoveAll(self, e):
        pass


    def onAddSource(self, e):
        
        path = ""
        dlg = wx.DirDialog(self, message=lang.DIALOG_CHOOSE_DIRECTORY,  defaultPath='')
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.parent.notify(['add', path])
            

    def onRemoveSource(self, e):
        pass

    def onSelect(self, e):
        pass


class DestinationPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent
        
        self.setDestination = wx.Button(self, -1, lang.BUTTON_SET_DESTINATION)
        self.setDestination.Bind(wx.EVT_BUTTON, self.onSetDestination)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.setDestination, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(vbox)
        
    def updateDestinationButton(self, path):
        
        if not path == "" or not path == None:
            self.setDestination.SetLabel(lang.LABEL_TARGET+" "+path)
        else:
            self.setDestination.SetLabel(lang.BUTTON_SET_DESTINATION)
            
    
    def onSetDestination(self, e):
        path = ""
        dlg = wx.DirDialog(self, message=lang.DIALOG_CHOOSE_DIRECTORY,  defaultPath='')
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.parent.notify(['destination', path])
            
            


class BackupPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent
        
        self.backup = wx.Button(self, -1, lang.BUTTON_BACKUP)
        self.backup.Bind(wx.EVT_BUTTON, self.onBackup)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.backup, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(vbox)
        
    def onBackup(self, e):
        pass
    

class MainWindow(wx.Frame):
    
    def __init__(self, *args, **kwds):

        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.notifyHook = None
        
        self.SetTitle("CoPy - Backup")
        self.SetSize((480, 400))
        
        self.headpanel          = HeadPanel(self)
        self.sourcepanel        = SourcePanel(self)
        self.destinationpanel   = DestinationPanel(self)
        self.backuppanel        = BackupPanel(self)
        
        self.initUI()
        
   
    def setNotifyHook(self, callback):
        self.notifyHook = callback


    def initUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.headpanel, 1, wx.EXPAND | wx.ALL, 0)
        vbox.Add(self.sourcepanel, 2, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.destinationpanel, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.backuppanel, 0, wx.EXPAND | wx.ALL, 10)
        
        self.SetSizer(vbox)

    def update(self, model):
        self.sourcepanel.updateList(model.sources)
        self.destinationpanel.updateDestinationButton(model.destination)
    
    def notify(self, message):
        if not self.notifyHook == None:
            self.notifyHook(message) 


