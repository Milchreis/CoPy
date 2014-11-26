import gui

class AppController():
    
    def __init__(self):
        
        self.appmodel = AppModel()
        self.view = gui.MainWindow(None, -1, "")
        self.view.setNotifyHook(self.handleEvent)
        
    def handleEvent(self, message):
        
        if message[0] == 'add':
            self.appmodel.addSource(message[1])
        
        if message[0] == 'destination':
            self.appmodel.destination = message[1]
        
        print message
        
        self.view.update(self.appmodel)


class AppModel():
    
    def __init__(self):
        
        self.sources = []
        self.destination = None
    
    
    def addSource(self, src):
        if(not src in self.sources):
            self.sources.append(src)
    
    
    def removeSource(self, src):
        if(src in self.sources):
            self.sources.remove(src)