#!/bin/bash

if [ -d dist ]; then
    rm -rfv dist
fi

python3 setup.py bdist

cd dist

tar -xvf ./ficha*.tar.gz

cp -v -a ./usr ../ficha_0.1_all

cd ..

#Build the DEB package
dpkg -b ficha_0.1_all/
cp -v -a ficha_0.1_all.deb dist

# Build a tar.gz to be install with python3 setup.py install command
python3 setup.py sdist

# Clean
rm -rfv build
rm ficha_0.1_all.deb
cd ficha_0.1_all
rm -rfv usr
cd ../dist
rm -rfv usr
rm ficha-0.1.linux*