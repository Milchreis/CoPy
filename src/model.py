import os
import gui
import tools


ADD_SOURCE="add"
REMOVE_SOURCE="rem_src"
REMOVE_ALL_SOURCES="rem"
DESTINATION="dest"
BACKUP="backup"


class AppController():
    
    def __init__(self):
        
        session = os.path.join(os.path.expanduser("~"), ".copySession")
        
        self.appmodel = AppModel(session)
        self.view = gui.MainWindow(None, -1, "")
        self.view.setNotifyHook(self.handleEvent)
        self.waitview = gui.WaitDialog(self.view)
        
        # read session file
        if os.path.exists(session):
            files = tools.readIn(session)
            
            if(len(files) >= 2):
                self.appmodel.destination = files[0]
                self.appmodel.setSource(files[1:])
                    
            self.view.update(self.appmodel)
    
            
    def handleEvent(self, message):
        
        if message[0] == ADD_SOURCE:
            self.appmodel.addSource(message[1])
        
        if message[0] == REMOVE_SOURCE:
            self.appmodel.removeSource(message[1])
        
        if message[0] == REMOVE_ALL_SOURCES:
            self.appmodel.sources = []
        
        if message[0] == DESTINATION:
            self.appmodel.destination = message[1]

        if message[0] == BACKUP:
            
            self.waitview = gui.WaitDialog(self.view)
            po = tools.ParallelOperation(self.appmodel.backup, self.waitview.updateView)
            po.start()

            self.waitview.ShowModal()
            self.waitview.Destroy()  
            
        
        self.view.update(self.appmodel)


class AppModel():
    
    def __init__(self, session=None):
        
        self.sources = []
        self.destination = None
        self.session = session
        
        self.__val = 0
        self.__updateCallback = None
    
    def setSource(self, array):
        for e in array:
            self.addSource(e)

    
    def addSource(self, src):
        if(not src in self.sources):
            self.sources.append(src)
    
    
    def removeSource(self, src):
        if(src in self.sources):
            self.sources.remove(src)


    def __backupupdate(self):
        self.__val += 1
        
        if not self.__updateCallback == None:
            self.__updateCallback(['num', self.__val])
        
  
    def backup(self, updateCallback=None):
        
        # write session file
        if not self.session == None:
            save = []
            save.append(self.destination)
            save.extend(self.sources)
            tools.writeOut(self.session, save)

        if not updateCallback == None:
            self.__updateCallback = updateCallback
            
            # Calculate number of files
            numbers = tools.getNumberFiles(self.sources)
            updateCallback(["max", numbers])
            
            for e in self.sources:
                tools.backupfiles(e, self.destination, self.__backupupdate)

            updateCallback(["end"])
            self.__val = 0

                    
                