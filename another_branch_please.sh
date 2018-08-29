#!/bin/bash
if [ "$#" -ne 1 ]
  then
    echo "usage:    `basename $0`  <number_of_new_commits>"
    exit 1
fi
random_string=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
loop=$1
git checkout -b branch-$random_string
if [ "$loop" -ge 1  ]; then 
   COUNTER=0
   while [[ $COUNTER -lt $loop ]]; do 
       echo "yadda $1" >> yadda-$random_string.out
       git add yadda-$random_string.out
       git commit -m "randmon string for commit $COUNTER message $random_string"
       let COUNTER=COUNTER+1
   done
fi
git push origin branch-$random_string 
