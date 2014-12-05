import os
import fnmatch
import shutil
import threading

def readIn(filepath):
    arr = []
    with open(filepath) as f:
        for line in f:
            arr.append(line.rstrip())
    return arr
            
            
def writeOut(filepath, arr):
    f = open(filepath, "w")
    for e in arr:
        f.write(e + "\n")
    f.close()
    

def __walk(root='.', recurse=True, pattern='*'):
    for path, _, files in os.walk(root):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)
            if not recurse:
                break

def getNumberFiles(patharray):
    counter = 0
    for path in patharray:
        for _ in __walk(path):
            counter += 1
      
    return counter


def backupfiles(path, destination, updatecallback=None):
        
    for fspec in __walk(path):
        curFile = fspec[len(path)+1:]
        
        lastSep = path.rfind(os.sep)
        prefix = path[lastSep+1:]
        destFile = os.path.join(destination, prefix)
        destFile = os.path.join(destFile, curFile)
        
        if os.path.isfile(destFile):
            if os.stat(fspec).st_mtime - os.stat(destFile).st_mtime > 1:
                shutil.copy2 (fspec, destFile)
                print "copied: " + destFile
        else:
            dirname = os.path.dirname(destFile)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
                print "made dir " + dirname
                
            shutil.copy2(fspec, destFile)
            print "first copied " + destFile
        
        if not updatecallback == None:
            updatecallback()


class ParallelOperation(threading.Thread):
    '''
    The ParallelOperation is based on the Thread class and runs
    function pointer in a new thread. Moreover it is possible to
    define listeners for before and after the main execution.
    '''
    def __init__(self, operation, *opArgs):
        threading.Thread.__init__(self)
        self._before = None;
        self._beforeArgs = None;
        
        self._update = None;
        
        self._after = None;
        self._afterArgs = None
        
        self._op = operation;
        self._opArgs = opArgs;

    def setBeforeFunc(self, beforeFunc, *args):
        self._before = beforeFunc;
        self._beforeArgs = args;

    def setUpdateFunc(self, updateFunc):
        self._update = updateFunc;

    def setAfterFunc(self, afterFunc, *args):
        self._after = afterFunc;
        self._afterArgs = args;

    def run(self):
        if(not(self._before == None)):
            self._before(*self._beforeArgs)
        
        val = self._op(*self._opArgs)
        
        if not self._update == None:
            self._update(val)

        if(not(self._after == None)):
            self._after(*self._afterArgs)
        
        return val

