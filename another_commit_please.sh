#!/bin/bash

touch yadda.out
echo "yadda" >> yadda.out
git add yadda.out
random_string=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
git commit -m "randmon string for commit message $random_string"
git push 
