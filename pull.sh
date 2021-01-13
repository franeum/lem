#!/usr/bin/env bash

echo Pulling Main Repository
git pull

for d in ROCKPIS-*; do
	echo "Pulling ${d}"
	cd $d
    git checkout main
	git pull origin main
	cd .. 
done
