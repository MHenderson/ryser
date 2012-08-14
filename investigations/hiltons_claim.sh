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

command="is_hall_on_interval"

echo $command $((a+(j-1)*s)) $((a+(j)*s-1))

