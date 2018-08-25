#!/bin/bash

for i in $(find /usr -path "*ficha*"); do
	rm -rfv $i
done


