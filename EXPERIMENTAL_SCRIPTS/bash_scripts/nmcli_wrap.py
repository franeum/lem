#!/usr/bin/env python3

import sys 
import subprocess as sp 

def get_connection():
    data = sp.check_output(['nmcli','--terse','d','wifi'])
    data = data.decode('utf-8').split('\n')
    data = [x.split(':')[:2] for x in data]

    for c in data:
        if c[0] == '*':
            #print(f"connected to {c[1]}")
            return c[1]

    return 0


def connect_wifi(ssid, passwd):
    response = sp.check_output(['nmcli','d','wifi','connect',ssid,'password',passwd])
    print(response)
    return 1


if __name__ == "__main__":

    try:
        ssid, password = sys.argv[1], sys.argv[2]
    except IndexError:
        print("you have to provide SSID and Password")
        exit(1)

    if get_connection() == 0:
        connect_wifi(ssid, password)
        #'Vodafone-A68830632','5ea28tebya6udz3w'
    else:
        print("Already connected")
