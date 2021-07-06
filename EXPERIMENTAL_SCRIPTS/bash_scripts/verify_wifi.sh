#!/bin/bash

# eseguire da sudo

conn=$(nmcli --terse d wifi | grep "*:")

IFS=':'
read -ra ADDR <<< $conn
connected_to=${ADDR[1]}

if [ $# != 2  ]; then
    echo Yout must provice ssid and password
    exit 1
fi

if [ "$connected_to" = "$1" ]; then
    echo sei gia connesso "(${ADDR[1]})"
else
    nmcli r wifi on
    nmcli d wifi connect $1 password $2
fi


