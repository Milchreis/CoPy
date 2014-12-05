import wx
import lang
import model

class WaitDialog(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(WaitDialog, self).__init__(*args, **kw) 
        self.SetSize((250, 100))
        self.SetTitle(lang.LABEL_WAIT_HEADER)

        self.max = 0
        
        self.label = wx.StaticText(self, label=lang.LABEL_WAIT_HEADER)
        self.gauge = wx.Gauge(self, range=0)
        
        self.stop = wx.Button(self, label=lang.LABEL_CANCEL)
        self.stop.Bind(wx.EVT_BUTTON, self.OnClose)
        
        hbox = wx.BoxSizer(wx.VERTICAL)
        hbox.Add(self.label,    2, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.gauge,    0, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.stop,     0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(hbox)
        
        
    def OnClose(self, e):
        self.Destroy()
        
        
    def updateView(self, param):
        if len(param) > 0:

            if param[0] == "num":
                wx.CallAfter(self.gauge.SetValue, param[1])
                wx.CallAfter(self.label.SetLabel, lang.LABEL_FILE_OF.format(param[1], self.max))
            
            if param[0] == "max":
                wx.CallAfter(self.gauge.SetRange, param[1])
                self.max = param[1]
            
            if param[0] == "end":
                wx.CallAfter(self.SetTitle, lang.LABEL_READY_HEADER)
                wx.CallAfter(self.label.SetLabel, lang.LABEL_FILE_OF.format(self.max, self.max))
                wx.CallAfter(self.stop.SetLabel, lang.LABEL_CLOSE)
    

class HeadPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent

        self.SetBackgroundColour((11, 11, 11))

        img = wx.Image("imgs/logo.png", wx.BITMAP_TYPE_PNG)
        self.bitmap = wx.BitmapFromImage(img)
        
        self.imgPane = wx.StaticBitmap(self, bitmap=self.bitmap)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.imgPane,    0, wx.EXPAND, 0)
        self.SetSizer(vbox)
        

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
        hbox.Add(vbox,              1, wx.ALL, 5)
        
        self.SetSizer(hbox)
        
        
    def updateList(self, listobj):
        self.sourclist.Clear()
        
        for e in listobj:
            self.sourclist.Append(e)


    def onRemoveAll(self, e):
        
        if self.sourclist.GetCount() == 0:
            return
        
        dial = wx.MessageDialog(self.parent, lang.DIALOG_SURE_REMOVE_ALL, 
                        lang.LABEL_REMOVE+"?", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        
        if dial.ShowModal() == wx.ID_YES:
            self.parent.notify([model.REMOVE_ALL_SOURCES])


    def onAddSource(self, e):
        
        path = ""
        dlg = wx.DirDialog(self, message=lang.DIALOG_CHOOSE_DIRECTORY,  defaultPath='')
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.parent.notify([model.ADD_SOURCE, path])
            

    def onRemoveSource(self, e):
        index = self.sourclist.GetSelection()
        entry = self.sourclist.GetString(index)
        self.parent.notify([model.REMOVE_SOURCE, entry])

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
        
        if not path == "" and not path == None:
            self.setDestination.SetLabel(lang.LABEL_TARGET+" "+path)
        else:
            self.setDestination.SetLabel(lang.BUTTON_SET_DESTINATION)
            
    
    def onSetDestination(self, e):
        path = ""
        dlg = wx.DirDialog(self, message=lang.DIALOG_CHOOSE_DIRECTORY,  defaultPath='')
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.parent.notify([model.DESTINATION, path])
            
            


class BackupPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent
              
        self.backup = wx.Button(self, -1, lang.BUTTON_BACKUP)
        self.backup.Bind(wx.EVT_BUTTON, self.onBackup)
        self.backup.Disable()
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.backup, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(vbox)
    
    
    def onBackup(self, e):
        self.parent.notify([model.BACKUP])
    

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
        vbox.Add(self.headpanel, 0, wx.EXPAND | wx.ALL, 0)
        vbox.Add(self.sourcepanel, 2, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.destinationpanel, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.backuppanel, 0, wx.EXPAND | wx.ALL, 10)
        
        self.SetSizer(vbox)

    def setWaitState(self, current, maxValue, enableState):
        self.backuppanel.updateWait(current, maxValue, enableState)


    def update(self, model):
        self.sourcepanel.updateList(model.sources)
        self.destinationpanel.updateDestinationButton(model.destination)
        
        if len(model.sources) > 0 and not model.destination == None:
            self.backuppanel.backup.Enable()
        else:
            self.backuppanel.backup.Disable()
    
    def notify(self, message):
        if not self.notifyHook == None:
            self.notifyHook(message) 


