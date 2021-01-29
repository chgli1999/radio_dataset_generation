#!/bin/bash
rm -rf raw/
mkdir raw/
num=0
t='2'
while true
do
# use usrp capture radio wave
s=`python rx_to_file.py -c 1.982e9 -r 40e6`

if [ $s -eq $t ]
then
break
fi

num=`expr $num + 1`
echo $num
done

# matlab to trans the raws to pics

mkdir amplitude
mkdir phase
matlab -nodesktop -nosplash -r 'parse;quit;'
