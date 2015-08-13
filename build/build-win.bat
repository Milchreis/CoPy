pyinstaller-2.0\pyinstaller.py -F -m manifest.xml -n PicSort -w -o ..\bin\ PicSort.spec
copy dist\PicSort ..\bin\PicSort

RMDIR /S build /Q
RMDIR /S dist /Q