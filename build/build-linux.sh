rm -r ../bin/imgs

pyinstaller-2.0/pyinstaller.py -F -m manifest.xml -n CoPy -w -o ../bin/ ../src/main.py
cp ../bin/dist/CoPy ../bin/CoPy
rm ../bin/CoPy.spec

rm -r ../bin/build
rm -r ../bin/dist

mkdir ../bin/imgs
cp ../src/imgs/logo.png ../bin/imgs/logo.png