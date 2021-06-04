#!/bin/bash          
pwd=$(pwd)
qmake-qt5 -project
sed -i '7 a QT += gui widgets' *.pro
qmake-qt5
make
re="\w+$"
if [[ $pwd =~ $re ]]; then
    exe=${BASH_REMATCH[0]}
fi
./$exe
