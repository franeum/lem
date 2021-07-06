#!/usr/bin/env python3

import subprocess

def get_wifi_list():
    CMD = ['nmcli','-g','SSID','dev','wifi']
    wifi_list = subprocess.check_output(CMD).decode("utf-8")
    wifi_list = [x.strip(None) for x in wifi_list.splitlines() if x != '']
    return list(set(wifi_list))

