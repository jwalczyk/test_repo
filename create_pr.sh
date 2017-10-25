#!/bin/bash
random_string=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

git checkout -b branch-$random_string

touch yadda-$random_string.out
echo "yadda" >> yadda-$random_string.out
git add yadda-$random_string.out
git commit -m "random string for commit message $random_string"
git push origin branch-$random_string 
git checkout master

curl -X POST \
  https://api.github.com/repos/jwalczyk/test_repo/pulls \
  -H 'authorization: token b027811325490aa1c77c830e7736b074ded96e7f' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "title": "pr_for_branch-'"$random_string"'",
  "head": "branch-'"$random_string"'",
  "base": "master"
}'

