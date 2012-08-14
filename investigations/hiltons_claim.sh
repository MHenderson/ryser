#!/bin/bash

a=1
b=$((2**34+1))
k=$SGE_TASK_LAST
d=$((b-a))
s=$((d/k))
j=$SGE_TASK_ID

#echo $a
#echo $b
#echo $k
#echo $s
#echo $j

command="python /work/work6/pmzmh/investigations/bin/is_hall_on_interval"

source /work/work6/pmzmh/bin/ENV/bin/activate
echo $command $((a+(j-1)*s)) $((a+(j)*s-1))

