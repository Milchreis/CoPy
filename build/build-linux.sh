pyinstaller-2.0/pyinstaller.py -F -m manifest.xml -n PicSort -w -o ../bin/ PicSort.spec
cp ./dist/PicSort ../bin/PicSort

rm -r ./build
rm -r ./dist