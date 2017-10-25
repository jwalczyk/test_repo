#!/bin/bash
random_string=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

git checkout -b branch-$random_string

touch yadda-$random_string.out
echo "yadda" >> yadda-$random_string.out
git add yadda-$random_string.out
git commit -m "randmon string for commit message $random_string"
git push origin branch-$random_string 
