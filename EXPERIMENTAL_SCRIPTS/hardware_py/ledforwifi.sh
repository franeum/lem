#!/usr/bin/env bash


response=`LANG=C nmcli -g DEVICE,STATE d status | grep -E "p2p0|wlan0" | cut -f2 -d:`
datum=0

for x in ${response[@]}; do
	if [[ $x == connected ]]; then
		datum+=1
	fi
done

if (( $datum > 0 )); then
	mraa-gpio set 21 1
	echo connected
	exit 0
else
	mraa-gpio set 21 0
	echo disconnected 
	exit 1
fi 
