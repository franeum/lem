#!/usr/bin/env python3

import runshell as sh 


APD_QUERY    = "systemctl {} hostapd"
KEYWORD = ['enable','disable','start','stop']


def check_exit(status_code):

    if status_code == 0:
        return True
    else:
        return False


def command(key):
    """execute some operations over hostapd service
    """
    if key in KEYWORD:
        res = sh.run(APD_QUERY.format(key)) 
        return check_exit(res)

    raise Exception("Valid command are: 'enable','disable','start','stop'")


def status():
    """query status to hostapd service
    """
    res = sh.command(APD_QUERY.format('status'))
    return res.decode('utf-8') 


if __name__ == '__main__':
    command('enable')
    command('start')
