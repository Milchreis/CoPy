pyinstaller-2.0/pyinstaller.py -F -m manifest.xml -n CoPy -w -o ../bin/ CoPy.spec
cp ./dist/CoPy ../bin/CoPy

rm -r ./build
rm -r ./dist