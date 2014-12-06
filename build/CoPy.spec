# -*- mode: python -*-
a = Analysis(['../src/main.py'],
             pathex=['build'],
             hiddenimports=[],
             hookspath=None)

a.datas += [('imgs/logo.png', '../src/imgs/logo.png','DATA')]
 

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'CoPy'),
          debug=False,
          strip=None,
          upx=True,
          console=True , manifest='manifest.xml')
app = BUNDLE(exe,
             name=os.path.join('dist', 'CoPy.app'))
