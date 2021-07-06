#!/bin/bash

mraa-gpio list
for ((i=1; i<27; i++))
do
	mraa-gpio get $i 
done
