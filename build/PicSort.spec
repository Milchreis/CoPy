# -*- mode: python -*-

# get all build in plugins
def getPluginList(directory):
  import os
  arr = []
  for f in os.listdir(directory):
    arr.append(('plugins/'+f, directory+f,'DATA'))
  return arr

a = Analysis(['../src/main.py'],
             pathex=['build'],
             hiddenimports=[],
             hookspath=None)

dataList = getPluginList('../src/plugins/')
dataList.insert(0, ('res/logo.png', '../src/res/logo.png', 'DATA'))

a.datas += dataList

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'PicSort'),
          debug=False,
          strip=None,
          upx=True,
          console=True , manifest='manifest.xml')
          #icon=r'imgs/icon.ico')
app = BUNDLE(exe, name=os.path.join('dist', 'PicSort.app'))