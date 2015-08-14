pyinstaller-2.0\pyinstaller.py -F -m manifest.xml -n CoPy -w -o ..\bin\ CoPy.spec
copy dist\CoPy ..\bin\CoPy

RMDIR /S build /Q
RMDIR /S dist /Q