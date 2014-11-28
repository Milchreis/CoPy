import shutil
import gui
import os
import fnmatch

ADD_SOURCE="add"
REMOVE_SOURCE="rem_src"
REMOVE_ALL_SOURCES="rem"
DESTINATION="dest"
BACKUP="backup"


class AppController():
    
    def __init__(self):
        
        self.appmodel = AppModel()
        self.view = gui.MainWindow(None, -1, "")
        self.view.setNotifyHook(self.handleEvent)
        
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
            print self.appmodel.getNumberOfFiles()
            self.appmodel.backup()
        
        
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

    def __walk(self, root='.', recurse=True, pattern='*'):
        for path, _, files in os.walk(root):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                if not recurse:
                    break
  
    def backup(self):
        
        for e in self.sources:
            for fspec in self.__walk(e):
                curFile = fspec[len(e)+1:]
                destFile = os.path.join(self.destination, curFile)
                
                if os.path.isfile(destFile):
                    lastModDest = os.path.getmtime(destFile)
                    lastModOrg  = os.path.getmtime(fspec)
                    
                    delta = lastModOrg - lastModDest

                    if delta >= 0:
                        shutil.copyfile(fspec, destFile)
                        print "copied: " + destFile
                else:
                    dirname = os.path.dirname(destFile)
                    if not os.path.exists(dirname):
                        os.makedirs(dirname)
                        print "made dir " + dirname
                        
                    shutil.copy2(fspec, destFile)
                    print "first copied " + destFile
                    
                
                