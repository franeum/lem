#!/usr/bin/env bash

# check if disconnected (30 is disconnected, 100 is connected)

server_path=/home/rock/Documenti/rockpis_server_ap/server/

function concheck {
	res=`nmcli -g GENERAL.STATE dev show wlan0 | grep 100` 
	if [ -n "$res" ]; then
		echo 0
	else
		echo 1
	fi
}


function createap {
	systemctl stop dnsmasq &&
	systemctl stop hostapd &&
	systemctl restart dhcpcd &&
	systemctl start dnsmasq &&
	systemctl start hostapd 

	res=$?
	
	echo $res 
}
	

function main {
	check=$(concheck)

	if [[ $check -eq 1 ]]; then
		echo yet disconnected 			
	else
		echo connected...

		nmcli dev disconnect wlan0 # disconnetto l'interfaccia wlan0
			
		echo now disconnected 	
	fi

	nmcli dev set wlan0 autoconnect no

	ap=$(createap)

	if [[ $ap -eq 0 ]]; then
		echo ACCESS POINT CREATED
	else
		echo SOMETHING WRONG
		exit 1
	fi

	sudo systemctl restart dnsmasq
	pkill node

	cd $server_path
	PORT=80 npm run dev
}

main
