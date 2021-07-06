#!/usr/bin/env python3

import re
import sys 
import inspect
import subprocess as sp 


DEBUG                   = 0
WIFI_DEVICE             = re.compile(r'^w.+0$')
CONNECTION_STRING       = "nmcli d wifi connect {} password {} ifname {}"
DISCONNECTION_STRING    = "nmcli con down uuid {}"
GET_DEVICE_QUERY        = "nmcli -g GENERAL.DEVICE,GENERAL.TYPE --mode multiline dev show"
GET_UUID_QUERY          = "nmcli -g DEVICE,UUID con show --active"
GET_WIFI_LIST_QUERY     = "nmcli -g SSID,SIGNAL dev wifi list"
WIFI_STATUS             = "nmcli r wifi"
ENABLE_WIFI_QUERY       = "nmcli r wifi on"


def __run_process(query):
    res = sp.run(query.split())
    return res.returncode


def wifi_status():
    res = __nmcli_command(WIFI_STATUS)
    return {"wifi_enabled": res.decode('utf-8').strip(None) == 'enabled'}


def __format_name(dotted):
    return (dotted.split('.')[1]).lower()

 
def get_device():
    """get wifi device name"""
    res = __nmcli_command(GET_DEVICE_QUERY)
    devices = [dev.decode('utf-8').split(':') for dev \
        in res.splitlines() if dev.decode('utf-8') != '']
    container = {}
    
    for n,d in enumerate(devices):
        container[__format_name(d[0])] = d[1]

        if n % 2 == 1:
            
            if container['type'] == 'wifi':
                return container

    raise Exception("Something wrong, perhaps wifi interface is not present?")
    
 
def get_uuid():
    res = __nmcli_command(GET_UUID_QUERY)
    res = res.splitlines()

    for dev in res:
        device = dev.decode('utf-8').split(':')
        #if re.search(WIFI_DEVICE, device[0]):
        if device[0] == get_device()['device']:
            return {"uuid": device[1]}

    raise Exception("Something wrong")


def __nmcli_command(string):
    if DEBUG:
        print(string)
    else:
        return sp.check_output(string.split())


def connect_wifi(ssid, password):
    device = get_device()['device']
    string = CONNECTION_STRING.format(ssid, password, device)
    res = __run_process(string) 

    if res != 0:
        return { "connected": False }
    
    return { "connected": True } 


def disconnect_wifi():
    uuid = get_uuid()['uuid']
    string = DISCONNECTION_STRING.format(uuid)
    res = __nmcli_command(string)

    if res == 0:
        return { "connected": False }
    
    return { "connected": True }

 
def get_wifi_list():
    res = __nmcli_command(GET_WIFI_LIST_QUERY)
    res = [i.decode("utf-8").split(':') for i in res.splitlines()]
    formatted_data = {}

    to_check_doubles = []

    for item in res:
        if len(item) == 2:
            if item[0] not in to_check_doubles:
                to_check_doubles.append(item[0])
                if item[1].isdigit():
                    signal = int(item[1])
                else:
                    signal = item[1]
                formatted_data[item[0]] = signal 
            
    return formatted_data


if __name__ == "__main__":
    print(get_device())
