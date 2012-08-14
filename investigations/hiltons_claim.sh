#!/bin/bash

a=1
b=$((2**34+1))
k=$1
d=$((b-a))
s=$((d/k))
j=$SGE_TASK_ID

echo this is a line of output # except for this
echo $a
echo $b
echo $k
echo $s
echo $j 

command="program_name"

END=$((k-1))
for ((i=0;i<=END;i++));
do
   echo $command $((a+i*s)) $((a+(i+1)*s-1))
done
