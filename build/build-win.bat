del "..\bin\imgs" /Q

pyinstaller-2.0\pyinstaller.py -F -m manifest.xml -n CoPy -w -o ..\bin\ ..\src\main.py
copy ..\bin\dist\CoPy.exe ..\bin\CoPy.exe
del "..\bin\CoPy.spec" /Q

RMDIR /S ..\bin\build /Q
RMDIR /S ..\bin\dist /Q

md ..\bin\imgs
copy ..\src\imgs\logo.png ..\bin\imgs\logo.png
