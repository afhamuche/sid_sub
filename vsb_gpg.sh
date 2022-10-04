#!/bin/bash

./vsb31

n=0
today="`date +%Y%m%d`"
logtxt="log.txt"
oldlog="old_log/"
newlog="log_$today-$n.gpg"

cd $oldlog
while [[ -f $newlog ]];
do
	newlog="log_$today-$n.gpg"
	n=$(( n + 1 ))
done
cd ..

gpg -o $newlog -c $logtxt
mv $newlog $oldlog
echo $logtxt > $logtxt
