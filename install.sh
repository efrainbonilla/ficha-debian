#!/bin/bash


depends="python3"

for dep in $depends
do
    if ! dpkg-query -l "$dep" | grep "ii" &> /dev/null
    then
        apt-get install "$dep"
    fi
done

python3 setup.py install
