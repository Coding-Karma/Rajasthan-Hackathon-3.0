#!/bin/bash
trap "exit" INT
i="0"
while [ $i -lt 100 ]
do
read -p "Please Enter a Message: `echo $'\n> '`" test
echo "The text you want converted is:" \ $test
.google-translate-python/translate-cli -t es -f en $test
i=$[$i+1]
done
