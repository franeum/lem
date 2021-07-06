#!/usr/bin/env bash

for i in ROCKPIS-*; do
    cd ${i}
    name=`git remote -v | grep push | grep -Eo "franeum/[^/].+\.git"`
    #echo ${name}
    git checkout main
    git remote set-url origin git@github.com:${name}
    cd ..
done
